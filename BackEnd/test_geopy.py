#pip install pytest
#UTILIZAR COMANDO: pytest test_document.py
from routes.document import document
from gpt.GPTQueryEngine import GPTQueryEngine
from google.geocoding import Geocoding
from fastapi.testclient import TestClient
from datetime import datetime
from main import app

client = TestClient(app)

def testGeo():
    # Caso de prueba 6: Enviar a procesar a google el resultado de GPT
    geoloc = Geocoding()

    GPTData = {'location': 'zona insular de la región de Valparaíso, Isla de Pascua', 'summary': 'Se espera lluvia en la noche del sábado y toda la jornada del domingo.'}
    
    geoResult = geoloc.getCoordinates(GPTData)
    print(geoResult)
    
    # Lo devuelto por google es una lista?
    assert isinstance(geoResult, list)
    # Cada item entregado por google
    for item in geoResult:
        # Es de tipo dict?
        assert isinstance(item, dict)
        # Tiene date?
        assert 'date' in item
        # Proporciona lugar?
        assert 'location' in item
        # Proporciona lat y lng?
        assert 'lat' in item
        assert 'lng' in item
    
    # Los lugares entregados no son vacios?
    for item in geoResult:
      assert 'location' in item
      assert isinstance(item['location'], str)
      assert len(item['location']) > 0, "Lugar vacio"

    
    # Las fechas proporcionadas son validas?
    for item in geoResult:
        assert 'date' in item
        try:
            datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            assert False, f"Formato de fecha invalido: {item['date']}"



#{
#        "id": 4,
#        "title": "Grupo de sujetos a rostro cubierto roba casa en Peñalolén: Sustrajeron dinero en efectivo y un automóvil",
#        "date": "May 31, 2023 @ 20:00:00.000",
#        "category": "delincuencia",
#        "text": "Un violento asalto se registró durante la noche de este miércoles, luego que un grupo de desconocidos ingresó a rostro cubierto a un domicilio en la comuna de Peñalolén. Los antisociales sustrajeron diversas especies durante este robo con violencia, donde lograron dinero en efectivo y se llevaron un automóvil durante el ilícito. Ir a la siguiente nota El capitán Matías Reiser, el oficial de ronda de la Prefectura Santiago Oriente, contó que fueron cuatro los antisociales que irrumpieron en el hogar e intimidaron a una de las víctimas.  \"Cuatro sujetos a rostro cubierto intimidaron con un arma de fuego y golpearon con esta al dueño de casa para sustraer diferentes especies, dinero en efectivo y un vehículo que, posteriormente, usaron para su huida\", detalló el funcionario policial. Asimismo, agregó que el jefe de hogar sólo resultó con lesiones leves. Los antecedentes fueron puestos a disposición del Ministerio Público para dar con el paradero de los delincuentes. Todo sobre Región Metropolitana",
#        "url": "https://www.meganoticias.cl/nacional/415730-sujetos-rostro-cubierto-roba-casa-penalolen-dinero-efectivo-automovil-01-06-2023.html"
#    }