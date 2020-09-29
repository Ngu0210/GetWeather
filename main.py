import requests
import json

from typing import List, Dict, Union


class Weather():
    

    def __init__(self, location: str, state_code: str='au') -> None:
        self.location = location
        self.state_code = state_code

    def cur_temp(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"{json_convert(url)['main']['temp']} Degrees Celsius"   

    def max_temp(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"{json_convert(url)['main']['temp_max']} Degrees Celcius"

    def min_temp(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"{json_convert(url)['main']['temp_min']} Degrees Celcius"
    
    def feels_like(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"{json_convert(url)['main']['feels_like']} Degrees Celcius"

    def humidity(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"Humidity: {json_convert(url)['main']['humidity']}%"


def json_convert(url: str) -> str:
    response = requests.request("GET", url)
    response_loaded: str = json.loads(response.text)
    return response_loaded

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
    

melbourne = Weather('melbourne')
sydney = Weather('sydney')
brisbane = Weather('brisbane')
adelaide = Weather('adelaide')
perth = Weather('perth')
darwin = Weather('darwin')
hobart = Weather('hobart')

location: dict = {'melbourne': melbourne, 'sydney': sydney, 'brisbane': brisbane, 'adelaide':adelaide, 'perth':perth, 'darwin':darwin, 'hobart':hobart}

print("Welcome to Australian Weather CLI!!")

while True:
    print("Enter a number corresponding to the list below:")
    usr_choice: str = input("1. Predefinied locations:\n2. Enter custom location\n")

    if usr_choice != '1' and usr_choice != '2':
        print("Please enter appropriate options (1 or 2)")
    elif usr_choice == '1':
        while True:
            print("\n\nWhich city would you like to know about?")
            city: str = input("Melbourne\nSydney\nBrisbane\nAdelaide\nPerth\nDarwin\nHobart\n")

            if city.lower() in location:
                while True:
                    print("\n\nWhat would you like to find out:")
                    weather_options: str = input("1. Current temperature\n2. Max temperature\n3. Min temperature\n4. Feels like temperature\n5. Humidity\n")
                    if weather_options in ['1','2','3','4','5']:
                        weather_choices(weather_options, city)
                    else:
                        print("Please choose the appropraite option")
            elif city not in location:
                print("Please enter appropriate city")


print(melbourne.cur_temp())