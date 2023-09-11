# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias especificadas en requirements.txt
RUN pip install -r requirements.txt

# Copia el código de tu aplicación al directorio de trabajo
COPY . .

# Expone el puerto que tu aplicación usará (por ejemplo, 5001 para FastAPI)
EXPOSE 5001

# Comando para ejecutar tu aplicación, ajusta según tu aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]
