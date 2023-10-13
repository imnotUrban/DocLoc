#pip install pytest
#UTILIZAR COMANDO: pytest test_document.py
from gpt.GPTQueryEngine import GPTQueryEngine
from google.geocoding import Geocoding
from fastapi.testclient import TestClient
from datetime import datetime
from main import app

client = TestClient(app)

def testCreateDocuments():
    # Caso de prueba 1: Enviar un documento válido
    response = client.post("/geolocalize", json=[
      {
        "id": 0,
        "title": "Pronóstico de lluvia para el fin de semana: Revisa las zonas en las que se esperan precipitaciones",
        "text": "De acuerdo al reporte de la Dirección Meteorológica de Chile, se espera que distintas zonas del país se vean afectadas por precipitaciones durante este fin de semana, incluyendo el viernes 2 de junio. Es específico, se trataría de 11 regiones en total en las que se presentaría el fenómeno, incluyendo a la zona insular de la región de Valparaíso. Ir a la siguiente nota Según el organismo, en la zona insular de la región de Valparaíso, en Isla de Pascua, se espera lluvia en la noche del sábado y toda la jornada del domingo. También se esperan precipitaciones para este viernes en la zona continental de la región de Valparaíso, donde se harían presente durante la mañana y la tarde. El mismo día, en la región Metropolitana, el fenómeno se presentaría en la tarde y en la noche, mientras que en O'Higgins comenzaría en la mañana y terminaría en la noche. Para la región de Maule se pronostica lluvia desde la madrugada hasta la tarde de este 2 de junio, al igual que en Ñuble, donde también caerían chubascos desde la tarde del sábado hasta la madrugada del domingo. En tanto, En Biobío el pronóstico apunta en la madrugada y mañana del viernes, y desde la mañana hasta el resto de la jornada del sábado. Las precipitaciones se harían presente en La Araucanía en la madrugada, tarde y noche del 2 de junio, y desde la madrugada hasta la tarde del día siguiente. Para Los Ríos se espera que el fenómeno se haga presente todo el viernes y el sábado, al igual que en Los Lagos, donde también se extendería en la noche del domingo. Se espera que en la región de Aysén caiga agua-nieve en la madrugada del 2 de junio, mientras que la lluvia se presentaría en la tarde y en la noche. Al día siguiente se registrarían nevadas hasta la mañana y chubascos el resto de la jornada. Finalmente, el domingo, las precipitaciones ocurrirían en la tarde y en la noche. En la región de Magallanes, en Torres del Paine, caerían chubascos desde la madrugada hasta la tarde del viernes. El 3 de junio habría chubascos de agua-nieve en la mañana y en la tarde, y chubascos de niev en la noche; mientras que el domingo la lluvia se registraría en la tarde y en la noche. En tanto, Punta Arenas presentaría precipitaciones en la madrugada, mañana y noche del viernes, además de la noche del domingo. Todo sobre El Tiempo",
        "date": "May 31, 2023 @ 20:00:00.000",
        "url": "https://www.meganoticias.cl/nacional/415732-lluvia-fin-de-semana-santiago-regiones-pronostico-del-tiempo-25-05-2023.html"
      }
    ])
    assert response.status_code == 200

    responseJSON = response.json()
    print(responseJSON)
    print(type(responseJSON))

    # Se tienen las claves requeridas
    assert all({'date', 'location', 'lat', 'lng'}.issubset(item.keys()) for item in responseJSON), "No todos los elementos tienen las claves requeridas"
    # Los valores lat y lng son validos
    assert all(isinstance(float(item['lat']), float) and isinstance(float(item['lng']), float) for item in responseJSON), "Al menos una coordenada no es un número válido"
    # No hay lugares duplicados
    assert len(responseJSON) == len(set((item['location']) for item in responseJSON)), "Hay elementos duplicados en la lista"


    # Datos de referencia con un margen de error de 10
    reference_data = [
        {'date': '2023-10-13 12:55:06.136412', 'location': 'zona insular de la región de Valparaíso, Isla de Pascua', 'lat': '-27.112723', 'lng': '-109.3496865'}, 
        {'date': '2023-10-13 12:55:06.136805', 'location': 'zona continental de la región de Valparaíso', 'lat': '-32.5040172', 'lng': '-71.0022311'}, 
        {'date': '2023-10-13 12:55:06.137143', 'location': 'región Metropolitana', 'lat': '-33.4843354', 'lng': '-70.6216794'}, 
        {'date': '2023-10-13 12:55:06.137485', 'location': "O'Higgins", 'lat': '0.0', 'lng': '0.0'}, 
        {'date': '2023-10-13 12:55:06.137817', 'location': 'región de Maule', 'lat': '-35.5163603', 'lng': '-71.5723953'}, 
        {'date': '2023-10-13 12:55:06.138187', 'location': 'Ñuble', 'lat': '-36.7225743', 'lng': '-71.7622481'}, 
        {'date': '2023-10-13 12:55:06.138538', 'location': 'Biobío', 'lat': '-37.4464428', 'lng': '-72.1416132'}, 
        {'date': '2023-10-13 12:55:06.138881', 'location': 'La Araucanía', 'lat': '-38.948921', 'lng': '-72.331113'}, 
        {'date': '2023-10-13 12:55:06.139189', 'location': 'Los Ríos', 'lat': '-1.0230607', 'lng': '-79.4608897'}, 
        {'date': '2023-10-13 12:55:06.139508', 'location': 'Los Lagos', 'lat': '-41.9197779', 'lng': '-72.1416132'}, 
        {'date': '2023-10-13 12:55:06.139805', 'location': 'región de Aysén', 'lat': '-46.378345', 'lng': '-72.3007623'}, 
        {'date': '2023-10-13 12:55:06.140146', 'location': 'región de Magallanes, Torres del Paine', 'lat': '-51.25325729999999', 'lng': '-72.35167659999999'}, 
        {'date': '2023-10-13 12:55:06.140501', 'location': 'Punta Arenas', 'lat': '-53.1633845', 'lng': '-70.9078263'}
    ]

    # Asegurarse de que haya la misma cantidad de elementos en la respuesta y los datos de referencia
    assert len(responseJSON) == len(reference_data), "La cantidad de elementos no coincide"

    # Comparar los datos con un margen de error de 10 para las coordenadas
    for i, reference_item in enumerate(reference_data):
        response_item = responseJSON[i]
        
        # Compara las coordenadas con un margen de error de 10
        lat_reference = float(reference_item['lat'])
        lng_reference = float(reference_item['lng'])
        lat_response = float(response_item['lat'])
        lng_response = float(response_item['lng'])

        assert abs(lat_reference - lat_response) <= 10, f"La latitud no coincide para el elemento {i}"
        assert abs(lng_reference - lng_response) <= 10, f"La longitud no coincide para el elemento {i}"

