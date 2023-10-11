from sqlalchemy import Table, Column, Integer, String, Text
from config.db import meta, engine


documents = Table("documents", meta, Column(
    "id", Integer, primary_key= True), 
    Column("title", String(255),nullable = False), 
    Column("text", Text,nullable = False),
    Column("date", String(255),nullable = False),
    Column("url", String(255),nullable = False),
    Column("state", Integer,nullable = False),
    Column("result", Text),
    Column("lat", String(255)),
    Column("long", String(255))
    )

meta.create_all(engine)