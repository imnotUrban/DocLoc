
# DocLoc

## Introducción

DocLoc es una poderosa API en Python que se ejecuta en la versión 3.10 o superior, construida con [FastAPI](https://fastapi.tiangolo.com/) y [uvicorn](https://www.uvicorn.org/) para gestionar y ofrecer datos estructurados de manera eficiente. Esta documentación te guiará a través de los pasos de instalación y el funcionamiento de la API.

## Instalación

Asegúrate de tener instalados [Python 3.10](https://www.python.org/downloads/) y [pip](https://pip.pypa.io/en/stable/installation/) antes de continuar. Luego, instala FastAPI y uvicorn ejecutando el siguiente comando:

```bash
pip install fastapi uvicorn
```

## Ejecutar la API

Para poner en marcha la API, utiliza el siguiente comando:

```bash
uvicorn main:app --reload
```

Si esto no funciona, puedes intentar lo siguiente:

```bash
python -m uvicorn app:app --reload
```

## Estructura de Carpetas

- **models**: En esta carpeta se encuentran las clases que representan los datos manejados por la API.
- **providers**: Aquí se gestionan las conexiones a la base de datos y los esquemas para las clases, así como las transformaciones de datos en la base de datos.
- **routes**: En esta sección se definen las rutas de la API y se asocian con las clases correspondientes.

### Modelo de Datos

La API maneja datos estructurados con el siguiente formato:

```json
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
```

## Base de Datos

Para gestionar la base de datos, necesitas instalar [SQLAlchemy](https://www.sqlalchemy.org/):

```bash
pip install SQLAlchemy
```

## Referencias

- Puedes encontrar una estructura de API y router con FastAPI de Python en este [enlace](https://kb.rolosa.com/estructura-apirouter-con-fastapi-de-python/).

## Dockerización

### Construir una Imagen Docker

Para crear una imagen Docker de la aplicación, ejecuta el siguiente comando:

```bash
docker build -t docloc .
```

### Ejecutar la Imagen Docker

Luego, puedes ejecutar la imagen Docker en el puerto 5001:

```bash
docker run -p 5001:5001 docloc
```

## Dockerizar MySQL

Si necesitas una base de datos MySQL en un contenedor Docker, puedes utilizar el siguiente comando:

```bash
docker run -d --rm --name mysqldocLoc -e MYSQL_ROOT_PASSWORD=5123123123 -e MYSQL_DATABASE=storedb -p 3308:3308 mariadb
```

### Documentaciòn DocLoc

## Codigo

## Sprint

## Casos de prueba







¡Disfruta utilizando DocLoc y su entorno Dockerizado!

