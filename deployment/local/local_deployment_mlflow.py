import requests
import json
import pandas as pd
import numpy as np

# URL donde se sirve el modelo
url = 'http://127.0.0.1:1234/invocations'

# Header para contenido de tipo JSON
headers = {'Content-type': 'application/json'}

# Datos a los que realizar la inferencia. MUY IMPORTANTE: Seguir el esquema de 'dataframe_split' con 'columns' y 'data'
X_test = json.dumps({
    "dataframe_split": {
        "columns": ["square_feet", "accommodates", "cleaning_fee", "beds", "availability_30", "bedrooms", "availability_60", "availability_90", "availability_365", "security_deposit", "bathrooms", "guests_included", "neighbourhood", "neighbourhood_group_cleansed", "property_type", "room_type", "amenities", "X", "Y", "Z", "date"], 
        "data": [
            [np.nan, 6, 60.0, 4.0, 30, 2.0, 60, 88, 359, 600.0, 2.0, 4, "Retiro", "Retiro", "Apartment", "Entire home/apt", 18, 4846242.12107298, -312605.06587381434, 4134833.3663519137, 2], 
            [np.nan, 6, 60.0, 4.0, 30, 2.0, 60, 88, 359, 600.0, 2.0, 4, "Retiro", "Retiro", "Apartment", "Entire home/apt", 18, 4846242.12107298, -312605.06587381434, 4134833.3663519137, 2]
            ]
    }
})                          

# Solicitud 'POST' al puerto donde el modelo está siendo expuesto con el 'header' de contenido JSON
resp = requests.post(url, headers=headers, data = X_test)

print(resp.content)
