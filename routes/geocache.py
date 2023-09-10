from fastapi import APIRouter
from schemas.geocache import CacheDocument
from google.geocoding import Geocoding

# Estas rutas son solo para pruebas.
# Borrar cuando salga a prod

cache = APIRouter()

@cache.post("/addcache")
def createCacheDocument(document: CacheDocument):
    document.saveCache()
    return "ok"

@cache.get("/checkcache")
def checkCacheItems(location: str):
    Geocoding().checkInCache(location)
    return "ok"