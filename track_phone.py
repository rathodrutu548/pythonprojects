import phonenumbers
from phonenumbers import geocoder
import folium
# from test import number

key="8ba6f1dd099647b6875731e5ddbc3c7d"

number=input("Enter your phone number with country code: ")
# number=phonenumbers.parse(a)
check_number=phonenumbers.parse(number)
number_location=geocoder.description_for_number(check_number,"en")
print(number_location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

# tofind the location of number
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)

query=str(number_location)
results=geocoder.geocode(query)

# for latitude and longitude 
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("mylocation.html")