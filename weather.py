import json
import requests

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

def json_convert( url: str) -> str:
    response = requests.request("GET", url)
    response_loaded: str = json.loads(response.text)
    return response_loaded

melbourne = Weather('melbourne')
sydney = Weather('sydney')
brisbane = Weather('brisbane')
adelaide = Weather('adelaide')
perth = Weather('perth')
darwin = Weather('darwin')
hobart = Weather('hobart')