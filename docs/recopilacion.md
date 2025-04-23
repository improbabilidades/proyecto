# Recopilación de datos

El análisis de datos comienza con la *recopilación* de datos. Podríamos separar la recopilación en dos grandes paradigmas:

- **Procesamiento por lotes** (*batch processing*): consiste en la recolección de una gran cantidad de datos históricos, típicamente una sola vez, o con una frecuencia tan baja que cada recopilación tiene una gran cantidad de datos. Ejemplos: los "famosos" datos de pasajeros del Titanic, los cuales necesariamente fueron recolectados una sola vez, o la información que utiliza YouTube o Netflix para entrenar sus sistemas de recomendaciones que, aunque son actualizados aproximadamente cada 24 horas, contienen millones de nuevas interacciones.
- **Procesamiento en tiempo real** (*real-time processing*): consiste en la recolección de datos al momento de su ocurrencia, esto es, basado en eventos (*event-driven*) o con una frecuencia de recopilación tan alta que solamente algunos pocos nuevos datos, o ninguno, son obtenidos en cada muestreo. Ejemplos: datos sobre terremotos, valores diarios de los mercados de valores o mediciones de redes de sensores recopiladas cada 10 segundos.

En medio de ambos hay una "zona gris" a menudo llamada **procesamiento en tiempo casi real** (*quasi real-time processing*) que captura la dinámica del sistema sin responder directamente a eventos o a una altísima frecuencia. Ejemplos: telemetría y rastreo en vehículos de transporte público, que actualizan datos cada 15 o 20 segundos, lo suficiente para tener una buena estimación de su posición, pero no totalmente "en tiempo real".

La definición varía según el fenómeno analizado, que puede tener cambios muy frecuentes o no.

!!! note "Definición informal de procesamiento en tiempo real" 
    Un flujo de datos en el cual el procesamiento de una nueva muestra inicia en el momento de su llegada y concluye antes de la llegada de la siguiente muestra o evento es un procesamiento en tiempo real.

### ¿Y de dónde vienen estos datos?

Los datos pueden venir de un solo archivo (ejemplo, un `.xlsx` o `.csv`), directamente de un sensor (ejemplo, un Arduino con un sensor de temperatura conectado a la computadora), o de una base de datos externa, siguiendo varios *modelos de comunicación* posibles, explicados a continuación.

#### Modelos de comunicación

Algunos de los modelos de comunicación para compartir datos entre sistemas son:

- **Solicitud/respuesta**: donde una *solicitud* del *cliente* interactúa con los *recursos* de un *servidor* que devuelve una *respuesta*. Ejemplo: HTTP (el famoso "404 Not Found") o las interfaces de programación de aplicaciones web (API, *Application Programming Interface*) que operan sobre HTTP y conectan distintos servicios. 
- **Publicación/suscripción**: donde un *productor* (*producer*) *publica* un *mensaje* que coloca en un *canal* sobre un *tópico* y un *intermediador de mensajes* (*message broker*) lo distribuye a todos los procesos que están *suscritos*. Ejemplo: el monitoreo de eventos en la agricultura de precisión con una red de sensores conectada con [MQTT](https://mqtt.org/). 
- **WebSockets**: donde hay un canal de comunicación *bidireccional* con comunicación *persistente*. Ejemplo: cualquier aplicación de chat (WhatsApp, Telegram, etc.) o videojuegos en línea. A diferencia de los WebSockets, HTTP es una conexión no persistente.
- **Otros**

Una de las soluciones más populares es obtener datos de fuentes externas, y hacerlo por medio de un API o *interfaz de programación de aplicaciones* (ver sección más adelante).

## ¿Qué haremos en el proyecto?

Para este proyecto haremos una recopilación de datos en **tiempo *casi* real** de fuentes externas con un **web API** y lo haremos de forma periódica, utilizando un administrador y planificador de tareas, para almacenarlos en una **base de datos relacional**.

A continuación hay una ampliación de estos conceptos.

### Datos desde fuentes externas con API

En el **PyX** [número 6](https://github.com/fabianabarca/python) hay una explicación más amplia sobre los web API y el uso del paquete `requests` de Python.

Hay una gran cantidad de API públicos disponibles en [Public APIs](https://publicapis.dev/) para experimentar con la recolección de datos.

### Recolección periódica de datos con un planificador de tareas

En Python es posible utilizar el paquete [Celery](https://docs.celeryq.dev/en/stable/index.html) como administrador de tareas (*task manager*) y como un planificador de tareas (*task scheduler*) que "calendariza" tareas en frecuencias especificadas, como "cada 60 segundos" o "a las 4:00 am", o según otros criterios como "el primer lunes del mes" o "al anochecer".

Por tanto, para un flujo de procesamiento de datos en tiempo real o en tiempo *casi* real podemos usar Celery para recopilar datos de forma continua y periódica. Hay más detalles a continuación.

### Administrador de tareas

**Celery Worker** administra la ejecución de tareas de forma *asincrónica* entre los "trabajadores" (*workers*) disponibles. Un "trabajador" puede ser simplemente un núcleo de la computadora local que está libre para ejecutar una tarea o puede ser un servidor remoto en una configuración más compleja, por ejemplo.

**Asincrónico** significa que las tareas no bloquean unas a otras. Por ejemplo: en un flujo **sincrónico** de tareas, una tarea es ejecutada solamente hasta que la anterior haya sido terminada. En el contexto de un administrador de tareas como Celery Worker, un flujo de tareas *asincrónico* permite que múltiples tareas sean ejecutadas sin esperar a que las tareas anteriores estén completas. Celery Worker estará a cargo de "vigilar" la cola de ejecución de las tareas y reportar sus resultados.

#### Planificador de tareas

**Celery Beat** define los momentos en que las tareas son ejecutadas, es decir, es un "calendarizador" o "planificador" (*scheduler*). Esto es útil para crear tareas en un periodo de tiempo definido como, por ejemplo, "cada 15 segundos" o "cada 12 horas" o "todos los días a las 2:00 am" o "el segundo miércoles de cada mes", e inclusive con base en eventos solares, como "al amanecer" o "al mediodía" (que varía según la ubicación en el planeta y la época del año).

#### Intermediador de mensajes

Cuando es necesaria la comunicación entre procesos en una computadora, es necesario un **intermediador de mensajes** (*message broker*) para entregar el mensaje, pues los procesos no pueden comunicarse entre sí directamente.

[Redis](https://redis.io/) es un intermediador de mensajes y base de datos tipo caché popular que permite varios modelos de comunicación, como publicación/suscripción. 

Redis tiene integración con Celery, y es necesario para el envío de la asignación de las tareas periódicas desde el planificador (Celery Beat) hasta el trabajador (Celery Worker).
