import os
from datetime import datetime
from config.db import conn
from models.geocache import geocache_table
from models.document import documents

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
    # TODO: definir el tamaño máximo de la cache, mover a otro modulo
    def checkInCache(self, location: str) -> json:
        row = conn.execute(geocache_table.select().where(geocache_table.c.location == location)).fetchone()
        if row:
            locationMatch = [{ "location_id": row[0],"location": row[1], "lat":row[2], "lng": row[3]}]
            return locationMatch
        else:
            return []
        
    # mover a otro modulo
    def saveInCache(location: json):
        conn.execute(geocache_table.insert().values(location))
        conn.commit()
        return {"msg": "documento guardado en cache con exito"}
    
    # Obtener SOLO las location entrantes para obtener: (lat, lng)
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
                coordinate = { 
                                "date": str(datetime.now()), # Tiempo de actualizacion
                                "location": place,
                                "lat": geocode_result[0]["geometry"]["location"]["lat"],
                                "long": geocode_result[0]["geometry"]["location"]["lng"]
                            }
                self.coordinates.append(coordinate)
            else:
                coordinate = { 
                                "date": str(datetime.now()),
                                "location": locationMatch[0]["location"],
                                "lat": locationMatch[0]["lat"],
                                "long": locationMatch[0]["lng"]
                            }
                self.coordinates.append(coordinate)
                self.saveInCache(coordinate)
        return self.coordinates
        