# Airbnb Madrid

En este repositorio se realiza un análisis exploratorio de datos (`EDA`) de la situación de los alquileres en la ciudad de Madrid. Se investiga la situación general del mercado en la ciudad y se analizan los precios de las publicaciones publicadas en la web. 

Posteriormente, se construyen varios modelos de `machine learning` para intentar predecir el precio diario de un alquiler en la ciudad, registrando los parámetros, las métricas y los modelos con `MLflow`.

Por último, se crea una imagen de `Docker` donde se sirve uno de los modelos entrenados en una aplicación web de `Streamlit` y se despliega dicha imagen mediante un despliegue y un servicio en un `cluster` local de `Kubernetes` con `Minikube`.


## Estructura

- **app**: Conjunto de archivos utilizados para la realización de la aplicación de `Streamlit` con el modelo de `scikit-learn` guardado con `MLflow` en formato `pickle`.


- **data**: Conjunto de archivos utilizados para la realización del análisis exploratorio y la construcción del modelo.


- **deployment**: Carpeta donde se almacena el `.YAML` para la creación del despliegue y servicio de `Kubernetes`, así como un tutorial sobre como realizar la contenerización de la aplicación web en una imagen de `Docker` y el posterior despliegue en producción de dicha imagen en un `cluster` de `Kubernetes`.


- **img**: Carpeta donde se recopilan un par de imágenes del proyecto.


- **mlflow**: Directorio donde se recopilan las carpetas por usar `MLflow`: 
	- **mrlruns**: Directorio donde se recopilan los parámetros y métricas de cada ejecución realizada en el experimento `MLflow` del proyecto. 
	- **mlartifacts**: Carpeta donde se recopilan todos los `artifacts` generados en las distintas ejecuciones de `MLflow`, es decir, los modelos, sus metadatos, las librerías requeridas para la ejecución de los mismos, etc.


- **Informe.pdf**: Informe del análisis exploratorio, de las métricas del modelo y de la propuesta de despliegue/productivización (no actualizado).


- **train.ipynb**: `Notebook` realizado en Python con el código del análisis exploratorio de datos y de los modelos entrenados para la predicción de los precios diarios, además de los registros de los modelos con `MLflow`.