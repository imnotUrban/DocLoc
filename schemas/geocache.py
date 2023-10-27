from config.db import conn
from models.geocache import geocache_table

class CacheDocument():
    location_id: int
    location: str
    lat: str
    lng: str
    
    def __init__(self, location_id=None ,location=None, lat=None, lng=None):
        self.location_id = location_id
        self.location = location
        self.lat = lat
        self.lng = lng

    def saveCache(self):
        newDocument = {"location": self.location, "lat": self.lat, "lng": self.lng}
        conn.execute(geocache_table.insert().values(newDocument))
        conn.commit()
        
    def checkInCache(self):
        print(f"Buscando en cahe: {self.location}")
        row = conn.execute(geocache_table.select().where(geocache_table.c.location == self.location)).fetchone()
        if row:
            cached_location = [{"location_id": row[0], "location": row[1], "lat": row[2], "lng": row[3]}]
            return cached_location
        else:
            return None

    def print(self):
        print(f"{self.location_id};{self.location};{self.lat};{self.lng}")

class Config:
    orm_mode = True