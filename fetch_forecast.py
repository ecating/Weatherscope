import requests #allows python to fetch data using APIs.  
import json #the parsing notation I will be using
from pprint import pprint #pprint makes JSON data human-readable
import time

#Variables that I may need to edit frequently
weather_map = 'http://api.openweathermap.org/data/2.5/forecast?'
city = 'zip=27510'
API_key = 'd05b7257b76f9e1bd5636b3555dec813'

#building the URL for the API
#typical value: http://api.openweathermap.org/data/2.5/forecast?zip=27510&APIkey=d05b7257b76f9e1bd5636b3555dec813
API_string = '&APIkey=' + API_key
weather_URL = weather_map + city + API_string



#Fetching the data from the API
five_day_forecast = requests.get(weather_URL) #get the five day forecast
five_day_header = five_day_forecast.headers #get the headers (not necessary now)
#Parse the JSON data
#'list' gives all the forecast data for the next 5 days in 3 hour increments
five_day_weather = requests.get(weather_URL).json()['list']
nine_hour_weather = [] #defining this as an empty list for future use

#get the current time. We only want weather forecasts within 9 hours of current time
current_time = time.time() #provides in unix time (seconds since 00:00:00, Jan 1, 1970)
end_time = current_time + 9*60*60 #converting 9 hrs into seconds, adding to current_time
""" Eventually I would like to change this so that it shows the high and low for the day between 7 am and 8 pm
and at 8 pm it changes to show TOMORROW's high and low for the same time period."""

"""This loops through every forecast in the five day weather forecast from OpenWeatherMap.
It adds all the forecasts from 3 hours ago until 9 hours from now to a new list called
nine_hour_weather."""
for forecast in five_day_weather: #cycles through every forecast in the 5 day forecast list 
    if forecast['dt']>(current_time - 3*60*60) and forecast['dt']<end_time: #for each forecast within our time of interest
        nine_hour_weather.append(forecast) #This may be unnecessary.
"""
This code fetches the maximum (minumum) value for the temperature 
"""
todays_high = max(nine_hour_weather, key=lambda x: x['main']['temp_max'])['main']['temp_max']
todays_low = min(nine_hour_weather, key=lambda x: x['main']['temp_min'])['main']['temp_min']
#find the humidity for the next nine hours using list comprehension
humidity = [x['main']['humidity'] for x in nine_hour_weather] 
humidity = int(sum(humidity)/len(humidity)) #average the humidity, convert to an integer value
print(humidity)
"""Eventually, these values will be fetched from OpenWeatherMap
weather_ID is a particular, numerical value in the JSON data from OpenWeatherMap.
weather_icon is another value but uneccessary for now. May be useful later on.
"""
#use list comprehension to get every weather.id value for the 8 hour period
#THIS ISN"T FUCKING WORKING AND I DON"T KNOW WHY!!!
weather_ids = [y['weather']['id'] for y in nine_hour_weather]

"""These are the codes used by OpenWeatherMap for various types of weather
events """
lightning = [200,201,202,210,211,212,221,230,231,232]
heavy_rain = [501,502,503,504,521,522,531]
light_rain = [300,301,302,310,311,312,313,314,321,500,520,701]
snow = [600,601,602,611,612,615,616,620,621,622,511]
sun = [800]
clouds = [801,802,803,804]
extreme = [781,900,901,902,903,904,905,906,961,962]


"""If the value of weather_ID is contained in a particular set of weather codes
shown above, it will trigger a particular lighting program on the Arduino. Each
catagory listed will have its own light/water program on the Arduino
This means each catagory will need to trigger a different GPIO output. Can do
this using 3 pins in binary, I think.
for each weather.id in the nine hour time period we check what catagory it is in.
"""
weather_counter = 0
for weather_ID in weather_ids:              
    if weather_ID in lightning:
        print('lightning')
        weather_counter += 1
    if weather_ID in heavy_rain:
        print('heavy_rain')
        weather_counter += 1
    if weather_ID in light_rain:
        print('light_rain')
        weather_counter += 1
    if weather_ID in snow:
        print('snow')
        weather_counter += 1
    if weather_ID in sun:
        print('sun')
        weather_counter += 1
    if weather_ID in clouds:
        print('clouds')
        weather_counter += 1
    if weather_ID in extreme:
        print('Extreme Weather Warning!')
        weather_counter += 1
    if weather_counter == 0:
        print('Weather condition unknown!')

""" Write code here to display the high and low temperature for the day
"""
