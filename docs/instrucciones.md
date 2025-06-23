# Enunciado del proyecto

## Instrucciones

### :material-cog: Configuración

Siguiendo las instrucciones de esta documentación y el archivo `README.md`, instalar y ejecutar localmente el repositorio con el problema de ejemplo. También, habilitar el control de versiones con Git y GitHub en los repositorios de [MPSS-EIE](https://github.com/mpss-eie).

### :material-database: Fuente de datos

En el sitio web [Kalouk](https://kalouk.xyz/) estará disponible un API, disponible en el siguiente _endpoint_:

- [https://kalouk.xyz/api/datos](https://kalouk.xyz/api/datos)

Cada grupo hará solicitudes en este _endpoint_ con el parámetro `grupo`. Si un grupo es, por ejemplo, el 000, entonces la solicitud de datos es:

```http
GET https://kalouk.xyz/api/datos?grupo=000
```

Esto devolverá un conjunto de datos con un formato _por determinar_. Con la recopilación de estos datos inicia el proyecto.

### :material-lightbulb-on: Consejos

- Es posible crear nuevos archivos con _scripts_ para la solución de las preguntas planteadas. Por ejemplo: `pdf.py` para determinar una función de densidad de probabilidad, `wss.py` para la estacionaridad en sentido amplio, etc.
- Lo anterior es recomendable también para "aislar" el trabajo en diferentes archivos cuando varias personas están trabajando en un mismo proyecto en Git, para así editar de forma paralela.

### :material-eye-check: Requisitos

La documentación de ambas entregas debe cumplir con los requisitos de la [siguiente página](requisitos.md).

## Parte I

![Static Badge](https://img.shields.io/badge/VALOR-10%25-blue)

En la documentación web deben presentar:

1. (2%) Modelos de la base de datos (`models.py`) y tareas de recolección de datos (`tasks.py`)
2. (2%) Recolección preliminar de datos (al menos 12 horas continuas) en la base de datos
3. Análisis exploratorio de los datos
   - (2%) Gráficas descriptivas de las variables (histogramas y otros, cuando aplica)
   - (2%) Modelos de probabilidad para los datos cuando aplica y gráfica de la función de densidad sobre el histograma de los datos
   - (2%) Momentos de los modelos (promedio, varianza, desviación estándar, inclinación, kurtosis)

## Parte II

![Static Badge](https://img.shields.io/badge/VALOR-20%25-blue)

Los datos recopilados representan una secuencia aleatoria, por cuanto son una sucesión de variables muestreadas en instantes discretos de tiempo, indexados por una marca temporal. En este sentido, es necesario hacer un análisis de _procesos aleatorios_ a los datos recopilados.

Cada grupo hará solicitudes en el siguiente _endpoint_. Si un grupo es, por ejemplo, el 000, entonces la solicitud de datos es:

```http
GET https://web.kalouk.xyz/api/proceso?grupo=000
```

Esto devolverá un conjunto de datos con un formato _por determinar_.

Las asignaciones son:

1. (2%) ¡Repartir más estrellas! Visitar GitHub con su cuenta y colocar una estrella en todos los siguientes repositorios:

    :material-github: [**kalouk-web** :star:](https://github.com/fabianabarca/kalouk-web)

    :   Servidor web de Kalouk, donde se encuentran los datos, la API, los WebSockets y otros servicios.

    :material-github: [**kalouk-js** :star:](https://github.com/fabianabarca/kalouk-js)

    :   Componentes web para interactividad con contenidos de matemáticas y programación.

    :material-github: [**kalouk-mcp** :star:](https://github.com/fabianabarca/kalouk-mcp)

    :   Servidor de contexto para agentes de inteligencia artificial con el protocolo de contexto de modelos (MCP)

    :material-github: [**kalouk-cli** :star:](https://github.com/fabianabarca/kalouk-cli)

    :   Interfaz de línea de comandos de Kalouk, donde se pueden hacer solicitudes a la API y otras cosas vía terminal.

    :material-github: [**kalouk-xyz** :star:](https://github.com/fabianabarca/kalouk-xyz)

    :   Sitio web con presentaciones del curso usando Kalouk y Slidev.

    :material-github: [**improbabilidades/web** :star:](https://github.com/improbabilidades/web)

    :   Sitio web con la teoría del curso usando Kalouk y Nuxt.

    :material-github: [**improbabilidades/proyecto** :star:](https://github.com/improbabilidades/proyecto)

    :   Este enunciado del proyecto.

    :material-github: [**tropicalizacion/ferias** :star:](https://github.com/tropicalizacion/ferias)

    :   Sitio web de promoción de las ferias del agricultor desarrollado por el TCU "Tropicalización de la tecnología".

2. (2%) ¡Seguir cuentas! Visitar GitHub con su cuenta y dar "Follow" en todas las siguientes cuentas:

    :material-github: [**improbabilidades**](https://github.com/improbabilidades)
    
    :   Cuenta de GitHub del curso, donde esta(rá) la teoría del curso (¡a partir de las transcripciones de las presentaciones que ustedes hicieron!).

    :material-github: [**tropicalizacion**](https://github.com/tropicalizacion)
    
    :   Cuenta de GitHub del TCU "Tropicalización de la tecnología", donde hacemos varios proyectos relacionados con transporte público, ferias del agricultor y talleres educativos, entre otras cosas.

    :material-github: [**simovilab**](https://github.com/simovilab)
    
    :   Cuenta de GitHub del nuevo Laboratorio de Sistemas Inteligentes de Movilidad, donde hacemos varios proyectos relacionados con la movilidad y el transporte público.

    :material-github: [**fabianabarca**](https://github.com/fabianabarca)
    
    :   Cuenta de GitHub del profesor Fabián.

    :material-github: [**RamirezSandi**](https://github.com/RamirezSandi)
    
    :   Cuenta de GitHub del profesor Sebastián.

1. (2%) Realizar la evaluación docente del profesor de cada grupo respectivo, en el link provisto por la universidad. Como evidencia, presentar una captura de pantalla del mensaje al finalizar la evaluación.
1. (2%) Participar de la sesión sincrónica/asincrónica del tema de Cadenas de Markov (instrucciones precisas serán enviadas por chat y correo electrónico). 
1. (12%) En el servidor web de Kalouk hay un proceso aleatorio que representa un sistema M/M/1, que es una "máquina" de colas con una sola línea de espera y un único servidor. El archivo `sse-client.py` es un cliente de _Server-Sent Events_ (SSE) que se conecta a este proceso aleatorio y recibe eventos de cambio de estado del sistema. El cliente imprime en la terminal los eventos recibidos. Es necesario modificar este archivo para conseguir los siguientes objetivos:
    - (3%) Durante al menos una hora, registrar los eventos de cambio de estado de un proceso aleatorio.
    - (4%) Determinar experimentalmente el valor numérico de los parámetros $\Omega_i$, $p_i$ y $q_i$ de la cadena de Markov, para cada estado $i$.
    - (3%) Determinar experimentalmente el vector de probabilidad de estado estable del sistema y sus valores numéricos.
    - (2%) Analizar los resultados obtenidos.


Nota: la determinación de los valores numéricos puede ser hecha después de la recolección de datos, en cuyo caso es necesario utilizar una base de datos para almacenar los eventos y hacer las consultas necesarias.

Nota: el servidor SSE está en la dirección [https://web.kalouk.xyz/sse/](https://web.kalouk.xyz/sse/).
