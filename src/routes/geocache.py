from fastapi import APIRouter
from ..schemas.geocache import CacheDocument
from ..google.geocoding import Geocoding

import json

# Estas rutas son solo para pruebas.
# Borrar cuando salga a produccion

cache = APIRouter()

with open(file="google/in.json", mode="r") as file:
    inputJson = json.load(file)

with open(file="google/out.json", mode="r") as file:
    outputJson = json.load(file)

# Este no se porque lo hice xd
with open(file="google/empty.json", mode="r") as file:
    emptyJson = json.load(file)

@cache.post("/addcache")
def createCacheDocument(document: CacheDocument):
    document.saveCache()
    return {"msg": "Añadido correctamente"}

@cache.get("/checkcache")
def checkCacheItems(location: str):
    # result = Geocoding().getCoordinates(inputJson["data"])
    return 0