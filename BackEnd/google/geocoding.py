import os
from datetime import datetime
from config.db import conn
from models.geocache import geocache_table
from schemas.geocache import CacheDocument

import json
from dotenv import load_dotenv
import googlemaps
from dataclasses import dataclass

load_dotenv(dotenv_path="../.env")
key = os.getenv("API_GEOCODING")
gmaps = googlemaps.Client(key=key)

@dataclass
class Geocoding:
    coordinates = []
    
    def make_doc(self, location, lat, lng):
        return { "date": str(datetime.now()), "location": location, "lat": lat, "lng": lng}

    # Obtiene lat y lng del documento entrante. # TODO:(máx 10)
    def getCoordinates(self, document) -> json:
        location = document['location']
        cached_location = CacheDocument(location=location).checkInCache()
        print(cached_location)
        if cached_location is None:
            try: 
                geocode_result = gmaps.geocode(location)      
                if geocode_result == []:
                    lat = " "
                    lng = " "
                else:
                    lat = str(geocode_result[0]["geometry"]["location"]["lat"])
                    lng = str(geocode_result[0]["geometry"]["location"]["lng"]) 
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
        