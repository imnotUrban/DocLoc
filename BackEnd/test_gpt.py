from gpt.GPTQueryEngine import GPTQueryEngine
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)
# El test debería ser capaz de cumplir con que, al ingresar la noticia, se obtenga la ubicación de la noticia con la clase geocoding, y contenga el nombre de la ubicación

news_test = [{
    "title": "Grupo de sujetos a rostro cubierto roba casa en Peñalolén: Sustrajeron dinero en efectivo y un automóvil",
    "text": "Un violento asalto se registró durante la noche de este miércoles, luego que un grupo de desconocidos ingresó a rostro cubierto a un domicilio en la comuna de Peñalolén. Los antisociales sustrajeron diversas especies durante este robo con violencia, donde lograron dinero en efectivo y se llevaron un automóvil durante el ilícito. Ir a la siguiente nota El capitán Matías Reiser, el oficial de ronda de la Prefectura Santiago Oriente, contó que fueron cuatro los antisociales que irrumpieron en el hogar e intimidaron a una de las víctimas.  \"Cuatro sujetos a rostro cubierto intimidaron con un arma de fuego y golpearon con esta al dueño de casa para sustraer diferentes especies, dinero en efectivo y un vehículo que, posteriormente, usaron para su huida\", detalló el funcionario policial. Asimismo, agregó que el jefe de hogar sólo resultó con lesiones leves. Los antecedentes fueron puestos a disposición del Ministerio Público para dar con el paradero de los delincuentes. Todo sobre Región Metropolitana",
    "date": "Mar 31, 2022 @ 21:00:00.000",
    "category": "ciencia",
    "url": "https://www.meganoticias.cl/nacional/415730-sujetos-rostro-cubierto-roba-casa-penalolen-dinero-efectivo-automovil-01-06-2023.html"
},
             
{
      "id": 0,
      "title": "Pronóstico de lluvia para el fin de semana: Revisa las zonas en las que se esperan precipitaciones",
      "text": "De acuerdo al reporte de la Dirección Meteorológica de Chile, se espera que distintas zonas del país se vean afectadas por precipitaciones durante este fin de semana, incluyendo el viernes 2 de junio. Es específico, se trataría de 11 regiones en total en las que se presentaría el fenómeno, incluyendo a la zona insular de la región de Valparaíso. Ir a la siguiente nota Según el organismo, en la zona insular de la región de Valparaíso, en Isla de Pascua, se espera lluvia en la noche del sábado y toda la jornada del domingo. También se esperan precipitaciones para este viernes en la zona continental de la región de Valparaíso, donde se harían presente durante la mañana y la tarde. El mismo día, en la región Metropolitana, el fenómeno se presentaría en la tarde y en la noche, mientras que en O'Higgins comenzaría en la mañana y terminaría en la noche. Para la región de Maule se pronostica lluvia desde la madrugada hasta la tarde de este 2 de junio, al igual que en Ñuble, donde también caerían chubascos desde la tarde del sábado hasta la madrugada del domingo. En tanto, En Biobío el pronóstico apunta en la madrugada y mañana del viernes, y desde la mañana hasta el resto de la jornada del sábado. Las precipitaciones se harían presente en La Araucanía en la madrugada, tarde y noche del 2 de junio, y desde la madrugada hasta la tarde del día siguiente. Para Los Ríos se espera que el fenómeno se haga presente todo el viernes y el sábado, al igual que en Los Lagos, donde también se extendería en la noche del domingo. Se espera que en la región de Aysén caiga agua-nieve en la madrugada del 2 de junio, mientras que la lluvia se presentaría en la tarde y en la noche. Al día siguiente se registrarían nevadas hasta la mañana y chubascos el resto de la jornada. Finalmente, el domingo, las precipitaciones ocurrirían en la tarde y en la noche. En la región de Magallanes, en Torres del Paine, caerían chubascos desde la madrugada hasta la tarde del viernes. El 3 de junio habría chubascos de agua-nieve en la mañana y en la tarde, y chubascos de niev en la noche; mientras que el domingo la lluvia se registraría en la tarde y en la noche. En tanto, Punta Arenas presentaría precipitaciones en la madrugada, mañana y noche del viernes, además de la noche del domingo. Todo sobre El Tiempo",
      "date": "May 31, 2023 @ 20:00:00.000",
      "category": "entretenimiento",
      "url": "https://www.meganoticias.cl/nacional/415732-lluvia-fin-de-semana-santiago-regiones-pronostico-del-tiempo-25-05-2023.html"
    }
]

location = ["Peñalolén, Región Metropolitana, Chile", "Dirección Meteorológica de Chile"]

@pytest.mark.parametrize(
  "news_test, location_expected",
  [
    (news_test[0],location[0]),
    (news_test[1],location[1])
   ]  
)

def test_gptQueryEngine(news_test, location_expected):
    query_engine = GPTQueryEngine()
    GPTResult = query_engine.query(news_test["text"])
    assert GPTResult["data"]["location"] == location_expected
