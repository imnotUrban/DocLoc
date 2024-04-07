from config.db import conn
from models.geocache import geocache_table
from pydantic import BaseModel

class CacheDocument(BaseModel):
    location_id: int | None = None
    location: str
    lat: float | None = None
    lng: float | None = None
    
    def saveCache(self):
        newDocument = {"location": self.location, "lat": self.lat, "lng": self.lng}
        try:
            conn.execute(geocache_table.insert().values(newDocument))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
        
    def checkInCache(self):
        print(f"Buscando en cache: {self.location}")
        try:
            row = conn.execute(geocache_table.select().where(geocache_table.c.location == self.location)).fetchone()
            conn.commit()
            if row:
                return {"location_id": row[0], "location": row[1], "lat": row[2], "lng": row[3]}
            else:
                return None
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
