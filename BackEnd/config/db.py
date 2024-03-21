from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

db_name = os.getenv("DB_NAME")

# dev_user = os.getenv("DEV_USER")
# dev_pass = os.getenv("DEV_PASS")
# dev_port = os.getenv("DEV_PORT")
# dev_host = os.getenv("DEV_IP")
# engine = create_engine(f"mariadb+pymysql://{dev_user}:{dev_pass}@{dev_host}:{dev_port}/{db_name}?charset=utf8mb4") # Dev - Local

prod_user = os.getenv("PROD_USER")
prod_pass = os.getenv("PROD_PASS")
prod_host = os.getenv("PROD_HOST")
engine = create_engine(f"mariadb+pymysql://{prod_user}:{prod_pass}@{prod_host}/{db_name}?charset=utf8mb4") # Prod - Docker

meta = MetaData()
Session = sessionmaker(bind=engine)
conn = Session()
