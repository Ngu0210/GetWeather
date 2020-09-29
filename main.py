from typing import List, Dict, Union
from functions import location, weather_choices

print("Welcome to Australian Weather CLI!!")

exit = True

while True & exit:
    print("\n\nEnter a number corresponding to the list below:")
    usr_choice: str = input("1. Predefinied locations:\n2. Enter custom location\nEnter 'exit' anytime you want to leave the program\n")
    if usr_choice == '1':
        while True & exit:
            print("\n\nWhich city would you like to know about?")
            city: str = input("Melbourne\nSydney\nBrisbane\nAdelaide\nPerth\nDarwin\nHobart\nEnter 'back' if you want to go back\n")

            if city.lower() in location:
                while True & exit:
                    print("\n\nWhat would you like to find out:")
                    weather_options: str = input("1. Current temperature\n2. Max temperature\n3. Min temperature\n4. Feels like temperature\n5. Humidity\nEnter 'back' if you want to go back\n")
                    if weather_options in ['1','2','3','4','5']:
                        weather_choices(weather_options, city)
                    elif weather_options.lower() == 'back':
                        break
                    elif weather_options.lower() == 'exit':
                        exit = False
                    else:
                        print("\n\nPlease choose the appropraite option")
            elif city.lower() == 'back':
                break
            elif city.lower() == 'exit':
                exit = False
            elif city not in location:
                print("\n\nPlease enter appropriate city")
    elif usr_choice == '2':
        pass
    elif usr_choice.lower() == 'exit':
        exit = False
    else:
        print("\n\nPlease enter the apropraite value (1, 2, exit)")
            