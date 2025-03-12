# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el código fuente de la aplicación
COPY . .

# Instala las dependencias directamente
RUN pip install --no-cache-dir Django

# Expón el puerto que utilizará tu aplicación Django
EXPOSE 80

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
