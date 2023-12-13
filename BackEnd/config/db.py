from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

db_name = os.getenv("DB_NAME")
db_container_user = os.getenv("USER_DOCKER")
db_container_pass = os.getenv("PASS_DOCKER")
db_container_host = os.getenv("HOST_DOCKER")
engine = create_engine(f"mariadb+pymysql://{db_container_user}:{db_container_pass}@{db_container_host}/{db_name}") # Para docker

meta = MetaData()
Session = sessionmaker(bind=engine)
conn = Session()
