# Librerías
import streamlit as st
import pickle
import pandas as pd

# Título de la Web App con cabecera H2
st.markdown("<h2 style='text-align: center; color: black;'> Predicción de alquileres Airbnb en la ciudad de Madrid </h2>",
            unsafe_allow_html=True)

# Decorador para cachear funciones que devuelven datos, como por ejemplo la inferencia de un modelo de machine learning
# La función 'load_model' del decorador simplemente carga el modelo de MLflow
@st.cache_data
def load_model():
    #loaded_model = pickle.load(open('C:/Users/valde/Desktop/Airbnb_Madrid/mlflow/mlartifacts/331952214411143549/'
                                    #'54cc146b9ebc4590ab12b96f7ad53349/artifacts/model/model.pkl', 'rb'))   # local
    loaded_model = pickle.load(open('model/model.pkl', 'rb'))                                               # Dockerfile
    return loaded_model

# Sliders y cajas de selección para seleccionar los valores de las variables de entrada
square_feet = st.slider("Pies cuadrados", value=5.0, min_value=0.1, max_value=5167.0, step=5.0)
accommodates = st.slider("Habitaciones", value=10, min_value=1, max_value=27, step=1)
cleaning_fee = st.slider("Tarifa de limpieza", value=20.0, min_value=0.0, max_value=550.0, step=1.0)
beds = st.slider("Camas", value=10.0, min_value=0.0, max_value=50.0, step=1.0)
availability_30 = st.slider("Disponibilidad 30 días/año", value=20, min_value=0, max_value=30, step=1)
bedrooms = st.slider("Dormitorios", value=2.0, min_value=0.0, max_value=11.0, step=1.0)
availability_60 = st.slider("Disponibilidad 60 días/año", value=20, min_value=0, max_value=60, step=1)
availability_90 = st.slider("Disponibilidad 90 días/año", value=20, min_value=0, max_value=90, step=1)
availability_365 = st.slider("Disponibilidad 365 días/año", value=20, min_value=0, max_value=365, step=1)
security_deposit = st.slider("Fianza", value=20.0, min_value=0.0, max_value=4460.0, step=5.0)
bathrooms = st.slider("Cuartos de baño", value=3.0, min_value=0.0, max_value=12.0, step=1.0)
guests_included = st.slider("Número de huéspedes incluidos", value=1, min_value=1, max_value=16, step=1)
neighbourhood = st.selectbox("Barrio", ['Acacias', 'Adelfas', 'Almagro', 'Almenara', 'Aluche', 'Arapiles', 'Arganzuela',
                                        'Argüelles', 'Atocha', 'Barajas', 'Bellas Vistas', 'Berruguete', 'Bethnal Green',
                                        'Carabanchel', 'Castellana', 'Castilla', 'Castillejos', 'Centro', 'Chamartín',
                                        'Chamberí', 'Ciudad Jardin', 'Ciudad Lineal', 'Cortes', 'Cuatro Caminos',
                                        'Delicias', 'El Tréntaiseis', 'El Viso', 'Embajadores', 'Estrella',
                                        'Fuencarral-el Pardo', 'Fuente del Berro', 'Gaztambide', 'Goya', 'Guindalera',
                                        'Hispanoamérica', 'Hortaleza', 'Ibiza', 'Imperial', 'Jerónimos', 'Justicia',
                                        'La Chopera', 'La Latina', 'Legazpi', 'Lista', 'Malasaña', 'Moncloa', 'Moratalaz',
                                        'Nueva España', 'Pacifico', 'Palacio', 'Palos do Moguer', 'Prosperidad',
                                        'Puente de Vallecas', 'Recoletos', 'Retiro', 'Rios Rosas', 'Salamanca', 'San Blas',
                                        'Sol', 'Tetuán', 'Trafalgar', 'Usera', 'Valdeacederas', 'Vallehermosa', 'Vicálvaro',
                                        'Villa de Vallecas', 'Villaverde', 'Otro'])
neighbourhood_group_cleansed = st.selectbox("Distrito", ['Arganzuela', 'Barajas', 'Carabanchel', 'Centro', 'Chamartín',
                                                         'Chamberí', 'Ciudad Lineal', 'Fuencarral - El Pardo', 'Hortaleza',
                                                         'Latina', 'Moncloa - Aravaca', 'Moratalaz', 'Puente de Vallecas',
                                                         'Retiro', 'Salamanca', 'San Blas - Canillejas', 'Tetuán', 'Usera',
                                                         'Vicálvaro', 'Villa de Vallecas', 'Villaverde'])
property_type = st.selectbox("Tipo de propiedad", ['Aparthotel', 'Apartment', 'Barn', 'Bed and breakfast', 'Boutique hotel',
                                                   'Bungalow', 'Camper/RV', 'Casa particular (Cuba)', 'Cave', 'Chalet',
                                                   'Condominium', 'Dome house', 'Earth house', 'Farm stay', 'Guest suite',
                                                   'Guesthouse', 'Hostel', 'Hotel', 'House', 'Hut', 'Igloo', 'Loft',
                                                   'Nature lodge', 'Other', 'Pension (South Korea)', 'Serviced apartment',
                                                   'Tent', 'Tiny house', 'Townhouse', 'Villa', 'Yurt'])
room_type = st.selectbox("Tipo de habitación", ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'])
amenities = st.slider("Comodidades", value=20, min_value=0, max_value=86, step=1)
x = st.slider("Coordenada X localización alquiler", value=4834420.0, min_value=4834420.0, max_value=4851910.0, step=5.0)
y = st.slider("Coordenada Y localización alquiler", value=-326518.0, min_value=-326518.0, max_value=-298892.0, step=5.0)
z = st.slider("Coordenada Z localización alquiler", value=4128069.0, min_value=4128069.0, max_value=4147577.0, step=5.0)
date = st.slider("Semana del año", value=1, min_value=1, max_value=53, step=1)

# Se crea un 'dataframe' de entrada estableciendo las columnas y como datos los botones establecidos
input = pd.DataFrame(
    data=[[square_feet, accommodates, cleaning_fee, beds, availability_30, bedrooms, availability_60, availability_90,
           availability_365, security_deposit, bathrooms, guests_included, neighbourhood, neighbourhood_group_cleansed,
           property_type, room_type, amenities, x, y, z, date]],
    columns=["square_feet", "accommodates", "cleaning_fee", 'beds', 'availability_30', 'bedrooms', 'availability_60',
             'availability_90', 'availability_365', 'security_deposit', 'bathrooms', 'guests_included', 'neighbourhood',
             'neighbourhood_group_cleansed', 'property_type', 'room_type', 'amenities', 'X', 'Y', 'Z', 'date']
)

# Se llama a la función del decorador que cachea datos
model = load_model()

# Se realiza la predicción con los datos de entrada y el modelo
prediction = model.predict(input)

# Se imprime la predicción con una cabecera H4
st.write("<h4 style='text-align: center; color: black;'> El precio pronosticado del alquiler es de " +
         str(round(float(prediction[0]), 2)) + "$" + "</h4>", unsafe_allow_html=True)