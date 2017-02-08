#! python3
# quickWeather.py - prints the weather for a location from the command line.

import json, requests, sys

apiKey = "26378bcf4eaf1eb8a0bb014b4a832a28"

# Compute location from command line argumments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    location = input('What is the weather for the weather information? ')
else:
    location = ' '.join(sys.argv[1:])

#Download the JSON data from openweathermap.org's API
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, apiKey)
response = requests.get(url)
response.raise_for_status()

#Load JSON data into a python variable
weatherData = json.loads(response.text)

#Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
