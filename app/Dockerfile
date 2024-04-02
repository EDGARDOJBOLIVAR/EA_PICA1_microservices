# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Instalar las dependencias del sistema operativo necesarias
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el contenido del directorio actual al contenedor en /app
COPY . /app

# Instalar cualquier dependencia necesaria especificada en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Establecer el directorio de trabajo en la carpeta src
WORKDIR /app/src

EXPOSE 9000

# Ejecutar app.py cuando se inicie el contenedor
CMD ["python", "app.py"]
