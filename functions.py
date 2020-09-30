from typing import Optional
from weather import melbourne, sydney, brisbane, adelaide, perth, darwin, hobart

location: dict = {'melbourne': melbourne, 'sydney': sydney, 'brisbane': brisbane, 'adelaide':adelaide, 'perth':perth, 'darwin':darwin, 'hobart':hobart}

def weather_choices(usr_input: str, city_choice: str):
    try:
        city_choice = city_choice.lower()
        if usr_input == '1':
            return location[city_choice].cur_temp()
        elif usr_input == '2':
            return location[city_choice].max_temp()
        elif usr_input == '3':
            return location[city_choice].min_temp()
        elif usr_input == '4':
            return location[city_choice].feels_like()
        elif usr_input == '5':
            return location[city_choice].humidity()
        else:
            return None
    except:
        print("\n\nConnection dropped, try again!")

def custom_weather_choices(usr_input, custom_location):
    try:
        if usr_input == '1':
            return custom_location.cur_temp()
        elif usr_input == '2':
            return custom_location.max_temp()
        elif usr_input == '3':
            return custom_location.min_temp()
        elif usr_input == '4':
            return custom_location.feels_like()
        elif usr_input == '5':
            return custom_location.humidity()
        else:
            return None
    except:
        print("\n\nConnection dropped, try again!")

def check_exists(custom_location):
    try:
        custom_location.main()
        return ""
    except:
        return True