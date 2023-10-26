import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
print(response)
# print(response.json())

for data in response.json()['items']:
    print(data['title'])
    # print(data['link'])

var = requests.status_codes
print(var)
