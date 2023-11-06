import phonenumbers
from phonenumbers import geocoder
from test import number
import folium
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier

Key= "6313d5545d7249f8a4700ae4a74855fe"

check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(Key)
query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

map_location = folium.Map(location= [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup = number_location).add_to(map_location)
map_location.save("location.html")
