import re
import requests
from flask import Flask
from flask import render_template

city =(str(raw_input ('Which city would you like to explore? (City, Country) \n'))).split()

search_place= city [0]

print '"Jet-setting off to "+search_place+"... "

address="+".join(city)

#print address

geocode=requests.get('http://maps.googleapis.com/maps/api/geocode/json?address={destination}'.format(destination=address))
lldat=geocode.json()
long=data.['geometry']['location']['lng']
lat=data.['geometry']['location']['lat']
longlat=",".join(lat,long)