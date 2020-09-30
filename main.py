from weather import Weather
from typing import List, Dict, Union
from functions import location, weather_choices

print("Welcome to Australian Weather CLI!!")

exit: bool = True

while True & exit:
    print("\n\nEnter a number corresponding to the list below:")
    usr_choice: str = input("1. Predefinied locations:\n2. Enter custom location\nEnter 'exit' anytime you want to leave the program\n\n")
    if usr_choice == '1':
        while True & exit:
            print("\n\nWhich city would you like to know about?")
            city: str = input("Melbourne\nSydney\nBrisbane\nAdelaide\nPerth\nDarwin\nHobart\nEnter 'back' if you want to go back\n\n")

            if city.lower() in location:
                while True & exit:
                    print("\n\nWhat would you like to find out:")
                    weather_options: str = input("1. Current temperature\n2. Max temperature\n3. Min temperature\n4. Feels like temperature\n5. Humidity\nEnter 'back' if you want to go back\n\n")
                    if weather_options in ['1','2','3','4','5']:
                        try:
                            print("\n\n"+weather_choices(weather_options, city))
                        except:
                            pass
                    elif weather_options.lower() == 'back' or weather_options.lower() == 'b':
                        break
                    elif weather_options.lower() == 'exit' or weather_options.lower() == 'e':
                        exit = False
                    else:
                        print("\n\nPlease choose the appropraite option")
            elif city.lower() == 'back' or city.lower() == 'b':
                break
            elif city.lower() == 'exit' or city.lower() == 'e':
                exit = False
            elif city not in location:
                print("\n\nPlease enter appropriate city")
    elif usr_choice == '2':
        custom_state = input("\n\nPlease enter the state you wish to find out. (au) 'without brackets'\n")
        custom_city = input("\n\nPlease enter the city. (melbourne)\n")
        custom_location = Weather(custom_state, custom_city)

    elif usr_choice.lower() == 'exit' or usr_choice.lower() == 'e':
        exit = False
    else:
        print("\n\nPlease enter the apropraite value (1, 2, exit)")
            