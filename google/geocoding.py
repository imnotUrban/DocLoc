import os
from datetime import datetime
from config.db import conn
from models.geocache import geocache_table
from schemas.geocache import CacheDocument

import json
from dotenv import load_dotenv
import googlemaps

load_dotenv(dotenv_path="../.env")
key = os.getenv("API_GEOCODING")
gmaps = googlemaps.Client(key=key)

class Geocoding:
    locations = [] # list
    coordinates = [] # json
    
    def __init__(self):
        return
    
    # Comprobar si una location esta en cache y retornar la primera
    # TODO: #4 Definir el tamaño máximo de la cache, mover a otro modulo. De otro modo cambiar nombre
    # TODO: Mover al schema CacheDocument
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

    # Obtiene lat y lng del documento entrante. # TODO:(máx 10)
    def getCoordinates(self, documents) -> json:
        self.getLocations(documents)
        for place in self.locations:
            locationMatch = self.checkInCache(place)
            if (len(locationMatch) == 0):
                geocode_result = gmaps.geocode(place)
                location = place
                lat = str(geocode_result[0]["geometry"]["location"]["lat"])
                lng = str(geocode_result[0]["geometry"]["location"]["lng"]) 
                coordinate = { 
                                "date": str(datetime.now()), # Tiempo de actualizacion
                                "location": location,
                                "lat": lat,
                                "long": lng
                            }
                self.coordinates.append(coordinate)
                # Guardar en cache
                CacheDocument(location_id = 100000, # Sin este valor, se rompe. Define el limite de la cache también. Modificable
                              location = location, 
                              lat= lat, 
                              lng= lng).saveCache()
            else:
                coordinate = { 
                                "date": str(datetime.now()),
                                "location": locationMatch[0]["location"],
                                "lat": locationMatch[0]["lat"],
                                "long": locationMatch[0]["lng"]
                            }
                self.coordinates.append(coordinate) 
        return self.coordinates
        