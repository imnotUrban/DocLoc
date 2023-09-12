from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

db_port = os.getenv("DB_PORT_LOCAL")
db_host = os.getenv("DB_HOST_LOCAL")

db_container = os.getenv("DB_HOST_DOCKER")

engine = create_engine(f"mariadb+pymysql://{db_user}:{db_pass}@{db_container}/{db_name}") # Para docker
# engine = create_engine(f"mariadb+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}") # Para local
meta = MetaData()
conn = engine.connect()
