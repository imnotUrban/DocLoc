from sqlalchemy import Table, Column, Integer, String
from config.db import meta, engine

geocache_table = Table(
        "geocache", 
        meta, 
        Column("location_id", Integer, primary_key= True), 
        Column("location", String(255), nullable = False),
        Column("lat", String(255), nullable = False),
        Column("lng", String(255), nullable = False)
)

meta.create_all(engine)