# Librerías
import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel

# Se define una nueva clase 'Rent' heredada de 'BaseModel' que contiene los campos de entrada para realizar la inferencia
# con el modelo entrenado. Se especifican los tipos que tienen que tener cada uno de los campos (columnas)
class Rent(BaseModel):
    square_feet: float
    accommodates: int
    cleaning_fee: float
    beds: float
    availability_30: int
    bedrooms: float
    availability_60: int
    availability_90: int
    availability_365: int
    security_deposit: float
    bathrooms: float
    guests_included: int
    neighbourhood: str
    neighbourhood_group_cleansed: str
    property_type: str
    room_type: str
    amenities: int
    x: float
    y: float
    z: float
    date: int

# Se declara la variable global 'model' sin ningún valor
model = None

# Decorador que convierte la función asociada en un gestor de contexto asíncrono. La función 'lifespan' del decorador usa
# como parámetro un dato de tipo 'FastAPI' (aunque no es usado en la función, si que se usa internamente en librerías). Se
# usa este tipo de decorador para cargar el modelo una vez, y que por tanto, no se haga en cada petición, ahorrando recursos
@asynccontextmanager
async def lifespan(app: FastAPI):

    # Se usa la palabra clave 'global' para modificar el valor de la variable global 'model' dentro de esta función
    global model

    # Se carga el modelo. Esta parte del código se ejecuta antes de que la aplicación empiece a procesar peticiones, durante
    # la puesta en marcha
    #model = pickle.load(open('C:/Users/valde/Desktop/Airbnb_Madrid/mlflow/mlartifacts/331952214411143549/'
                             #'54cc146b9ebc4590ab12b96f7ad53349/artifacts/model/model.pkl', 'rb'))      # local
    model = pickle.load(open('model/model.pkl', 'rb'))                                                  # Dockerfile

    # Umbral entre la ejecución antes/después de procesar peticiones
    yield

    # Se descarga el modelo. Esta parte del código se ejecuta después de que la aplicación termine de procesar peticiones,
    # justo antes de apagarse, liberando así recursos como memoria o GPU
    model.clear()

# Título, descripción y versión de la API, además de pasar en el parámetro 'lifespan' el gestor de contexto asíncrono
# definido arriba
app = FastAPI(title="Predicción de alquileres Airbnb en la ciudad de Madrid",
              description='''Obtén la predicción del precio diario de un alquiler Airbnb en la ciudad de Madrid gracias 
              al modelo de árbol de decisión entrenado con scikit-learn. Visita esta URL en el puerto 8501 para ejecutar
              la interfaz de Streamlit.''',
              version="0.1.0", lifespan=lifespan)

# Decorador 'GET' en la ruta '/'. La función asociada simplemente da la bienvenida a la API
@app.get("/", tags=["welcome"])
def welcome():
    return {
        "Mensaje": "Bienvenido a la API de FastAPI para calcular los precios de los alquileres"
    }

# Decorador 'POST' en la ruta '/predict'. La función asociada toma un parámetro 'rent_info' de tipo 'Rent'
@app.post("/predict", tags=["predictions"])
def get_prediction(rent_info: Rent):

    # Se crea un 'dataframe' de entrada estableciendo las columnas de entrada del modelo y como datos, los del cuerpo JSON
    # de la solicitud 'POST'
    input = pd.DataFrame(
        columns=["square_feet", "accommodates", "cleaning_fee", 'beds', 'availability_30', 'bedrooms',
                 'availability_60', 'availability_90', 'availability_365', 'security_deposit', 'bathrooms',
                 'guests_included', 'neighbourhood', 'neighbourhood_group_cleansed', 'property_type', 'room_type',
                 'amenities', 'X', 'Y', 'Z', 'date'],
        data=[[rent_info.square_feet, rent_info.accommodates, rent_info.cleaning_fee, rent_info.beds,
               rent_info.availability_30, rent_info.bedrooms, rent_info.availability_60, rent_info.availability_90,
               rent_info.availability_365, rent_info.security_deposit, rent_info.bathrooms, rent_info.guests_included,
               rent_info.neighbourhood, rent_info.neighbourhood_group_cleansed, rent_info.property_type, rent_info.room_type,
               rent_info.amenities, rent_info.x, rent_info.y, rent_info.z, rent_info.date]]
    )

    # Se realiza la predicción con los datos de entrada y el modelo cargado
    prediction = model.predict(input)

    # Se devuelve el precio diario pronosticado del alquiler
    return {
        "precio_pronosticado": str(round(float(prediction[0]), 2)) + "$"
    }

# Se ejecuta el servidor web con Uvicorn en el puerto 8000 si el programa de la APP se ejecuta como programa principal
if __name__ == "__main__":
    uvicorn.run(app, port=8000)