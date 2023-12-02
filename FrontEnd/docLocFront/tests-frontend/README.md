## Pasos para instalar el dirver para Selenium

1. Descarga del controlador

Dependiendo del navegador con el que quieras realizar las pruebas, necesitarás el controlador específico:

* Chrome: ChromeDriver - Descárgalo desde el sitio web oficial de [ChromeDriver](https://sites.google.com/chromium.org/driver/).
* Firefox: GeckoDriver - Descárgalo desde el sitio web oficial de [GeckoDriver](https://github.com/mozilla/geckodriver/releases).
* Safari: SafariDriver - Ya viene incluido con Safari en macOS.

2. Configuración del controlador

Una vez descargado, descomprime el archivo y colócalo dentro de la carpeta tests-frontend

## Pasos para configurar el ambiente virtual

1. Crea un ambiente virtual

```
python -m venv test_frontend
```

2. Activa el ambiente virtual

En Windows

```
test_frontend\Scripts\activate
```

En macOS y Linux

```
test_frontend/bin/activate
```

3. Instala las dependencias

```
pip install -r requirements.txt
```

4. Desactivar el ambiente virtual (para cuando termines las pruebas)

```
deactivate
```
## Ejecutar pruebas

Puedes ejecutar todas las pruebas usando el comando

```
pytest
```

También puedes ejecutar un conjunto de pruebas usando marcadores (usar marcadores evita que la prueba que verifica la url funcione).

Los siguientes marcadores están disponibles:

```
pytest -m select
```
Prueba que el filtro de las noticias de acuerdo a las categorias funciona.

```
pytest -m data
```
Prueba que el filtro de las noticias de acuerdo a un intervalo de fechas funciona.

```
pytest -m navigation
```
Prueba que los botones de navegación de atrás y adelante funcionan.

## Documentación para Selenium

https://www.selenium.dev/documentation/

## Uso de @pytest.mark.parametrize

`@pytest.mark.parametrize` se usa para ejecutar una prueba con diferentes conjuntos de datos o escenarios. Permite ejecutar la misma prueba con diferentes entradas, lo que hace que el código de prueba sea más conciso y fácil de mantener.

## Uso de @pytest.mark

`@pytest.mark` (Marcadores personalizados): Los marcadores te permiten etiquetar tus pruebas para organizarlas, filtrarlas o ejecutarlas selectivamente. Puedes crear marcadores personalizados para identificar diferentes categorías de pruebas (como pruebas lentas, pruebas de integración, etc.). Para ejecutarlos se usa:

```
pytest -m <nombre>
```

El nombre es lo que va después de @pytest.mark, por ejemplo para @pytest.mark.n el nombre es n.
