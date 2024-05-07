# Imagen base
FROM python:3.9-slim

# Directorio dentro de la imagen en el que se está trabajando
WORKDIR /app

# Se copia el contenido de la carpeta 'frontend' local (código y 'requirements.txt') al directorio 'app' de la imagen
COPY app/fullstack/frontend/requirements.txt app/fullstack/frontend/app.py ./

# Se actualiza la imagen y se instalan las librerías del 'requirements.txt'
RUN apt-get update && pip install -r requirements.txt

# Se expone el puerto 8501 ya que será en éste donde se servirá la aplicación
EXPOSE 8501

# Comprobación de funcionamiento en el localhost de la imagen en el puerto 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Se ejecuta la APP de streamlit con el código copiado en la imagen especificando la IP (127.0.0.1) y el puerto (8501)
# donde se servirá
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]