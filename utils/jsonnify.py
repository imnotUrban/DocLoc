# Transforma la lista, en un json 
import json


def transform_to_json(data_list):
    # Lista para almacenar los objetos JSON
    json_data = []

    # Iterar sobre las tuplas y crear objetos JSON
    for item in data_list:
        json_item = {
            "title": item[1],
            "text": item[2],
            "date": item[3],
            "url": item[4],
            "state": item[5],
            "result": item[6],
            "lat": item[7],
            "long": item[8]
        }
        json_data.append(json_item)

    # Convertir la lista de objetos JSON a una cadena JSON
    json_string = json.dumps(json_data, indent=4)

    # Eliminar los saltos de línea
    json_string = json_string.replace("\n", "")

    return json_string