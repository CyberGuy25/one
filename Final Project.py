
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
