#program uses a website to give the weather reports to the user

import json, requests
#Need library to call webservice

from requests.exceptions import HTTPError
#verifies web connection
try:
  response = requests.get('http://openweathermap.org/?')
  response.raise_for_status()
  #access JSON content
  jsonResponse = response.json()
  print("Entire JSON response")
  print(jsonResponse)

except HTTPError as http_err:
  print(f'HTTP error occured: {http_err}')
except Exception as err:
  print(f'Other error occured while attempting to verify HTTP: {err}')


print("Welcome to the weather program")
#Welcome intro

def main():
#loops back to here

  base_url = "https://api.openweathermap.org/data/2.5/weather"
  #website we pull the info from

  appid = "2b886554a5810e4614bc73e0f57a5566"
  #key that allows us to pull info from       https://home.openweathermap.org/api_keys

  city=str(input("Please enter the city name or zip code of the city you would like to know the weather?:"))
  #ask for user to input city

  url = f'{base_url}?q={city}&units=imperial&APPID={appid}'
  #print(url)
  #print ()
  #if we wanted to print  the url

  response = requests.get(url)
  #using a request library

  unformated_data = response.json()
  #response is in json

  #print(unformated_data)

  try:

    temp = unformated_data["main"]["temp"]
    print(f"The current temp is: {temp}")
    #showing current temp to user

    temp_max = unformated_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")
    #showing max temp to user

    temp_min = unformated_data["main"]["temp_min"]
    print(f"The min temp is: {temp_min}")
    #showing min temp to user

    rerun=input("would you like to try again?:")
    #rerun or exit program
    if rerun == "yes" or rerun == "y":
      main()
    else:
      print("End Program")
      exit()

  except KeyError:
    print(f"{city} city is unrecognized(please type the city name or enter a zipcode in digits")
    #catches unrecognized city inputs and alerts the user

    restart=input("Would you like to try again?:")
    #restart or exit program
    if restart == "yes" or restart == "y":
      main()
    else:
      print("End Program")
      exit()
      #allows the user to either try to input a city correctly or exit the program

main()
