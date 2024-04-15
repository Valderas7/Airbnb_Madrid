# Airbnb Madrid

En este repositorio se realiza un análisis exploratorio de datos (`EDA`) de la situación de los alquileres en la ciudad de Madrid. Se investiga la situación general del mercado en la ciudad y se analizan los precios de las publicaciones publicadas en la web. 

Posteriormente, se intenta construir un modelo de `machine learning` para intentar predecir lo mejor posible el precio diario de un alquiler en la ciudad:


## Estructura

- **dataset_nuevo**: Conjunto de archivos utilizados para la realización del análisis exploratorio y la construcción del modelo.


- **mlflow**: Directorio donde se recopilan las carpetas por usar `MLflow`: 
	- **mrlruns**: Directorio donde se recopilan los parámetros y métricas de cada ejecución realizada en el experimento `MLflow` del proyecto. 
	- **mlartifacts**: Carpeta donde se recopilan todos los `artifacts` generados en las distintas ejecuciones de `MLflow`, es decir, los modelos, sus metadatos, las librerías requeridas para la ejecución de los mismos, etc.


- **Airbnb.ipynb**: `Notebook` realizado en Python con el código del análisis exploratorio de datos y de los modelos entrenados para la predicción de los precios diarios.


- **Informe_Airbnb_Madrid.pdf**: Informe del análisis exploratorio, de las métricas del modelo y de la propuesta de despliegue/productivización.