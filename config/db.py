from sqlalchemy import create_engine, MetaData
### Usuario:contraseña
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/storedb")
meta = MetaData()
conn = engine.connect()