def testCreateVoidDocuments():
    # Caso de prueba 2: Enviar un documento vacio invalido
    response = client.post("/geolocalize", json=[])
    assert response.status_code == 406
  
def testCreateManyDocuments():
    # Caso de prueba 3: Enviar muchos documentos (envio invalido)
    response = client.post("/geolocalize", json=[
      {
        "id": 0,
        "title": "Pronóstico de lluvia para el fin de semana: Revisa las zonas en las que se esperan precipitaciones",
        "text": "De acuerdo al reporte de la Dirección Meteorológica de Chile, se espera que distintas zonas del país se vean afectadas por precipitaciones durante este fin de semana, incluyendo el viernes 2 de junio. Es específico, se trataría de 11 regiones en total en las que se presentaría el fenómeno, incluyendo a la zona insular de la región de Valparaíso. Ir a la siguiente nota Según el organismo, en la zona insular de la región de Valparaíso, en Isla de Pascua, se espera lluvia en la noche del sábado y toda la jornada del domingo. También se esperan precipitaciones para este viernes en la zona continental de la región de Valparaíso, donde se harían presente durante la mañana y la tarde. El mismo día, en la región Metropolitana, el fenómeno se presentaría en la tarde y en la noche, mientras que en O'Higgins comenzaría en la mañana y terminaría en la noche. Para la región de Maule se pronostica lluvia desde la madrugada hasta la tarde de este 2 de junio, al igual que en Ñuble, donde también caerían chubascos desde la tarde del sábado hasta la madrugada del domingo. En tanto, En Biobío el pronóstico apunta en la madrugada y mañana del viernes, y desde la mañana hasta el resto de la jornada del sábado. Las precipitaciones se harían presente en La Araucanía en la madrugada, tarde y noche del 2 de junio, y desde la madrugada hasta la tarde del día siguiente. Para Los Ríos se espera que el fenómeno se haga presente todo el viernes y el sábado, al igual que en Los Lagos, donde también se extendería en la noche del domingo. Se espera que en la región de Aysén caiga agua-nieve en la madrugada del 2 de junio, mientras que la lluvia se presentaría en la tarde y en la noche. Al día siguiente se registrarían nevadas hasta la mañana y chubascos el resto de la jornada. Finalmente, el domingo, las precipitaciones ocurrirían en la tarde y en la noche. En la región de Magallanes, en Torres del Paine, caerían chubascos desde la madrugada hasta la tarde del viernes. El 3 de junio habría chubascos de agua-nieve en la mañana y en la tarde, y chubascos de niev en la noche; mientras que el domingo la lluvia se registraría en la tarde y en la noche. En tanto, Punta Arenas presentaría precipitaciones en la madrugada, mañana y noche del viernes, además de la noche del domingo. Todo sobre El Tiempo",
        "date": "May 31, 2023 @ 20:00:00.000",
        "url": "https://www.meganoticias.cl/nacional/415732-lluvia-fin-de-semana-santiago-regiones-pronostico-del-tiempo-25-05-2023.html"
      },
      {
        "id": 1,
        "title": "Alerta meteorológica: Pronóstico de lluvia para el fin de semana en Chile",
        "text": "Según el informe emitido por el Servicio Meteorológico Nacional de Chile, se anticipa la llegada de condiciones climáticas adversas durante el próximo fin de semana. Se prevé que diversas regiones del país se vean afectadas por precipitaciones, incluyendo el sábado 10 de junio. Con detalles específicos, se espera que un total de 13 regiones experimenten este fenómeno, abarcando desde el norte hasta el sur del país.\n\nDe acuerdo con el pronóstico, en la región de Antofagasta se esperan lluvias intensas desde la madrugada del sábado hasta la tarde, lo que podría generar problemas en áreas propensas a inundaciones. En la región de Atacama, las precipitaciones se pronostican para la tarde y noche del sábado.\n\nEn la región de Coquimbo, las lluvias llegarían en la tarde del sábado y se extenderían hasta la mañana del domingo. Mientras tanto, en la región de Valparaíso, se esperan chubascos durante la noche del sábado y la madrugada del domingo, afectando tanto a la zona continental como a la insular, incluyendo Isla de Pascua.\n\nPara la región Metropolitana, se pronostica lluvia en la tarde del sábado y en la mañana del domingo. En O'Higgins, las precipitaciones comenzarían en la madrugada del sábado y continuarían hasta la tarde.\n\nEn Maule, se espera lluvia desde la madrugada hasta la tarde del 10 de junio, y en Ñuble, los chubascos caerían desde la tarde del sábado hasta la madrugada del domingo.\n\nEn Biobío, el pronóstico apunta a lluvia en la madrugada y la mañana del sábado, extendiéndose hasta el resto del día. La Araucanía experimentaría precipitaciones en la madrugada, tarde y noche del 10 de junio, y continuarían hasta la tarde del día siguiente.\n\nEn la región de Los Ríos, se espera que las precipitaciones estén presentes durante todo el sábado y domingo, al igual que en Los Lagos, donde también se extenderían hasta la noche del domingo.\n\nSe anticipa que en la región de Aysén, caiga aguanieve en la madrugada del 10 de junio, seguido de lluvia por la tarde y noche. Al día siguiente, se registrarían nevadas hasta la mañana y chubascos durante el resto del día. Finalmente, el domingo, las precipitaciones ocurrirían en la tarde y noche.\n\nEn la región de Magallanes, en Torres del Paine, se prevén chubascos desde la madrugada hasta la tarde del viernes 9 de junio. El 10 de junio habría chubascos de aguanieve en la mañana y la tarde, seguidos de chubascos de nieve en la noche; mientras que el domingo la lluvia se registraría en la tarde y noche.\n\nPor último, Punta Arenas presentaría precipitaciones en la madrugada, mañana y noche del viernes 9 de junio, además de la noche del domingo 11 de junio.\n\nMantente informado sobre las condiciones climáticas y toma las precauciones necesarias para enfrentar esta situación meteorológica.",
        "date": "Jun 5, 2023 @ 18:30:00.000",
        "url": "https://www.ejemplonoticias.cl/nacional/123456-alerta-meteorologica-lluvia-fin-de-semana-chile-pronostico-10-06-2023.html"
      }
    ])
    assert response.status_code == 406

