# Airbnb Madrid

En este repositorio se realiza un análisis exploratorio de datos (`EDA`) de la situación de los alquileres en la ciudad de Madrid. Se investiga la situación general del mercado en la ciudad y se analizan los precios de las publicaciones publicadas en la web. 

Posteriormente, se construyen varios modelos de `machine learning` para intentar predecir el precio diario de un alquiler en la ciudad, registrando los parámetros, las métricas y los modelos con `MLflow`.

Por último, se crea una imagen de `Docker` donde se sirve uno de los modelos entrenados en un servicio web y se despliega un servicio de inferencia con `KServe` en un cluster local de `Kubernetes` con `Minikube`.


## Estructura

- **dataset_nuevo**: Conjunto de archivos utilizados para la realización del análisis exploratorio y la construcción del modelo.


- **deployment**: Directorio donde se recopilan los archivos a usar para el despliegue:
	- **local**: Código para la inferencia cuando se sirve el modelo en una `API REST` local. 
	- **production**: Carpeta donde se recopila el `.yaml` para la creación del servicio de inferencia en `Kubernetes`, así como un archivo `.json` en formato V2 para usar como datos de entrada en el servicio de inferencia en producción de `Kubernetes`.


- **img**: Carpeta donde se recopilan un par de imágenes del proyecto.


- **mlflow**: Directorio donde se recopilan las carpetas por usar `MLflow`: 
	- **mrlruns**: Directorio donde se recopilan los parámetros y métricas de cada ejecución realizada en el experimento `MLflow` del proyecto. 
	- **mlartifacts**: Carpeta donde se recopilan todos los `artifacts` generados en las distintas ejecuciones de `MLflow`, es decir, los modelos, sus metadatos, las librerías requeridas para la ejecución de los mismos, etc.


- **Airbnb.ipynb**: `Notebook` realizado en Python con el código del análisis exploratorio de datos y de los modelos entrenados para la predicción de los precios diarios, además de los registros de los modelos con `MLflow` y la guía para servir el modelo en una API y el posterior despliegue en `Kubernetes`.


- **Informe.pdf**: Informe del análisis exploratorio, de las métricas del modelo y de la propuesta de despliegue/productivización (no actualizado).