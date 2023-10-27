from sqlalchemy import Date, and_  #Define subrutas o rutas por separado
from config.db import engine
from sqlalchemy.orm import sessionmaker
from models.document import documents

Session = sessionmaker(bind=engine)
conn = Session()

def get_all():
   return conn.query(documents).all()

# DD-MM-AAAA
def get_by_date(from_: Date, to_: Date):
   return conn.query(documents).filter(and_(documents.c.date >= from_, documents.c.date <= to_)).all()

def get_by_category(category = str):
   return conn.query(documents).filter(documents.c.category == category).all()

# def get_by_both(from_: Date, to_: Date, category = str):
#     return conn.query(documents).filter(documents.c.date >= from_, documents.c.date <= to_).all() and db.query(documents).filter(documents.c.category == category).all()