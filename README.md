# DocLoc

### OJO QUE EL PYTHON DEBE SER VERSIÖN 3.10 o más

#### pasos de instalación fast api - uvicorn

pip install fastapi uvicorn




#### Para levantar la api usar: 
uvicorn main:app --reload


si no les funciona, usar:

python -m uvicorn app:app --reload


### Carpetas

#### models
Se almacenan las clases 

#### providers
Conexión a la DB y esquemas para las clases y como cambian sus datos en la db

#### routes
van las rutas y las carpetas de las clases asociadas a las rutas



#### ES UN ORM NUESTRO SOFTWARE


### DB _ 
pip install SQLAlchemy



https://kb.rolosa.com/estructura-apirouter-con-fastapi-de-python/



[
  {
    "title": "string",
    "text": "string",
    "date": "string",
    "url": "string"
  },
{
    "title": "string",
    "text": "string",
    "date": "string",
    "url": "string"

  }
]




### Construir imagen docker

docker build -t docloc .

## correr imagen
docker run -p 5001:5001 docloc





## Imagen mysql
### Dockerizar mysql
docker run -d --rm --name mysqldocLoc -e MYSQL_ROOT_PASSWORD=5123123123 -e MYSQL_DATABASE=storedb -p 3308:3308 mariadb
