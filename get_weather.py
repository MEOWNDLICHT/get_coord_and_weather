# WEATHER LOOKUP PROGRAM USING AN API FROM WEATHERAPI.COM 
""" Gets the current weather condition along with some general info about the entered location """


import requests
from get_coord import get_coordinates


def get_current_weather(coords: dict):
    if not coords:
        return
    
    api_key = str(input('Enter your API KEY here to access the weather info (from weatherapi): '))
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={coords['lat']},{coords['lon']}"
    
    
    response = requests.get(url)

    if response.status_code == 401:
        print('Enter a valid API key to access weather information.')
        return
    elif response.status_code != 200:
        print("\nThe site may be down, my apologies.\n")
        return
        

    data = response.json()

    if data['current']['is_day'] == 1:
        data['current']['is_day'] = "Day" 
    else:
        data['current']['is_day'] = "Night"


    result = {
        "location_info" : 
            {"country" : data['location']['country'],
            "place" : data['location']['name'],
            "region" : data['location']['region'],
            "localtime" : data['location']['localtime']},
        
        "weather_data" : 
            {"current_temperature" : data['current']['temp_c'],
            "feels_like" : data['current']['feelslike_c'],
            "current_cycle" : data['current']['is_day'],
            "current_condition" : data['current']['condition']['text']}
            }
    
    return result



if __name__ == "__main__":
    search_place = str(input("Enter the name of the place -> "))
    coordinates = get_coordinates(search_place)
    weather_result = get_current_weather(coordinates)


    while True:
        if coordinates or weather_result:
            print(f"\nYou searched for: {search_place.capitalize()}")

            print("\nGENERAL INFORMATION")
            for category, info in weather_result['location_info'].items():
                print(f"{category.capitalize()}: {info}")
                

            print("\nCURRENT WEATHER")
            for condition, info in weather_result['weather_data'].items():
                condition = condition.replace("_", " ").capitalize()
                print(f"{condition.capitalize()}: {info}")
            print()
        break