def testCreateImaginaryDocument():
    # Caso de prueba 4: Enviar un documento que no deberia existir
    response = client.post("/geolocalize", json=[
      {
        "id": 3,
        "title": "Noticias de Azeroth: Preparativos para la Batalla en Shadowlands",
        "text": "En el mundo de World of Warcraft, la tensión aumenta a medida que los héroes de Azeroth se preparan para una nueva batalla épica en las Tierras Sombrías. La expansión Shadowlands ha traído consigo un giro en la narrativa y desafíos emocionantes para los aventureros de la Horda y la Alianza por igual.\n\nLos jugadores han estado explorando los reinos misteriosos de las Tierras Sombrías, donde se encuentran con las cuatro Covenants: los Kyrianos, Necroseñores, Venthyr y los Nocheterna. Cada Covenant ofrece poderes únicos y habilidades especiales que los jugadores pueden desbloquear y personalizar para adaptarse a su estilo de juego.\n\nLa Torre de Torghast, la Torre de los Condenados, se ha convertido en un lugar crucial para la obtención de legendarios y mejoras poderosas. Los jugadores se enfrentan a desafíos generados aleatoriamente en esta mazmorra infinita, donde la dificultad aumenta a medida que avanzan. ¡Es el lugar perfecto para demostrar su valía!\n\nAdemás, la amenaza del Carcelero y su plan maestro en las Tierras Sombrías sigue siendo una preocupación constante para los héroes. La trama se desarrolla mientras los jugadores descubren más sobre los oscuros secretos de este antagonista.\n\nCon el lanzamiento de la primera gran actualización de Shadowlands, los jugadores pueden esperar nuevas zonas, mazmorras y desafíos para mantenerlos entretenidos durante meses.\n\n¿Estás listo para unirte a la lucha en las Tierras Sombrías? Prepárate para forjar alianzas, descubrir secretos y enfrentarte a poderosos enemigos en el emocionante mundo de World of Warcraft.",
        "date": "Oct 15, 2023 @ 14:45:00.000",
        "url": "https://www.wowhead.com/es/azeroth/shadowlands-preparativos-batalla-15-10-2023.html"
      }
    ])
    assert response.status_code == 200

    responseJSON = response.json()
    print(responseJSON)
    print(type(responseJSON))

    # Se tienen las claves requeridas
    assert all({'date', 'location', 'lat', 'lng'}.issubset(item.keys()) for item in responseJSON), "No todos los elementos tienen las claves requeridas"
    # Los valores lat y lng son validos
    assert all(item['lat'] == ' ' and item['lng'] == ' ' for item in responseJSON), "Al menos una coordenada no es un espacio en blanco"
    # No hay lugares duplicados
    assert len(responseJSON) == len(set((item['location']) for item in responseJSON)), "Hay elementos duplicados en la lista"

