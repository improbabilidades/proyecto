# Recopilación de datos

El análisis de datos comienza con la *recopilación* de datos. Podríamos separar la recopilación en dos grandes paradigmas:

- **Procesamiento por lotes** (*batch processing*): consiste en la recolección de una gran cantidad de datos históricos, típicamente una sola vez, o con una frecuencia tan baja que cada recopilación tiene una gran cantidad de datos. Ejemplos: los "famosos" datos de pasajeros del Titanic, los cuales necesariamente fueron recolectados una sola vez, o la información que utiliza YouTube o Netflix para entrenar sus sistemas de recomendaciones que, aunque son actualizados diariamente, contienen millones de nuevas interacciones en cada recopilación.
- **Procesamiento en tiempo real** (*real-time processing*): consiste en la recolección de datos al momento de su ocurrencia, esto es, basado en eventos (*event-driven*) o con una frecuencia de recopilación tan alta que solamente algunos pocos nuevos datos, o ninguno, son obtenidos en cada muestreo. Ejemplos: datos sobre terremotos, valores diarios de los mercados de valores o mediciones de redes de sensores recopiladas cada 10 segundos.

En medio de ambos hay una "zona gris", a menudo llamada **procesamiento en tiempo casi real** (*quasi real-time processing*), que captura la dinámica del sistema sin responder directamente a eventos o sin una frecuencia tan alta. Por ejemplo, la telemetría y rastreo en vehículos de transporte público actualiza datos cada 15 o 20 segundos, lo cual es suficiente para tener una buena estimación de su posición, pero no es totalmente "en tiempo real".

La definición, entonces, varía según el fenómeno analizado, que puede tener cambios muy frecuentes o no. Por ejemplo: un muestreo anual podría ser "tiempo real" en el análisis de fenómenos geológicos (lentos, por naturaleza).

!!! note "Definición informal de procesamiento en tiempo real" 
    Un flujo de datos en el cual el procesamiento de una nueva muestra inicia en el momento de su llegada y concluye antes de la llegada de la siguiente muestra o evento.

## Fuentes de datos

Los datos pueden venir de un solo archivo (ejemplo, un `.xlsx` o `.csv`), directamente de un sensor (ejemplo, un Arduino conectado a la computadora con un sensor de temperatura), o de una base de datos externa, siguiendo varios *modelos de comunicación* posibles, explicados a continuación.

### Modelos de comunicación

Algunos de los modelos de comunicación para compartir datos entre sistemas son:

