#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:43:54 2015

@author: Simon
"""

from pyowm import OWM #Source: https://github.com/csparpa/pyowm
import argparse
import datetime

API_KEY = "d0cb5fa784383be285f4b7a637ea8168"

#Parse arguments
parser = argparse.ArgumentParser(description='Show the current weather.')
parser.add_argument("-l", "--location", help="The location where you want to know the weather", default="Tampere, FI")
args = parser.parse_args()
location = args.location

#Collect info
owm = OWM(API_key=API_KEY, language='en')
observation = owm.weather_at_place(location)
weather = observation.get_weather()
temp = weather.get_temperature(unit='celsius')['temp']
status = weather.get_status()
forecaster = owm.three_hours_forecast(location)
forecast = forecaster.get_forecast()
location = observation.get_location().get_name()

print ('')
print ('Current weather in %s:' %(location))
print ('Temperature: %.1f degrees celsius' %(temp))
print ('Sky: %s' %(status))
print('')
print('Forecast:')
for i in range(4):
    w = forecast.get(i)
    time_unix = w.get_reference_time()
    time_local = datetime.datetime.fromtimestamp(
        int(time_unix)
    ).strftime('%Y-%m-%d %H:%M')
    status = w.get_status()
    temp = w.get_temperature(unit='celsius')['temp']
    print ('%s %s %.1f degrees' %(time_local, status, temp))

print('')


