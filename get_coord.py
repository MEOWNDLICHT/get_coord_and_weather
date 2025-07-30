# COORDINATES LOOKUP USING OPENWEATHERMAP'S API

import requests


def get_coordinates(place: str) -> dict[str: float]: 
    # returns early if place is blank or not str
    if not place or not place.isalpha():
        print('Enter a valid place.')
        return

    api_key = str(input('Enter your API KEY here to access the coordinates info (from openweathermap): '))
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&appid={api_key}"

    try:
        response = requests.get(url)

        # For returning early for invalid API
        if response.status_code == 401:
            print('Enter a valid API key.')
            return
        
        data = response.json()
        coordinates = {"lat" : data[0]['lat'], "lon" : data[0]['lon']}
    


    except requests.exceptions.HTTPError as http_error:
        print(f"An HTTP error occured: {http_error}")
        return()
    
    
    except IndexError:
        print(f"\n'{place}' cannot be found!\nEnter a valid place.\n")
        return
    
    except KeyError:
        print("\nPlease enter anything. As long as it's a real place.\n")
        return
    
    return coordinates



if __name__ == '__main__':
    place = input("Enter a place -> ")
    coordinates_data = get_coordinates(place)

    while True:
        if coordinates_data:
            print("\nThe coordinates of the place are:")
            print(f"lat: {coordinates_data['lat']}\nlon: {coordinates_data['lon']}\n")
        break