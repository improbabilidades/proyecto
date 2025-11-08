# Enunciado del proyecto

## Instrucciones

### :material-cog: Configuración

Siguiendo las instrucciones de esta documentación y el archivo `README.md`, instalar y ejecutar localmente el repositorio con el problema de ejemplo.

### :material-database: Fuente de datos

En el sitio web de SIMOVI (Laboratorio de Sistemas Inteligentes de Movilidad) estará disponible un intermediador MQTT, disponible en la siguiente URL:

- `tcp://mqtt.simovi.org:1883`

Cada persona hará solicitudes en *broker* en el tópico `A01234`, es decir, su carné universitario (letra mayúscula). Los mensajes devolverán un conjunto de datos con un formato _para determinar_. Con la recopilación de estos datos inicia el proyecto.

### :material-lightbulb-on: Consejos

- Es posible crear nuevos archivos con _scripts_ para la solución de las preguntas planteadas.
- Lo anterior es recomendable también para "aislar" el trabajo en diferentes archivos cuando varias personas están trabajando en un mismo proyecto en Git, para así editar de forma paralela.

### :material-eye-check: Requisitos

La documentación de la entrega debe cumplir con los requisitos de la [siguiente página](requisitos.md).

## Parte I

![Static Badge](https://img.shields.io/badge/VALOR-10%25-blue)

1. (1%) Actualizar su perfil de GitHub con nombre, descripción e imagen.

2. (3%) ¡Repartir estrellas! Visitar GitHub con su cuenta y colocar una estrella en todos los siguientes repositorios:

    :material-github: [**simovilab/repositories/\*** :star:](https://github.com/orgs/simovilab/repositories)

    :   **Todos** los repositorios de SIMOVI.

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

    :material-github: [**improbabilidades/improbabilidades** :star:](https://github.com/improbabilidades/improbabilidades)

    :   Sitio web con la teoría del curso.

    :material-github: [**improbabilidades/proyecto** :star:](https://github.com/improbabilidades/proyecto)

    :   Este enunciado del proyecto.

    :material-github: [**tropicalizacion/ferias** :star:](https://github.com/tropicalizacion/ferias)

    :   Sitio web de promoción de las ferias del agricultor desarrollado por el TCU "Tropicalización de la tecnología".

3. (3%) ¡Seguir cuentas! Visitar GitHub con su cuenta y dar "Follow" en todas las siguientes cuentas:

    :material-github: [**improbabilidades**](https://github.com/improbabilidades)
    
    :   Cuenta de GitHub del curso, donde esta(rá) la teoría del curso.

    :material-github: [**tropicalizacion**](https://github.com/tropicalizacion)
    
    :   Cuenta de GitHub del TCU "Tropicalización de la tecnología", donde hacemos varios proyectos relacionados con transporte público, ferias del agricultor y talleres educativos, entre otras cosas.

    :material-github: [**simovilab**](https://github.com/simovilab)
    
    :   Cuenta de GitHub del nuevo Laboratorio de Sistemas Inteligentes de Movilidad, donde hacemos varios proyectos relacionados con la movilidad y el transporte público.

    :material-github: [**fabianabarca**](https://github.com/fabianabarca)
    
    :   Cuenta de GitHub del profesor Fabián.

    :material-github: [**RamirezSandi**](https://github.com/RamirezSandi)
    
    :   Cuenta de GitHub del profesor Sebastián.

4. (3%) Realizar la evaluación docente del profesor de cada grupo respectivo, en el link provisto por la universidad.

## Parte II

![Static Badge](https://img.shields.io/badge/VALOR-30%25-blue)

> El objetivo es modelar la distribución de los tiempos de retraso entre un evento y otro, recibidos secuencialmente a través de un tópico de MQTT.

En la documentación web deben presentar:

1. (8%) Modelos de la base de datos (`models.py`) y cliente de recolección de datos (`client.py`), los cuales deben ser diseñados según la estructura de los datos recibidos.

2. (10%) Recolección y almacenamiento de datos (al menos 3 horas continuas) en la base de datos.

3. (12%) Análisis exploratorio de los datos.
   
    - (4%) Gráficas descriptivas de las variables (histogramas y otros, cuando aplica).
    - (4%) Modelos de probabilidad para los datos cuando aplica y gráfica de la función de densidad sobre el histograma de los datos, junto con sus parámetros.
    - (4%) Momentos de los modelos (promedio, varianza, desviación estándar, inclinación, kurtosis).

### Ejemplo

- Un evento sucedió en el instante 2025-11-07T12:34:56.69485.
- Otro evento sucedió en el instante 2025-11-07T12:35:09.95763.
- La diferencia temporal es de aproximadamente **13.26278** segundos.
- Un nuevo evento ocurre en 2025-11-07T12:35:26.96319.
- La diferencia con respecto al último evento es de aproximadamente **17.00556** segundos.
- Después de la recolección de muchos eventos, es posible recopilar todas las diferencias temporales entre eventos consecutivos, visualizar su distribución (histograma), obtener momentos estadísticos (media, varianza, inclinación y kurtosis) y encontrar el modelo de probabilidad de mejor ajuste.