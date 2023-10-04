import httpx
import asyncio
import random
import pandas as pd
import time
import json

csv_file = "./gpt/noticias-2023-05-31.csv"
data = pd.read_csv(csv_file)
TIMEOUT = 300 # Tiempo maximo que esperamos la respuesta de la API (en segundos)

def tiempo_de_ejecucion(inicio):
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")

def print_resultados(data):
    for doc in data:
        print(f"Location: {doc['location']}, ({doc['lat']}, {doc['lng']})")

n_noticias = 1
docs = []
#Toma noticias random de un csv
for i in range(n_noticias):
    top = data.shape[0] - i
    random_index = random.randint(0, top)
    new = data.iloc[random_index]
    doc = {
        "id": random_index,
        "title": new["title"],
        "date": new["date"],
        "text": new["text"],
        "url": new["url"]
    }
    docs.append(doc)


for doc in docs:
    titulo = str(doc['title'][:50])
    print(f"Fila: {doc['id']}\t Titulo: {titulo}...")

# Para guardar el doc en un .json
# with open('doc.json', 'w') as jf: 
#     json.dump(docs[0], jf, ensure_ascii=False, indent=4)

# Para testear un archivo
# with open('doc.json', 'r') as doc: 
#     doc = json.load(doc)
#     docs.append(doc)

# URL de la API
url = "http://127.0.0.1:8000/geolocalize"

# Realiza una solicitud POST a la API con la lista de documentos
async def enviar_documentos():
    # Ajustar el timeout en caso de demora, actualmente 300 segundos
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        inicio = time.time()
        response = await client.post(url, json=docs) # json=doc, es lo que se envia a la API

    if response.status_code == 200: # Respuesta buena
        tiempo_de_ejecucion(inicio)
        data = response.json()
        print(f"Respuesta de la API:")
        print_resultados(data)
    else:
        tiempo_de_ejecucion(inicio)
        print(f"Error al llamar a la API. Código de estado: {response.status_code}")
        print("Respuesta de la API:", response.text)

# Ejecuta la función para enviar los documentos a la API
asyncio.run(enviar_documentos())