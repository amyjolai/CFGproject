#---------Geocode API Key ---------

<<<<<<< HEAD
# ------- URL ------- 
=======
#API KEY: AIzaSyA1SqRM6ra6Ttlt2UYE6eomDTfQDvhvgTk

#------Geocode------
city =((str(raw_input ('Which city would you like to explore?'))).strip()).strip(',')

address=(city.split()).replace(' ','+')

print 'Jet-setting off to '+city+'... '

geocode=requests.get('http://maps.googleapis.com/maps/api/geocode/json?address={destination}'.format(destination=address))
ll=
# ------- Query URL ------- 
>>>>>>> origin/master

# ------- FOURSQUARE API KEY ------- 


# Client ID: 0XFBHJXOKIQBB3FZSJJEGJFHS0WOJI5ZV3ZFDCBCWC2AVLH2
# Client SECRET: 2R0RBMTKV3LTRIPR1INR4LFQ2BNPL4FP4GG4AS2F1C4N4ZIO


"""https://api.foursquare.com/v2/venues/search?ll=51.504557,-0.017334

&query=bars=browse
&client_id=0XFBHJXOKIQBB3FZSJJEGJFHS0WOJI5ZV3ZFDCBCWC2AVLH2
&client_secret=2R0RBMTKV3LTRIPR1INR4LFQ2BNPL4FP4GG4AS2F1C4N4ZIO
&v=20161024&limit=5&rating"""

# ------- CODE ------- 

import requests

city = raw_input ('Which city would you like to explore?')

req = requests.get("https://api.foursquare.com/v2/{venues}/trending?ll=&query=bars=browse&oauth_token=SBI2I10VMO23IPNK3PU0AANO0JEHYKNGKZYNBB3ZTF3OL3EQ&v=20161111".format(city_name=city))

data =req.json()
import pdb; pdb.set_trace()

print "Here are the top trending{venues}in your desired{city}".format(city=data['city'],venues=data['city'][0]['venues'])
