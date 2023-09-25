from fastapi import APIRouter
from schemas.geocache import CacheDocument
from google.geocoding import Geocoding

import json

# Estas rutas son solo para pruebas.
# Borrar cuando salga a produccion

cache = APIRouter()

geo = Geocoding()

with open(file="google/in.json", mode="r") as file:
    inputJson = json.load(file)

with open(file="google/out.json", mode="r") as file:
    outputJson = json.load(file)

@cache.post("/addcache")
def createCacheDocument(document: CacheDocument):
    geo.getCoordinates(inputJson["data"])
    return {"msg": "Añadido correctamente"}