def testQueryGPT():
    # Caso de prueba 5: Funcionamiento de API GPT
    queryEngine = GPTQueryEngine()

    doc = {
      "id": 0,
      "title": "Pronóstico de lluvia para el fin de semana: Revisa las zonas en las que se esperan precipitaciones",
      "text": "De acuerdo al reporte de la Dirección Meteorológica de Chile, se espera que distintas zonas del país se vean afectadas por precipitaciones durante este fin de semana, incluyendo el viernes 2 de junio. Es específico, se trataría de 11 regiones en total en las que se presentaría el fenómeno, incluyendo a la zona insular de la región de Valparaíso. Ir a la siguiente nota Según el organismo, en la zona insular de la región de Valparaíso, en Isla de Pascua, se espera lluvia en la noche del sábado y toda la jornada del domingo. También se esperan precipitaciones para este viernes en la zona continental de la región de Valparaíso, donde se harían presente durante la mañana y la tarde. El mismo día, en la región Metropolitana, el fenómeno se presentaría en la tarde y en la noche, mientras que en O'Higgins comenzaría en la mañana y terminaría en la noche. Para la región de Maule se pronostica lluvia desde la madrugada hasta la tarde de este 2 de junio, al igual que en Ñuble, donde también caerían chubascos desde la tarde del sábado hasta la madrugada del domingo. En tanto, En Biobío el pronóstico apunta en la madrugada y mañana del viernes, y desde la mañana hasta el resto de la jornada del sábado. Las precipitaciones se harían presente en La Araucanía en la madrugada, tarde y noche del 2 de junio, y desde la madrugada hasta la tarde del día siguiente. Para Los Ríos se espera que el fenómeno se haga presente todo el viernes y el sábado, al igual que en Los Lagos, donde también se extendería en la noche del domingo. Se espera que en la región de Aysén caiga agua-nieve en la madrugada del 2 de junio, mientras que la lluvia se presentaría en la tarde y en la noche. Al día siguiente se registrarían nevadas hasta la mañana y chubascos el resto de la jornada. Finalmente, el domingo, las precipitaciones ocurrirían en la tarde y en la noche. En la región de Magallanes, en Torres del Paine, caerían chubascos desde la madrugada hasta la tarde del viernes. El 3 de junio habría chubascos de agua-nieve en la mañana y en la tarde, y chubascos de niev en la noche; mientras que el domingo la lluvia se registraría en la tarde y en la noche. En tanto, Punta Arenas presentaría precipitaciones en la madrugada, mañana y noche del viernes, además de la noche del domingo. Todo sobre El Tiempo",
      "date": "May 31, 2023 @ 20:00:00.000",
      "url": "https://www.meganoticias.cl/nacional/415732-lluvia-fin-de-semana-santiago-regiones-pronostico-del-tiempo-25-05-2023.html"
    }

    PTResult = queryEngine.query(doc["text"])
    print(type(PTResult))
    print(PTResult)

    # PTResult es dictionary?
    assert isinstance(PTResult, dict)
    # PTResult tiene data de GPT?
    assert "data" in PTResult

    for item in PTResult["data"]:
        # GPT entrego lugares?
        assert "location" in item 
        # GPT entrego resumenes?
        assert "summary" in item

