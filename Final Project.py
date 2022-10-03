<<<<<<< HEAD

import json, requests

base_url =
appid =
city =

url = f'{base_url}?q={city}&units=imperial&APPID={appid}'
print(url)
print ()

response = requests.get(url)
unformatted_data = response.json()

#print(unformatted_data)

temp = unformated_data["main"]["temp"]
print(f"The current temp is: {temp}")

temp_max = unformatted_data["main"]["temp_max"]
print(f"The max temp is: {temp_max}")
=======

import json, requests

base_url =
appid =
city =

url = f'{base_url}?q={city}&units=imperial&APPID={appid}'
print(url)
print ()

response = requests.get(url)
unformatted_data = response.json()

#print(unformatted_data)

temp = unformated_data["main"]["temp"]
print(f"The current temp is: {temp}")

temp_max = unformatted_data["main"]["temp_max"]
print(f"The max temp is: {temp_max}")
>>>>>>> a0c99a0644869b708941b48cb32545598859950e