- **Solicitud/respuesta**: donde una *solicitud* del *cliente* interactúa con los *recursos* de un *servidor* que devuelve una *respuesta*. Ejemplo: HTTP (el famoso "404 Not Found" es uno de los [códigos de estado de respuesta](https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status) posibles) o las interfaces de programación de aplicaciones web (web API, *Application Programming Interface*) que operan sobre HTTP y conectan distintos servicios de forma *programática*. 
- **Publicación/suscripción**: donde un *productor* (*producer*) *publica* un *mensaje* que coloca en un *canal* sobre un *tópico* y un *intermediador de mensajes* (*message broker*) lo distribuye a todos los procesos que están *suscritos*. Ejemplo: el monitoreo de eventos en la agricultura de precisión con una red de sensores conectada con [MQTT](https://mqtt.org/). 
- **WebSockets**: donde hay un canal de comunicación *bidireccional* con comunicación *persistente*. Ejemplo: en cualquier aplicación de chat (WhatsApp, Telegram, etc.) o videojuegos en línea, en las que la acción de un cliente es reflejada en los otros. Por ejemplo: cuando aparte "*Fulanito está escribiendo…*" en un chat. Por su parte, HTTP es una conexión no persistente, a diferencia de los WebSockets.
- **Otros**

Una de las soluciones más populares es obtener datos de fuentes externas, y hacerlo por medio de un API o *interfaz de programación de aplicaciones*, como está descrito a continuación.

### Datos desde fuentes externas con API

En el **PyX** número 6 ([Py6](https://github.com/fabianabarca/PyX)) hay una amplia explicación sobre los web API y el uso del paquete `requests` de Python.

Hay una gran cantidad de API públicos disponibles en [Public APIs](https://publicapis.dev/) para experimentar con la recolección de datos.

El siguiente es un ejemplo con el API de GitHub, donde está disponible la información de la cuenta de las personas registradas.

```python title="playground.ipynb"
import requests

# Usuario(a) de GitHub
usuario = "fabianabarca"

# Construir la URL
api_url = "https://api.github.com/users/" + usuario

# Hacer la solicitud GET y guardar un "Response" en la variable r
r = requests.get(api_url)

# Convertir la información obtenida en JSON
datos = r.json()

# Extraer y mostrar algún dato particular
print("Compañía:", datos["company"])

# Resultado
# Compañía: Universidad de Costa Rica
```

**Nota**: En el archivo `playground.ipynb` (Notebook de Jupyter) de este repositorio pueden experimentar con este código.

## Recopilación de datos en el proyecto

Para este proyecto haremos una recopilación de datos en **tiempo *casi* real** de fuentes externas con un **web API** y lo haremos de forma periódica, utilizando un administrador y planificador de tareas, para almacenarlos en una **base de datos relacional**.

A continuación hay una ampliación de estos conceptos.

### Recolección periódica de datos con un planificador de tareas

A menudo es necesario realizar tareas de forma periódica y automática. Esta gestión debe ser realizada con suficiente robustez para asignar correctamente *quién* va a realizar la tarea y *cuándo* la va a hacer, y cómo lidiar con posibles problemas en su ejecución. En el análisis de datos esta no es una tarea trivial y requiere de adecuada planificación. Existen plataformas completas para esto, como [Apache Airflow](https://airflow.apache.org/), pero usaremos una herramienta más básica aunque igualmente poderosa, que de hecho está en el corazón de Airflow.

En Python es posible utilizar el paquete [Celery](https://docs.celeryq.dev/en/stable/index.html) como **administrador de tareas** (*task manager*) y como **planificador de tareas** (*task scheduler*) que "calendariza" tareas en frecuencias especificadas, como "cada 60 segundos" o "a las 4:00 am", o según otros criterios como "el primer lunes del mes" o "al anochecer".

Por tanto, para un flujo de procesamiento de datos en tiempo real o en tiempo *casi* real podemos usar Celery para recopilar datos de forma programática, continua y periódica. Hay más detalles a continuación.

#### Administrador de tareas

**Celery Worker** administra la ejecución de tareas de forma *asincrónica* entre los "trabajadores" (*workers*) disponibles. Un "trabajador" puede ser simplemente un núcleo de la computadora local que está libre para ejecutar una tarea o puede ser, por ejemplo, un servidor remoto en una configuración más compleja.

*Asincrónico* significa que las tareas no bloquean unas a otras. Por ejemplo, en un flujo *sincrónico* de tareas, una tarea es ejecutada solamente después de que la anterior haya terminado. En el contexto de un administrador de tareas como Celery Worker, un flujo de tareas *asincrónico* permite que múltiples tareas sean ejecutadas en paralelo o de manera independiente, sin necesidad de esperar la finalización de otras. Celery Worker se encarga de *consumir tareas de una cola de mensajes*, ejecutarlas y reportar sus resultados.

#### Planificador de tareas

**Celery Beat** define los momentos en que las tareas son ejecutadas, es decir, es un "calendarizador" o "planificador" (*scheduler*). Esto es útil para crear tareas en una frecuencia definida como, por ejemplo, "cada 15 segundos" o "cada 12 horas" o "todos los días a las 2:00 am" o "el segundo miércoles de cada mes", e inclusive con base en eventos solares, como "al amanecer" o "al mediodía" (que varía según la ubicación en el planeta y la época del año).

#### Intermediador de mensajes

Cuando es necesaria la comunicación entre procesos en una computadora, es necesario un **intermediador de mensajes** (*message broker*) para entregar el mensaje, pues los procesos no pueden comunicarse entre sí directamente.

[Redis](https://redis.io/) es un intermediador de mensajes y base de datos tipo caché popular que permite varios modelos de comunicación, como publicación/suscripción. 

Redis tiene integración con Celery, y es necesario para el envío de la asignación de las tareas periódicas desde el planificador (Celery Beat) hasta el trabajador (Celery Worker).

Hay más detalles en la [documentación de Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html).
