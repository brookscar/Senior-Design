import requests
import json

##Query the wttr website with a remote shell with location details 
# (city or gps)
##Grab the hourly values each hour from JSON output
##Specfically grab degree, description, wind, and precip values 
# put these into seperate lists
##Use those values to check if job status can be continued or canceled
# Function to Generate Report

#Weather Data
""""
Morning 0-6 AM 
JSON: 3 and 6 AM [0][1]

Noon 6-12 PM 
JSON:9 and 12 PM [2][3]

Afternoon 12-6 PM 
JSON: 3 and 6 PM [4][5]

Evening 6-12 AM 
JSON: 9 and 12 AM [6][7]
"""

file1 = open("weatherData.JSON","w")
location = 'Denver'

def get_data(C):
    try:
        url = 'https://wttr.in/'+location+'?format=j1'.format(C)
        data = requests.get(url)
        T = data.text
        
    except:
        T = "Error Occurred"
    file1.write(T)
    ##print(T)

def parse_data(D):
    hourlyList = []
    data = json.load(D)
    ##Weather Data is seperated into segements of 8
    hours = []
    for i in data['weather']:
        for values in data['weather'][0]['hourly']:
            print("Values: ", values)
            hours = [values['FeelsLikeF']]
            print()
            if len(hourlyList) == 8:
                break
            else:
                hourlyList.append(hours)
    print(hourlyList)
    print()
    # Closing file
    
    D.close()


get_data(location)
weatherData = open("weatherData.JSON", "r")
parse_data(weatherData)

""""
def item_generator(lookup_key):
    with open("weatherData.json") as D:
        json_input = json.load(D)
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

wind = []
for i in item_generator("WindGustMiles"):
    ans = {"WindGustMiles" : i}
    wind.append(ans)

print(wind)
"""