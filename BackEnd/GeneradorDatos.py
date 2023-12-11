import random

def generar_string(indice):
    texto_lorem = 'Lorem ipsum dolor sit amet'
    fecha = '2023-{:02d}-{:02d}'.format(random.randint(1, 12), random.randint(1, 28))
    categoria = random.choice(['CIENCIA', 'ENTRETENIMIENTO', 'INTERNACIONAL', 'TECNOLOGIA', 'POLITICA'])
    url = 'http://www.otroejemplo.com'
    numero1 = round(random.uniform(-56.5, -17.5), 6)
    numero2 = round(random.uniform(-75.0, -66.75), 6)

    return f'({indice}, \'{texto_lorem}\', \'{texto_lorem}\', \'{fecha}\', \'{categoria}\', \'{url}\', 2, \'{texto_lorem}\', \'{texto_lorem}\', \'{numero1}\', \'{numero2}\')'

def generar_archivo(n):
    with open('salida.txt', 'w') as archivo:
        lineas = [generar_string(i) for i in range(1, n + 1)]
        archivo.write(', '.join(lineas))
        print(', '.join(lineas))

# Cambia el valor de n según la cantidad de veces que quieras repetir el patrón
n = 5000
generar_archivo(n)
