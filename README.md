# Documentación de DocLoc API

## Introducción

DocLoc es una poderosa API en Python que se ejecuta en la versión 3.10 o superior, construida con [FastAPI](https://fastapi.tiangolo.com/) y [uvicorn](https://www.uvicorn.org/) para gestionar y ofrecer datos estructurados de manera eficiente. Esta documentación te guiará a través de los pasos de instalación y el funcionamiento de la API.
---

## **Instalación**

Para integrar **DocLoc API** en tu aplicación, sigue estos pasos:

### **Paso 1: Instalar la biblioteca de cliente**

Utiliza la biblioteca de cliente oficial de **DocLoc API** en tu proyecto. Puedes instalarla mediante **`pip`**, el administrador de paquetes de Python. Ejecuta el siguiente comando en tu terminal:

```bash
pip install docloc
```

### **Paso 2: Configurar la clave de API**

En tu aplicación, configura la clave de API que has obtenido de la forma que hayas establecido previamente. Esto normalmente se hace durante la inicialización de la biblioteca de cliente. Aquí tienes un ejemplo en Python:

```python
import docloc

# Configura la clave de API (reemplaza 'TU_CLAVE_DE_API' con tu clave real)
docloc.configurar(api_key='TU_CLAVE_DE_API')
```

Con la biblioteca de cliente de **DocLoc API** correctamente instalada y configurada, estás listo para comenzar a geolocalizar documentos territoriales. Consulta nuestra sección de **Utilización** para obtener ejemplos de cómo enviar consultas y procesar las respuestas de la API.

---

## Utilización

**DocLoc API** es fácil de usar para geolocalizar documentos territoriales. Sigue estos pasos para realizar una consulta y obtener la geolocalización de un documento:

### Paso 1: Realizar una Consulta

Para geolocalizar un documento territorial, debes enviar una solicitud HTTP POST a la siguiente URL:

```
https://api.docloc.com/geolocalizar
```

### Parámetros de Consulta

Asegúrate de incluir los siguientes parámetros en tu solicitud:

- **Título**: El título del documento.
- **Fecha**: La fecha del documento en formato YYYY-MM-DD.
- **Cuerpo**: El texto o contenido del documento.
- **Enlace**: El enlace al documento original.

A continuación se muestra un ejemplo de solicitud HTTP POST:

```python
POST https://api.docloc.com/geolocalizar
Content-Type: application/json
Authorization: Bearer TU_CLAVE_DE_API

[
	{
	  "titulo": "Ejemplo de Documento 1",
	  "fecha": "2023-08-28",
	  "cuerpo": "Este es un ejemplo de texto de un documento territorial 1.",
	  "enlace": "https://enlace-al-documento-original.com"
	},
	{
	  "titulo": "Ejemplo de Documento 2",
	  "fecha": "2023-08-28",
	  "cuerpo": "Este es un ejemplo de texto de un documento territorial 2.",
	  "enlace": "https://enlace-al-documento-original.com"
	}
]
```

### Paso 2: Obtener la Geolocalización

La API procesará tu solicitud y responderá con la geolocalización en forma de latitud y longitud. Aquí tienes un ejemplo de respuesta:

```json
[
	{
		"titulo":"Ejemplo de documento 1",
	  "latitud": 40.7128,
	  "longitud": -74.0060
	  "desc" : "Se creó un ejemplo de documento 1.",
	  "fecha" : "2023-08-28"
	},
	{
		"titulo":"Ejemplo de documento 2",
	  "latitud": 89.4241,
	  "longitud": -47.4245,
	  "desc" : "Se creó un ejemplo de documento 2.",
	  "fecha" : "2023-08-28"
	}
]
```

### Ejemplo de Implementación en Python

A continuación, te mostramos un ejemplo de cómo realizar una consulta a **DocLoc API** en Python:

```python
import docloc

# Configura la URL de la API
url = "https://api.docloc.com/geolocalizar"

# Configura los parámetros de la consulta
payload = [{
    "titulo": "Ejemplo de Documento 1",
    "fecha": "2023-08-28",
    "cuerpo": "Este es un ejemplo de texto de un documento territorial 1.",
    "enlace": "https://enlace-al-documento-original.com"
},{
    "titulo": "Ejemplo de Documento 2",
    "fecha": "2023-08-28",
    "cuerpo": "Este es un ejemplo de texto de un documento territorial. 2",
    "enlace": "https://enlace-al-documento-original.com"
}
]

# Configura la clave de API (reemplaza 'TU_CLAVE_DE_API' con tu clave real)
headers = {
    "Authorization": "Bearer TU_CLAVE_DE_API"
}

# Realiza la solicitud POST
response = docloc.post(url, json=payload, headers=headers)

# Obtiene la respuesta en formato JSON
resultado = response.json()

# Muestra la geolocalización del documento 1
print("nombre_doc :", resultado[0]["nombre_doc"])
print("Latitud:", resultado[0]["latitud"])
print("Longitud:", resultado[0]["longitud"])
print("desc :", resultado[0]["desc "])
print("fecha:", resultado[0]["fecha"])
```

¡Eso es todo! Ahora puedes utilizar **DocLoc API** para geolocalizar documentos territoriales de manera efectiva en tu aplicación.
