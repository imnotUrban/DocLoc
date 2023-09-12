from pydantic import BaseModel
from config.db import conn
from models.geocache import geocache_table

class CacheDocument(BaseModel):
    location_id: int
    location: str
    lat: str
    lng: str
    
    def saveCache(self):
        newDocument = {"location" : self.location, "lat": self.lat, "lng": self.lng}
        conn.execute(geocache_table
                        .insert()
                        .values(newDocument))
        conn.commit()
    
class Config:
    orm_mode = True