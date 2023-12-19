# LyricsAnalyzer - AI Topics
## Datos del estudiante 📝
* **Nombre:** Marcos Andrés Simon Ágreda
* **Código:** 56728
* **Carrera:** Ingeniería de Sistemas Computacionales
* **Curso:** Tópicos Selectos en Inteligencia Artificial

## Descripción del proyecto 📋

El proyecto consiste en la implementación de una API, cuyos endpoints, de forma general, brindan acceso a cuatro modelos, tres de procesamiento de lenguaje natural, y uno de visión por computadora, necesarios para realizar un análisis de sentimiento, emoció, significado y significado de portada de una canción, a partir de su letra.

- **distilbert-base-uncased-finetuned-sst-2-english:** Modelo que permite realizar la tarea de Sentiment Analysis, la cual consiste en identificar el sentimiento de una oración, en este caso: Negativo o Positivo; y el porcentaje para cada uno. En este caso, el modelo es utilizado para identificar el sentimiento de las secciones de la letra de una canción.
- **SamLowe/roberta-base-go_emotions:** Modelo que permite realizar la tarea de Emotion Analysis, la cual consiste en identificar las 10 emociones más probables de una oración, de un total de 21 posibles. En este caso, se utiliza el modelo para obtener las 3 emociones más probables de las secciones de la letra de una canción.
- **Nvidia NeVa - 22B:**: Modelo de visión por computadora, que permite realizar la tarea de Image Captioning, la cual consiste en generar una descripción textual de una imagen. En este caso, se utiliza el modelo para obtener la descripción de la portada de la canción.
- **GPT 3.5-Turbo-1106**: Modelo de lenguaje, que permite realizar la tarea de Text Generation, la cual consiste en generar texto a partir de un texto de entrada. En este caso, se utiliza el modelo para generar, tanto una descripción del significado de la letra de la canción por secciones, utilizando solo su letra; y hacer lo mismo, pero basándose en las salidas de los modelos anteriores.

La API está desarrollada en Python, haciendo uso de la librería FastAPI, y cada uno de los modelos, están basados en las siguientes librerías:

- **distilbert-base-uncased-finetuned-sst-2-english:** Librería PyTorch y transformers.
- **SamLowe/roberta-base-go_emotions:** Librería PyTorch y transformers (modelo creado por Sam Lowe).
- **GPT 3.5-Turbo-1106:** Librería OpenAI y LangChain.
- **Nvidia NeVa - 22B:** Llamado a la API de NGC.

Como un extra, se ha desarrollado una aplicación web, que hace uso de la API, para brindar una interfaz gráfica al usuario, y así poder hacer uso de la API de forma más amigable, la cual se encuentra en la carpeta `frontend`. Dicho frontend solamente hace uso de los endpoints `/sentiment_url`, `/emotion_url`, `/cover-description`,`/meaning_url`, `/analysis_url` y `/profile`

## Descripción de la API 🚀

La API cuenta con los siguientes endpoints:

* `/status`: Endpoint que devuelve el estado de la API, en caso de que esté activa, devuelve un mensaje de éxito, además de datos extra, como el nombre de la API, la versión y los nombres de los modelos.
* `/sentiment`: Endpoint que recibe el nombre de la canción, el artista y la letra de la canción, y devuelve la predicción numérica del sentimiento de la letra de la canción, y la etiqueta de sentimiento asignada. En este caso, que tan negattiva y positiva es la letra de la canción, junto a sus puntajes, los cuales suman a 1. Se usa el modelo distilbert-base-uncased-finetuned-sst-2-english.
* `/emotion`: Endpoint que recibe el nombre de la canción, el artista y la letra de la canción, y devuelve la predicción numérica de las tres emociones más significativas de la letra de la canción, y la etiqueta de emociones asignadas. En este caso, las tres emociones más significativas, suman sus puntajes a 1. Se usa el modelo SamLowe/roberta-base-go_emotions.
* `/meaning`: Endpoint que recibe el nombre de la canción, el artista y la letra de la canción, y devuelve la descripción del significado de la las secciones de la letra de la canción, y la descripción de la canción en general. En este caso, se hace uso del modelo GPT 3.5-Turbo-1106, para generar la descripción del significado de la letra de la canción.
* `/cover-description`: Endpoint que recibe la portada de la canción, y devuelve la descripción de la portada de la canción. En este caso, se hace uso del modelo Nvidia NeVa - 22B, para generar la descripción de la portada de la canción.
* `/sentiment_url`: Endpoint que recibe la URL de la letra de la canción del sitio web Genius, y devuelve la predicción numérica del sentimiento de la letra de la canción, y la etiqueta de sentimiento asignada. En este caso, que tan negattiva y positiva es la letra de la canción, junto a sus puntajes, los cuales suman a 1. Se usa el modelo distilbert-base-uncased-finetuned-sst-2-english.
* `/emotion_url`: Endpoint que recibe la URL de la letra de la canción del sitio web Genius, y devuelve la predicción numérica de las tres emociones más significativas de la letra de la canción, y la etiqueta de emociones asignadas. En este caso, las tres emociones más significativas, suman sus puntajes a 1. Se usa el modelo SamLowe/roberta-base-go_emotions.
* `/meaning_url`: Endpoint que recibe la URL de la letra de la canción del sitio web Genius, y devuelve la descripción del significado de la las secciones de la letra de la canción, y la descripción de la canción en general. En este caso, se hace uso del modelo GPT 3.5-Turbo-1106, para generar la descripción del significado de la letra de la canción.
* `/analysis`: Endpoint que recibe el nombre de la canción, el artista y la letra de la canción, y devuelve la descripción del significado de la las secciones de la letra de la canción, y la descripción de la canción en general, tomando en cuenta los resultados de los modelos de Sentiment Analysis, Emotion Analysis y Text Generation. En este caso, se hace uso del modelo GPT 3.5-Turbo-1106, para generar la descripción del significado de la letra de la canción; además de los modelos distilbert-base-uncased-finetuned-sst-2-english y SamLowe/roberta-base-go_emotions, para obtener los resultados de Sentiment Analysis y Emotion Analysis, respectivamente, junto con el modelo de Nvidia NeVa - 22B, para obtener la descripción de la portada de la canción.
* `/analysis_url`: Endpoint que recibe la URL de la letra de la canción del sitio web Genius, y devuelve la descripción del significado de la las secciones de la letra de la canción, y la descripción de la canción en general, tomando en cuenta los resultados de los modelos de Sentiment Analysis, Emotion Analysis y Text Generation. En este caso, se hace uso del modelo GPT 3.5-Turbo-1106, para generar la descripción del significado de la letra de la canción; además de los modelos distilbert-base-uncased-finetuned-sst-2-english y SamLowe/roberta-base-go_emotions, para obtener los resultados de Sentiment Analysis y Emotion Analysis, respectivamente, junto con el modelo de Nvidia NeVa - 22B, para obtener la descripción de la portada de la canción. 
* `/profile`: Endpoint, que genera un perfil de usuario, basado en los resultados de los endpoints anteriores (excepto /cover-description), y devuelve los resultados de: Cuantas canciones fueron analizadas, el sentimiento general de todas las canciones, y las tres emociones más significativas de todas las canciones. 

