## Pasos para instalar el dirver para Selenium

1. Descarga del controlador

Dependiendo del navegador con el que quieras realizar las pruebas, necesitarás el controlador específico:

* Chrome: ChromeDriver - Descárgalo desde el sitio web oficial de ChromeDriver https://sites.google.com/chromium.org/driver/.
* Firefox: GeckoDriver - Descárgalo desde el sitio web oficial de GeckoDriver https://github.com/mozilla/geckodriver/releases.
* Safari: SafariDriver - Ya viene incluido con Safari en macOS.

2. Configuración del controlador

Una vez descargado, descomprime el archivo y colócalo en un directorio accesible (por ejemplo, /usr/local/bin en sistemas Unix) o añade su ubicación al PATH del sistema.

En Linux o macOS, puedes hacerlo así (suponiendo que el controlador se encuentra en tu carpeta de descargas)

```
# Cambia el nombre del archivo del controlador según corresponda
sudo mv ~/Downloads/chromedriver /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```

También se puede colocar descomprimido en la carpeta tests-frontend.

3. Verificación de la instalación

Para verificar que el controlador está correctamente instalado y en tu PATH, puedes ejecutar el siguiente comando en la terminal:

```
chromedriver --version  # Reemplaza "chromedriver" con el nombre del controlador que instalaste
```

Si todo está bien, debería mostrar la versión del controlador.

4. Uso del controlador con Selenium

En tu código de prueba de Selenium, inicializa el controlador usando el nombre del controlador correspondiente:

```
from selenium import webdriver

# Ruta al controlador (ejemplo para ChromeDriver)
driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Reemplaza con la ubicación correcta del controlador
```

Asegúrate de usar la ruta correcta al controlador que has instalado en tu sistema. Con esta configuración, Selenium utilizará el controlador correspondiente para controlar el navegador que elijas para realizar las pruebas automatizadas.

## Pasos para configurar el ambiente virtual

1. Crear un nuevo ambiente virtual

```
python -m venv test_frontend
```

2. Activar el ambiente virtual

En Windows

```
test_frontend\Scripts\activate
```

En macOS y Linux

```
test_frontend/bin/activate
```

3. Instalar dependencias

```
pip install -r requirements.txt
```

4. Desactivar el ambiente virtual

```
deactivate
```

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
