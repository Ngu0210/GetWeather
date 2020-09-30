import unittest
import json
import requests
from Weather import json_convert

url: str = "http://api.openweathermap.org/data/2.5/weather?q=melbourne,au&units=metric&appid=b2cf60917edb97ded95da68172607141"
response = requests.request("GET", url)
response_loaded: str = json.loads(response.text)

class testWeather(unittest.TestCase):
    def test_json_convert(self):
        result = json_convert(url)
        self.assertEqual(result, response_loaded, msg=f"Results: {result}, Expected: {response_loaded}")

