import os
from datetime import datetime
from config.db import conn
from models.geocache import geocache_table
from schemas.geocache import CacheDocument
from geopy.geocoders import Nominatim

import json
from dotenv import load_dotenv
from dataclasses import dataclass


geolocator = Nominatim(user_agent="DocLoc")

@dataclass
class Geocoding:
    coordinates = []
    
    def make_doc(self, location, lat, lng):
        return { "date": str(datetime.now()), "location": location, "lat": lat, "lng": lng}

    # Obtiene lat y lng del documento entrante. # TODO:(máx 10)
    def getCoordinates(self, document) -> json:
        location = document['location']
        cached_location = CacheDocument(location=location).checkInCache()
        if cached_location is None:
            try: 
                # geocode_result = gmaps.geocode(location) # Google maps
                geocode = geolocator.geocode(location)
                if geocode == []:
                    lat = " "
                    lng = " "
                else:
                    lat = geocode.latitude
                    lng = geocode.longitude
                    # lat = str(geocode_result[0]["geometry"]["location"]["lat"]) # Google maps
                    # lng = str(geocode_result[0]["geometry"]["location"]["lng"]) # Google maps
                coordinate = self.make_doc(location=location, lat=lat, lng=lng)
                self.coordinates.append(coordinate)
                CacheDocument(location=location, lat=lat, lng=lng).saveCache()
            except Exception as e:
                raise Exception(f"Algo ha salido mal obteniendo las coordenadas: {str(e)}")
        else:
            coordinate = self.make_doc(location=cached_location["location"], lat=cached_location["lat"], lng=cached_location["lng"])
            self.coordinates.append(coordinate)
        geoResult = self.coordinates[0]
        self.coordinates = []
        return geoResult
        