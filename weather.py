import requests
import json
from datetime import datetime

wfile = open("weatherData.JSON","w")
location = 'Denver'
#List of current conditions: precipInches, pressureInches, windSpeed
currentPrecipList = []
currentPressureList = []
currentWindSpeedList = []

#Lists of hourly key values from JSON ordered: windGust, chanceofrain, chanceofsnow, precipInches, pressureInches, windSpeed
windGustList = []
rainChanceList = []
snowChanceList = []
precipList = []
pressureList = []
windSpeedList = [] 

##Query the wttr website with a remote shell with location details 
def get_data(C):
    try:
        url = 'https://wttr.in/'+location+'?format=j1'.format(C)
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    wfile.write(T)

##Grab the values each hour from JSON output
def parse_data():
    weatherData = open("weatherData.JSON", "r")
    data = json.load(weatherData)
    for values in data ['current_condition']:
            #Key values for current
            cPrec = [values['precipInches']]
            cPress = [values['pressureInches']]
            cWindS = [values['windspeedMiles']]
            currentPrecipList.append(cPrec)
            currentPressureList.append(cPress)
            currentWindSpeedList.append(cWindS)
    for i in data['weather']:
        for values in data['weather'][0]['hourly']:
            #Key Values for hourly
            windG = [values['WindGustMiles']]
            rainC = [values['chanceofrain']]
            snowC = [values['chanceofsnow']]
            prec = [values['precipInches']]
            press = [values['pressureInches']]
            windS = [values['windspeedMiles']]

            ##Weather Data is seperated into segements of 8 per day
            if len(windSpeedList) == 8:
                break
            else:
                windGustList.append(windG)
                rainChanceList.append(rainC)
                snowChanceList.append(snowC)
                precipList.append(prec)
                pressureList.append(press)
                windSpeedList.append(windS)

    print("Current Precipitation in Inches:", currentPrecipList)
    print("Current Pressure in inMg:", currentPressureList)
    print("CurrentWind in Miles:", currentWindSpeedList, "\n")

    print("Wind Gust in Miles:", windGustList)
    print("Rain Chance:", rainChanceList)
    print("Snow Chance:", snowChanceList)
    print("Precipitation in Inches:", precipList)
    print("Pressure in inMg:", pressureList)
    print("Wind in Miles:", windSpeedList, "\n")
    weatherData.close()

