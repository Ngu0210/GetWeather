import requests
import json

from typing import List, Dict, Union


class Weather():
    

    def __init__(self, location: str, state_code: str='au') -> None:
        self.location = location
        self.state_code = state_code

    def cur_temp(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"{json_convert(url)['main']} Degrees Celsius"   

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
        return f"{json_convert(url)['main']['humidity']} Degrees Celcius"


def json_convert(url: str) -> str:
    response = requests.request("GET", url)
    response_loaded = json.loads(response.text)
    return response_loaded

melbourne = Weather('melbourne')
sydney = Weather('sydney')
queensland = Weather('queensland')
adelaide = Weather('adelaide')
perth = Weather('perth')
darwin = Weather('darwin')
hobart = Weather('hobart')
canberra = Weather('canberra')
ginifer = Weather('ginifer')

print("Welcome to Australian Weather CLI!!")

city: str = input("Which city are you located in Australia?")

location.append(city)

print(melbourne.cur_temp())