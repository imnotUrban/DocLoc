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

# with open(file="./in.json", mode="r") as file:
#     inputJson = json.load(file)
    
# with open(file="./out.json", mode="r") as file:
#     outputJson = json.load(file)

# with open(file="./empty.json", mode="r") as file:
#     emptyJson = json.load(file)

class Geocoding:
    locations = []
    coordinates = []
    
    def __init__(self):
        return
    
    # Esto no deberia hacerlo geocoding  
    def checkInCache(self, location: str) -> bool:
        if conn.execute(geocache_table
                     .select()
                     .where(geocache_table.c.location == location)):
            return True
        else:
            return False
        
    def getLocations(self, documents) -> list:
        for document in documents:
          self.locations.append(document["location"])
        return self.locations
    
    def getCoordinates(self, documents) -> list:
        self.getLocations(documents)
        for place in self.locations:
            geocode_result = gmaps.geocode(place)
            coordinate = { 
                          "date": str(datetime.today), # Tiempo de actualizacion
                          "location": place,
                          "lat": geocode_result[0]["geometry"]["location"]["lat"],
                          "long": geocode_result[0]["geometry"]["location"]["lng"],
                        }
            self.coordinates.append(coordinate)
        return self.coordinates
    
    ##TODO: Actualizar tabla documents 
    # Esto no deberia hacerlo geocoding...
    # def updateDocuments(self):
    #     conn.execute(documents
    #                  .update()
    #                  .where(documents.c.id == ).)

# print(outputJson[0]["place_id"]) # Obtener más detalles del lugar o (empresa)  
# print(outputJson[0]["geometry"]["location"]) # lat y long de la geoloc
# print(outputJson[0]["geometry"]["location_type"]) # Precision de la geoloc, 4 tipos. ROOFTOP, el mejor.
