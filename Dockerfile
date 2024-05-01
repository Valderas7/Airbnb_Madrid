# Imagen base
FROM python:3.9-slim

# Directorio dentro de la imagen en el que se está trabajando
WORKDIR /app

# Se copia el contenido de la carpeta 'app' local (código y 'requirements.txt') al directorio 'app' de la imagen
COPY app /app

# Se copia el modelo (.pkl) del árbol de decisión de MLflow al directorio 'app/model' de la imagen
COPY mlflow/mlartifacts/331952214411143549/54cc146b9ebc4590ab12b96f7ad53349/artifacts/model/model.pkl /app/model/model.pkl

# Se actualiza la imagen y se instalan las librerías del 'requirements.txt'
RUN apt-get update && pip install -r requirements.txt

# Se expone el puerto 8501 ya que será en éste donde se servirá la aplicación
EXPOSE 8501

# Comprobación de funcionamiento en el localhost de la imagen en el puerto 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Se ejecuta la APP de streamlit con el código copiado en la imagen especificando la IP (127.0.0.1) y el puerto (8501)
# donde se servirá
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]