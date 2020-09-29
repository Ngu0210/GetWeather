from typing import Optional
from weather import melbourne, sydney, brisbane, adelaide, perth, darwin, hobart

location: dict = {'melbourne': melbourne, 'sydney': sydney, 'brisbane': brisbane, 'adelaide':adelaide, 'perth':perth, 'darwin':darwin, 'hobart':hobart}

def weather_choices(usr_input: str, city_choice: str):
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