## Proceso de instalación y ejecución 🛠️

Antes de poder ejecutar la API, se debe crear un archivo `.env` en la ruta raiz del proyecto, y agregar las siguientes variables de entorno:

```
NVIDIA_KEY=<API_KEY>
OPENAI_KEY=<API_KEY>
```

Para poder ejecutar la API, se debe tener instalado Docker. Posteriormente, se debe abrir una terminal en la raiz del proyecto, y ejecutar el siguiente comando:

```
docker-compose up
```

Este comando, creará un contenedor de Docker, sin antes crear la imagen Docker, basada en el archivo `Dockerfile`, el cual descargará todas las dependencias necesarias para ejecutar la API, y posteriormente, ejecutará la API en el puerto 8000.

### Instalación y ejecución sin Docker 🐳

ATECIÓN: Este proceso de instalación y ejecución, no es recomendado, ya que se debe instalar cada una de las dependencias de forma manual, y además, se deben descargar los modelos de forma manual, lo cual puede tomar mucho tiempo.

El modelo de distilbert-base-uncased-finetuned-sst-2-english, se debe descargar de la siguiente dirección:
```
git clone https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
```

OJO, se debe tener habilitado el LFS de Git, para poder clonar el modelo.

Y la carpeta clonada, es decir `distilbert-base-uncased-finetuned-sst-2-english`, se debe mover a la carpeta `models`, que se encuentra en la carpeta src del proyecto.

El modelo de SamLowe/roberta-base-go_emotions, se debe descargar de la siguiente dirección:
```
git clone https://huggingface.co/SamLowe/roberta-base-go_emotions
```

Y la carpeta clonada, es decir `roberta-base-go_emotions`, se debe mover a la carpeta `models`, que se encuentra en la carpeta src del proyecto.


Después, se debe tener Python 3.10 o superior instalado, y posteriormente instalar las dependencias del proyecto:

```
fastapi
uvicorn
pydantic
pydantic-settings
python-multipart
python-dotenv
numpy
openai
langchain
transformers
Pillow
beautifulsoup4
sqlmodel
```

Además, de forma separada, se debe ejecutar el siguiente comando:

```
pip3 install torch==2.1.1+cpu torchvision==0.16.1+cpu torchaudio==2.1.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
```
Finalmente, para ejecutar la API, se debe abrir una terminal en la raiz del proyecto, y ejecutar el siguiente comando:

```
uvicorn src.app:app --host 0.0.0.0 --reload
```

## Extra: Aplicación web 📦

Para poder ejecutar la aplicación web, se debe tener instalado Node.js 18 o superior. Posteriormente, se debe abrir la carpeta `frontend` en una terminal, y ejecutar el siguiente comando:

```
npm install
```

Posteriormente, crear un archivo `.env` en la carpeta `frontend`, y agregar la siguiente variable de entorno:

```
VITE_API_URL='http://localhost:8000'
``` 
O, también se puede usar el link de la API en Google Cloud Platform (adjuntado en el correo)

Finalmente, ejecutar el siguiente comando:

```
npm run dev
```

El frontend, se ejecutará en el puerto 5173, por lo que se puede acceder a la aplicación web.

