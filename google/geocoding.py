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
    locations = [] # list
    coordinates = [] # json
    
    def checkInCache(self, location: str) -> json:
        row = conn.execute(geocache_table.select().where(geocache_table.c.location == location)).fetchone()
        if row:
            locationMatch = [{ "location_id": row[0],"location": row[1], "lat":row[2], "lng": row[3]}]
            return locationMatch
        else:
            return []
        
    # Obtener las location entrantes, para obtener: lat y lng
    def getLocations(self, documents) -> list:
        for document in documents:
          self.locations.append(document["location"])
        return self.locations

    def make_doc(self, location, lat, lng):
        return { "date": str(datetime.now()), # Tiempo de actualizacion
                "location": location,
                "lat": lat,
                "lng": lng
                }

    # Obtiene lat y lng del documento entrante. # TODO:(máx 10)
    def getCoordinates(self, document) -> json:
        place = document['location']
        locationMatch = self.checkInCache(place)
        if (len(locationMatch) == 0):
            geocode_result = gmaps.geocode(place)
            location = place
            if geocode_result == []:
                lat = " "
                lng = " "
            else:
                lat = str(geocode_result[0]["geometry"]["location"]["lat"])
                lng = str(geocode_result[0]["geometry"]["location"]["lng"]) 
            coordinate =  self.make_doc(location=location, lat=lat, lng=lng)
            self.coordinates.append(coordinate)
            temp = CacheDocument(location = location, lat = lat, lng = lng)
            temp.saveCache()
            
        else:
            match = locationMatch[0]
            coordinate =  self.make_doc(location=match["location"], lat=match["lat"], lng=match["lng"])
            self.coordinates.append(coordinate)
        geoResult = self.coordinates
        self.coordinates = []
        return geoResult
        