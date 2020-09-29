from typing import List, Dict, Union
from functions import location, weather_choices

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