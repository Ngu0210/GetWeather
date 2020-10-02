# Australia Weather CLI Solution
## Introduction:
Welcome to Australia Weather CLI, this program will utilise an API Openweathermap. This api provide real time weather data around the world! 

The program will provide real time weather temperture, max temperature, min temperature, feels like temperature and humidity of pre defined location all around Australia. As for the users who wants to know the weather from a location outside Australia, there is an option to do so.

## Inputs and Outputs
This program will be displayed as an CLI (Command Line Interface). So all input will have to be written down in the Terminal. The inputs expected will be shown on the terminal instructions/guides (specifically the predefined locations). Whereas the custom location, the user will be expected to enter the state code such as (us, au, nz) and the city of that state (new york, melbourne, auckland).

In anycase where the user enters a value that is incorrect/unexpected/doesn't exist, the program will prompt the user the faults they've made and will give the user an option to redo the inputs again.

## Structure

The whole coding format will be split into 3 files, *main*, *functions*, *weather*. The main file we consist of print statements, control flow statements, loops, and calls of functions. The function file will contain most of the functions that has been defined in the code for cleanliness and consistency. The weather file will contain the calls of the API and return the results of thsose calls.

Another folder *test* will be created for the program which will test most functions of the program.