##Use those values to check if job status can be continued or canceled
def generate_status():
    ##Flatten the lists to one
    cPrecipListFloat = [item for sublist in currentPrecipList for item in sublist]
    cPressureListInt = [item for sublist in currentPressureList for item in sublist]
    cWindSpeedListInt = [item for sublist in currentWindSpeedList for item in sublist]
    windGustListInt = [item for sublist in windGustList for item in sublist]
    rainChanceListInt = [item for sublist in rainChanceList for item in sublist]
    snowChanceListInt = [item for sublist in snowChanceList for item in sublist]
    precipListFloat = [item for sublist in precipList for item in sublist]
    pressureListInt = [item for sublist in pressureList for item in sublist]
    windSpeedListInt = [item for sublist in windSpeedList for item in sublist]
    """"
    Morning 12-6 AM 
    JSON: 3 and 6 AM [0][1]

    Noon 6-12 PM 
    JSON:9 and 12 PM [2][3]

    Afternoon 12-6 PM 
    JSON: 3 and 6 PM [4][5]

    Evening 6-12 AM 
    JSON: 9 and 12 AM [6][7]
    """ 
    ##Get Current time
    now = datetime.now()

    if now.hour <= 3:
        if(int(windGustListInt[0]) >= 24):
            print("Moderate Wind Gust recorded between 12:00 AM and 3:00 AM")
        elif(int(rainChanceListInt[0]) >= 50):
            print("High Chance of rain recorded between 12:00 AM and 3:00 AM")
        elif(int(snowChanceListInt[0]) >= 50):
            print("High Chance of snow recorded between 12:00 AM and 3:00 AM")
        elif(float(precipListFloat[0]) > 0.3):
            print('Moderate Precipitation recorded between 12:00 AM and 3:00 AM')
        elif(int(windSpeedListInt[0]) >= 24):
            print('Moderate Wind Speed recorded between 12:00 AM and 3:00 AM')
        elif abs((int(pressureListInt[0])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[0]) <= 28) or (int(pressureListInt[0] >= 31)):
            print("High pressure changes recorded between 12:00 AM and 3:00 AM")
    if now.hour >= 3 and now.hour <= 6:
        if(int(windGustListInt[1]) >= 24):
            print("Moderate Wind Gust recorded between 3:00 AM and 6:00 AM")
        elif(int(rainChanceListInt[1]) >= 50):
            print("High Chance of rain recorded between 3:00 AM and 6:00 AM")
        elif(int(snowChanceListInt[1]) >= 50):
            print("High Chance of snow recorded between 3:00 AM and 6:00 AM")
        elif(float(precipListFloat[1]) > 0.3):
            print('Moderate Precipitation recorded between 3:00 AM and 6:00 AM')
        elif(int(windSpeedListInt[1]) >= 24):
            print('Moderate Wind Speed recorded between 3:00 AM and 6:00 AM')
        elif abs((int(pressureListInt[1])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[1]) <= 28) or (int(pressureListInt[1] >= 31)):
            print("High pressure changes recorded between 3:00 AM and 6:00 AM")
    if now.hour >= 6 and now.hour <= 9:
        if(int(windGustListInt[2]) >= 24):
            print("Moderate Wind Gust recorded between 6:00 AM and 9:00 AM")
        elif(int(rainChanceListInt[2]) >= 50):
            print("High Chance of rain recorded between 6:00 AM and 9:00 AM")
        elif(int(snowChanceListInt[2]) >= 50):
            print("High Chance of snow recorded between 6:00 AM and 9:00 AM")
        elif(float(precipListFloat[2]) > 0.3):
            print('Moderate Precipitation recorded between 6:00 AM and 9:00 AM')
        elif(int(windSpeedListInt[2]) >= 24):
            print('Moderate Wind Speed recorded between 6:00 AM and 9:00 AM')
        elif abs((int(pressureListInt[2])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[2]) <= 28) or (int(pressureListInt[2] >= 31)):
            print("High pressure changes recorded between 6:00 AM and 9:00 AM")
    if now.hour >= 9 and now.hour <= 12:
        if(int(windGustListInt[3]) >= 24):
            print("Moderate Wind Gust recorded between 9:00 AM and 12:00 PM")
        elif(int(rainChanceListInt[3]) >= 50):
            print("High Chance of rain recorded between 9:00 AM and 12:00 PM")
        elif(int(snowChanceListInt[3]) >= 50):
            print("High Chance of snow recorded between 9:00 AM and 12:00 PM")
        elif(float(precipListFloat[3]) > 0.3):
            print('Moderate Precipitation recorded between 9:00 AM and 12:00 PM')
        elif(int(windSpeedListInt[3]) >= 24):
            print('Moderate Wind Speed recorded between 9:00 AM and 12:00 PM')
        elif abs((int(pressureListInt[3])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[3]) <= 28) or (int(pressureListInt[3] >= 31)):
            print("High pressure changes recorded between 9:00 AM and 12:00 PM")
    if now.hour >= 12 and now.hour <= 15:
        if(int(windGustListInt[4]) >= 24):
            print("Moderate Wind Gust recorded between 12:00 PM and 3:00 PM")
        elif(int(rainChanceListInt[4]) >= 50):
            print("High Chance of rain recorded between 12:00 PM and 3:00 PM")
        elif(int(snowChanceListInt[4]) >= 50):
            print("High Chance of snow recorded between 12:00 PM and 3:00 PM")
        elif(float(precipListFloat[4]) > 0.3):
            print('Moderate Precipitation recorded between 12:00 PM and 3:00 PM')
        elif(int(windSpeedListInt[4]) >= 24):
            print('Moderate Wind Speed recorded between 12:00 PM and 3:00 PM')
        elif abs((int(pressureListInt[4])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[4]) <= 28) or (int(pressureListInt[4] >= 31)):
            print("High pressure changes recorded between 12:00 PM and 3:00 PM")
    if now.hour >= 15 and now.hour <= 18:
        if(int(windGustListInt[5]) >= 24):
            print("Moderate Wind Gust recorded between 3:00 PM and 6:00 PM")
        elif(int(rainChanceListInt[5]) >= 50):
            print("High Chance of rain recorded between 3:00 PM and 6:00 PM")
        elif(int(snowChanceListInt[5]) >= 50):
            print("High Chance of snow recorded between 3:00 PM and 6:00 PM")
        elif(float(precipListFloat[5]) > 0.3):
            print('Moderate Precipitation recorded between 3:00 PM and 6:00 PM')
        elif(int(windSpeedListInt[5]) >= 24):
            print('Moderate Wind Speed recorded between 3:00 PM and 6:00 PM')
        elif abs((int(pressureListInt[5])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[5]) <= 28) or (int(pressureListInt[5] >= 31)):
            print("High pressure changes recorded between 3:00 PM and 6:00 PM")
    if now.hour >= 18 and now.hour <= 21:
        if(int(windGustListInt[6]) >= 24):
            print("Moderate Wind Gust recorded between 6:00 PM and 9:00 PM")
        elif(int(rainChanceListInt[6]) >= 50):
            print("High Chance of rain recorded between 6:00 PM and 9:00 PM")
        elif(int(snowChanceListInt[6]) >= 50):
            print("High Chance of snow recorded between 6:00 PM and 9:00 PM")
        elif(float(precipListFloat[6]) > 0.3):
            print('Moderate Precipitation recorded between 6:00 PM and 9:00 PM')
        elif(int(windSpeedListInt[6]) >= 24):
            print('Moderate Wind Speed recorded between 6:00 PM and 9:00 PM')
        elif abs((int(pressureListInt[6])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[6]) <= 28) or (int(pressureListInt[6] >= 31)):
            print("High pressure changes recorded between 6:00 PM and 9:00 PM")
    if now.hour >= 21 and now.hour <= 24:
        if(int(windGustListInt[7]) >= 24):
            print("Moderate Wind Gust recorded between 9:00 PM and 12:00 AM")
        elif(int(rainChanceListInt[7]) >= 50):
            print("High Chance of rain recorded between 9:00 PM and 12:00 AM")
        elif(int(snowChanceListInt[7]) >= 50):
            print("High Chance of snow recorded between 9:00 PM and 12:00 AM")
        elif(float(precipListFloat[7]) > 0.3):
            print('Moderate Precipitation recorded between 9:00 PM and 12:00 AM')
        elif(int(windSpeedListInt[7]) >= 24):
            print('Moderate Wind Speed recorded between 9:00 PM and 12:00 AM')
        elif abs((int(pressureListInt[7])) - (int(cPressureListInt[0]))) >= 2 or (int(pressureListInt[7]) <= 28) or (int(pressureListInt[7] >= 31)):
            print("High pressure changes recorded between 9:00 PM and 12:00 AM")
    else:
        if(float(cPrecipListFloat[0]) > 0.3):
            print('Moderate Precipitation recorded between around current time')
        elif(int(cWindSpeedListInt[0]) >= 24):
            print('Moderate Wind Speed recorded around current time')
        print('No weather anomalies detected. Delivery will proceded as scheduled.')
#Run every hour
get_data(location)
parse_data()
generate_status()