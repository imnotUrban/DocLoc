from sqlalchemy import Table, Column, Integer, String, Float
from config.db import meta, engine

geocache_table = Table(
        "geocache", 
        meta, 
        Column("location_id", Integer, primary_key = True, autoincrement = True), 
        Column("location", String(255), nullable = False),
        Column("lat", Float, nullable = True),
        Column("lng", Float, nullable = True)
)

meta.create_all(engine)