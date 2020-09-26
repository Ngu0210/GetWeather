import requests
import json


class Weather():
    

    def __init__(self, location, state_code):
        self.location = location
        self.state_code = state_code

    def cur_temp(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"{json_convert(url)['main']['temp']} Degrees Celsius"   

    def max_temp(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location},{self.state_code}&units=metric&appid=b2cf60917edb97ded95da68172607141"
        return f"{json_convert(url)['main']['temp_max']} Degrees Celcius"


def json_convert(url):
    response = requests.request("GET", url)
    response_loaded = json.loads(response.text)
    return response_loaded

location = []

melbourne = Weather('melbourne', 'au')

print("Welcome to Australian Weather CLI!!")

location = input("Which city are you located in Australia?")

print(melbourne.cur_temp())