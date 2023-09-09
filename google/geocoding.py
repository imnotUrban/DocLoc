import googlemaps
from datetime import datetime

from dotenv import load_dotenv
import os
import json

text = '''[
  {
    "location": "New York",
    "summary": "A vibrant city"
  },
  {
    "location": "Los Angeles",
    "summary": "City of Angels"
  },
  {
    "location": "San Francisco",
    "summary": "Tech hub by the bay"
  }
]
'''
# JSON de juguete
data = json.loads(text)

load_dotenv(dotenv_path=".env")
key = os.getenv("API_GEOCODING")
gmaps = googlemaps.Client(key=key)

class Geocoding:
    locations = []
    coordinates = []
    def __init__(self):
        return

    def getLocations(self, documents):
        for document in documents:
            self.locations.append(document["location"])
        return self.locations
    
    def getCoordinates(self,documents):
        self.getLocations(documents)
        for place in self.locations:
            geocode_result = gmaps.geocode(place)
            coordinate = { 
                        "location": place,
                        "lat": geocode_result[0]["geometry"]["location"]["lat"],
                        "long": geocode_result[0]["geometry"]["location"]["lng"],
                        "summary": []
                        }
            self.coordinates.append(coordinate)
        return self.coordinates

geo = Geocoding().getCoordinates(data)
print(geo)

# geocode_result = json.loads('''[{
#     "address_components": 
#     [
#         {"long_name": "Google Building 40", "short_name": "Google Building 40", "types": ["premise"]}, 
#         {"long_name": "1600", "short_name": "1600", "types": ["street_number"]}, 
#         {"long_name": "Amphitheatre Parkway", "short_name": "Amphitheatre Pkwy", "types": ["route"]}, 
#         {"long_name": "Mountain View", "short_name": "Mountain View", "types": ["locality", "political"]}, 
#         {"long_name": "Santa Clara County", "short_name": "Santa Clara County", "types": ["administrative_area_level_2", "political"]}, 
#         {"long_name": "California", "short_name": "CA", "types": ["administrative_area_level_1", "political"]}, 
#         {"long_name": "United States", "short_name": "US", "types": ["country", "political"]}, 
#         {"long_name": "94043", "short_name": "94043", "types": ["postal_code"]}
#     ], 
#     "formatted_address": "Google Building 40, 1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA", 
#     "geometry":
#     {
#         "bounds":
#         {
#             "northeast":
#             {
#                     "lat": 37.4226618, "lng": -122.0829302
#             }, 
#             "southwest": 
#             {
#                 "lat": 37.4220699, "lng": -122.084958
#             }
#         }, 
#         "location": 
#             {
#                 "lat": 37.4223878, "lng": -122.0841877
#             }, 
#         "location_type": "ROOFTOP", 
#         "viewport": 
#             {
#                 "northeast": 
#                 {
#                     "lat": 37.42372298029149, 
#                     "lng": -122.0825951197085
#                 }, 
#                 "southwest": 
#                 {
#                     "lat": 37.4210250197085, 
#                     "lng": -122.0852930802915
#                 }
#             }
#         },
#         "place_id": "ChIJj38IfwK6j4ARNcyPDnEGa9g", 
#         "types": ["premise"]
#     }
# ]''')

# print(geocode_result[0]["place_id"]) # Obtener más detalles del lugar o (empresa)  
# print(geocode_result[0]["geometry"]["location"]) # lat y long de la geoloc
# print(geocode_result[0]["geometry"]["location_type"]) # Precision de la geoloc, 4 tipos. ROOFTOP, el mejor.
