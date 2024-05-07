# Airbnb Madrid

En este repositorio se realiza un análisis exploratorio de datos (`EDA`) de la situación de los alquileres en la ciudad de Madrid. Se investiga la situación general del mercado en la ciudad y se analizan los precios de las publicaciones publicadas en la web. 

Posteriormente, se construyen varios modelos de `machine learning` para intentar predecir el precio diario de un alquiler en la ciudad, registrando los parámetros, las métricas y los modelos con `MLflow`.

A partir de aquí se siguen dos estrategias de despliegue:
- En una de ellas se crea una imagen de `Docker` donde se sirve uno de los modelos entrenados en una aplicación web embebida de `Streamlit` y se despliega dicha imagen mediante un despliegue y un servicio en un `cluster` local de `Kubernetes` con `Minikube`.


- En otra de ellas se crea como `backend` una `API` con `FastAPI` donde se sirve el modelo y como `frontend` una aplicación web con `Streamlit` que realiza peticiones `POST` a la `API`, obteniendo el resultado de los precios pronosticados de vuelta. Se crea una imagen de `Docker` tanto para el `backend` como el `frontend` y se despliegan ambas imágenes mediante contenedores en un despliegue de `Kubernetes`, con un contenedor de cada una de las imágenes en un mismo `pod`, y exponiendo tanto la `API` como la aplicación web a través de un servicio de Kubernetes que tiene dos puertos expuestos (uno para cada contenedor).


## Estructura

- **app**: Directorio donde se recopilan los archivos para crear la `API` y/o la aplicación web.
    - **embedded**: Conjunto de archivos utilizados para la realización de la aplicación embebida de `Streamlit` con el modelo de `scikit-learn` guardado con `MLflow`.
    - **fullstack**: Recopilación de archivos usados para la construcción de la parte `backend`y `frontend` para desplegar el modelo con `FastAPI` y `Streamlit` conjuntamente.


- **data**: Conjunto de archivos utilizados para la realización del análisis exploratorio y la construcción del modelo.


- **deployment**: Carpeta donde se almacenan los archivos `.YAML` para la creación del despliegue y servicio de `Kubernetes`, tanto de forma embebida como de forma conjunta con los servicios de `frontend` y `backend`, así como un tutorial sobre como realizar la contenerización de la aplicación web en una imagen de `Docker` y el posterior despliegue en producción en un `cluster` de `Kubernetes`.


- **img**: Carpeta donde se recopilan un par de imágenes de demostración del proyecto.


- **mlflow**: Directorio donde se recopilan las carpetas por usar `MLflow`: 
	- **mlruns**: Directorio donde se recopilan los parámetros y métricas de cada ejecución realizada en el experimento `MLflow` del proyecto. 
	- **mlartifacts**: Carpeta donde se recopilan todos los `artifacts` generados en las distintas ejecuciones de `MLflow`, es decir, los modelos, sus metadatos, las librerías requeridas para la ejecución de los mismos, etc.


- **Informe.pdf**: Informe del análisis exploratorio, de las métricas del modelo y de la propuesta de despliegue.


- **train.ipynb**: `Notebook` realizado en Python con el código del análisis exploratorio de datos y de los modelos entrenados para la predicción de los precios diarios, además de los registros de los modelos con `MLflow`.