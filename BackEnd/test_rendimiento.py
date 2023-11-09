# pytest -s test_rendimiento.py
from routes.document import document
from gpt.GPTQueryEngine import GPTQueryEngine
from google.geocoding import Geocoding
from fastapi.testclient import TestClient
from datetime import datetime
from main import app
import time


client = TestClient(app)

def testBenchmark():
    start_time = time.time()
    # Caso de prueba 1: Enviar un documento válido
    response = client.post("/geolocalize", json=[
    {
        "id": 4,
        "title": "Grupo de sujetos a rostro cubierto roba casa en Peñalolén: Sustrajeron dinero en efectivo y un automóvil",
        "date": "May 31, 2023 @ 20:00:00.000",
        "text": "Un violento asalto se registró durante la noche de este miércoles, luego que un grupo de desconocidos ingresó a rostro cubierto a un domicilio en la comuna de Peñalolén. Los antisociales sustrajeron diversas especies durante este robo con violencia, donde lograron dinero en efectivo y se llevaron un automóvil durante el ilícito. Ir a la siguiente nota El capitán Matías Reiser, el oficial de ronda de la Prefectura Santiago Oriente, contó que fueron cuatro los antisociales que irrumpieron en el hogar e intimidaron a una de las víctimas.  \"Cuatro sujetos a rostro cubierto intimidaron con un arma de fuego y golpearon con esta al dueño de casa para sustraer diferentes especies, dinero en efectivo y un vehículo que, posteriormente, usaron para su huida\", detalló el funcionario policial. Asimismo, agregó que el jefe de hogar sólo resultó con lesiones leves. Los antecedentes fueron puestos a disposición del Ministerio Público para dar con el paradero de los delincuentes. Todo sobre Región Metropolitana",
        "category": "ciencia",
        "url": "https://www.meganoticias.cl/nacional/415730-sujetos-rostro-cubierto-roba-casa-penalolen-dinero-efectivo-automovil-01-06-2023.html"
    }
    ])

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido en prueba de documento: {elapsed_time} segundos")

    assert elapsed_time < 15