def testGeoGoogle():
    # Caso de prueba 6: Enviar a procesar a google el resultado de GPT
    geoloc = Geocoding()

    GPTData = [
        {'location': 'zona insular de la región de Valparaíso, Isla de Pascua', 'summary': 'Se espera lluvia en la noche del sábado y toda la jornada del domingo.'},
        {'location': 'zona continental de la región de Valparaíso', 'summary': 'Se esperan precipitaciones para este viernes durante la mañana y la tarde.'},
        {'location': 'región Metropolitana', 'summary': 'El fenómeno se presentaría en la tarde y en la noche del viernes.'},
        {'location': "O'Higgins", 'summary': 'El fenómeno comenzaría en la mañana y terminaría en la noche del viernes.'},
        {'location': 'región de Maule', 'summary': 'Se pronostica lluvia desde la madrugada hasta la tarde de este 2 de junio.'},
        {'location': 'Ñuble', 'summary': 'Caerían chubascos desde la tarde del sábado hasta la madrugada del domingo.'},
        {'location': 'Biobío', 'summary': 'El pronóstico apunta a precipitaciones en la madrugada y mañana del viernes, y desde la mañana hasta el resto de la jornada del sábado.'},
        {'location': 'La Araucanía', 'summary': 'Las precipitaciones se harían presente en la madrugada, tarde y noche del 2 de junio, y desde la madrugada hasta la tarde del día siguiente.'},
        {'location': 'Los Ríos', 'summary': 'Se espera que el fenómeno se haga presente todo el viernes y el sábado.'},
        {'location': 'Los Lagos', 'summary': 'Se espera que el fenómeno se haga presente todo el viernes y el sábado, y también se extendería en la noche del domingo.'},
        {'location': 'región de Aysén', 'summary': 'Se espera que caiga agua-nieve en la madrugada del 2 de junio, y luego se registrarían nevadas hasta la mañana y chubascos el resto de la jornada del domingo.'},
        {'location': 'región de Magallanes, Torres del Paine', 'summary': 'Caerían chubascos desde la madrugada hasta la tarde del viernes. El 3 de junio habría chubascos de agua-nieve en la mañana y en la tarde, y chubascos de nieve en la noche; mientras que el domingo la lluvia se registraría en la tarde y en la noche.'},
        {'location': 'Punta Arenas', 'summary': 'Presentaría precipitaciones en la madrugada, mañana y noche del viernes, además de la noche del domingo.'}
    ]
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
