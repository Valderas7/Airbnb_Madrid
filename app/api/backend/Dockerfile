# Imagen base
FROM python:3.9-slim

# Directorio dentro de la imagen en el que se está trabajando
WORKDIR /app

# Se copia el contenido de la carpeta 'backend' local (código y 'requirements.txt') al directorio 'app' de la imagen
COPY app/api/backend ./

# Se copia el modelo (.pkl) del árbol de decisión de MLflow al directorio 'app/model' de la imagen
COPY mlflow/mlartifacts/331952214411143549/54cc146b9ebc4590ab12b96f7ad53349/artifacts/model/model.pkl ./model/model.pkl

# Se actualiza la imagen y se instalan las librerías del 'requirements.txt'
RUN apt-get update && pip install -r requirements.txt

# Se expone el puerto 8000 ya que será en éste donde se servirá la aplicación
EXPOSE 8000

# Comprobación de funcionamiento en el localhost de la imagen en el puerto 8000
HEALTHCHECK CMD curl --fail http://localhost:8000/_stcore/health

# Se ejecuta la APP de FastAPI con el código copiado en la imagen especificando la IP (127.0.0.1) y el puerto (8000)
# donde se servirá. Hay que especificar el nombre del código de Python (server) y el nombre de la variable FastAPI utilizada
# en el código (app)
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]