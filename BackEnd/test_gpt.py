from gpt.GPTQueryEngine import GPTQueryEngine
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)
# El test debería ser capaz de cumplir con que, al ingresar la noticia, se obtenga la ubicación de la noticia con la clase geocoding, y contenga el nombre de la ubicación, luego 
news_test = [{
    "title": "Grupo de sujetos a rostro cubierto roba casa en Peñalolén: Sustrajeron dinero en efectivo y un automóvil",
    "text": "Un violento asalto se registró durante la noche de este miércoles, luego que un grupo de desconocidos ingresó a rostro cubierto a un domicilio en la comuna de Peñalolén. Los antisociales sustrajeron diversas especies durante este robo con violencia, donde lograron dinero en efectivo y se llevaron un automóvil durante el ilícito. Ir a la siguiente nota El capitán Matías Reiser, el oficial de ronda de la Prefectura Santiago Oriente, contó que fueron cuatro los antisociales que irrumpieron en el hogar e intimidaron a una de las víctimas.  \"Cuatro sujetos a rostro cubierto intimidaron con un arma de fuego y golpearon con esta al dueño de casa para sustraer diferentes especies, dinero en efectivo y un vehículo que, posteriormente, usaron para su huida\", detalló el funcionario policial. Asimismo, agregó que el jefe de hogar sólo resultó con lesiones leves. Los antecedentes fueron puestos a disposición del Ministerio Público para dar con el paradero de los delincuentes. Todo sobre Región Metropolitana",
    "date": "Mar 31, 2022 @ 21:00:00.000",
    "category": "ciencia",
    "url": "https://www.meganoticias.cl/nacional/415730-sujetos-rostro-cubierto-roba-casa-penalolen-dinero-efectivo-automovil-01-06-2023.html"
}]

location = "Peñalolén, Región Metropolitana, Chile"

@pytest.mark.parametrize(
    "news_test, location_expected",
    [
        (news_test[0],location)
    ]  
)

def test_gptQueryEngine(news_test, location_expected):
    query_engine = GPTQueryEngine()
    
    # lat_test = -33.4765918
    # lng_test = -70.5418308
    
    GPTResult = query_engine.query(news_test["text"])
    assert GPTResult["data"]["location"] == location_expected