import phonenumbers
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
import folium
from opencage.geocoder import OpenCageGeocode
pepnumber=phonenumbers.parse(number,"IN")
location=geocoder.description_for_number(pepnumber,"en")
print(location)
service_provider = carrier.name_for_number(pepnumber, "en")
print("Service Provider:", service_provider)
key='your api key'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
# print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation.html") 