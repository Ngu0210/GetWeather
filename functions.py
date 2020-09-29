import requests
from weather import melbourne, sydney, brisbane, adelaide, perth, darwin, hobart

location: dict = {'melbourne': melbourne, 'sydney': sydney, 'brisbane': brisbane, 'adelaide':adelaide, 'perth':perth, 'darwin':darwin, 'hobart':hobart}

def weather_choices(usr_input: str, city_choice: str) -> None:
    city_choice = city_choice.lower()
    if usr_input == '1':
        print("\n\n"+location[city_choice].cur_temp())
    elif usr_input == '2':
        print("\n\n"+location[city_choice].max_temp())
    elif usr_input == '3':
        print("\n\n"+location[city_choice].min_temp())
    elif usr_input == '4':
        print("\n\n"+location[city_choice].feels_like())
    elif usr_input == '5':
        print("\n\n"+location[city_choice].humidity())  