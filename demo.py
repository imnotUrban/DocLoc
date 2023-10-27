import httpx
import json
import asyncio

# URL de la API
url = "http://127.0.0.1:8000/geolocalize"

async def enviar_documentos(noticia):
    async with httpx.AsyncClient(timeout=300) as client:
        response = await client.post(url, json=noticia) # json=doc, es lo que se envía a la API
    if response.status_code == 200: # Respuesta buena
        print(f"Listo: {noticia[0]['title']}")
    else:
        print(f"Error al llamar a la API. Código de estado: {response.status_code}")
        print("Respuesta de la API:", response.text)

with open('noticias.json', 'r') as jf: 
    noticias = json.load(jf)

async def send():
    for noticia in noticias[68:]:
        await enviar_documentos([noticia])
        await asyncio.sleep(15)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send())
