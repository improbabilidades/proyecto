# Enunciado del proyecto

## Instrucciones

### :material-cog: Configuración

Siguiendo las instrucciones de esta documentación y el archivo `README.md`, instalar y ejecutar localmente el repositorio con el problema de ejemplo. También, habilitar el control de versiones con Git y GitHub en los repositorios de [MPSS-EIE](https://github.com/mpss-eie).

### :material-database: Fuente de datos

En el sitio web [Kalouk](https://kalouk.xyz/) estará disponible un API, disponible en el siguiente *endpoint*:

- [https://kalouk.xyz/api/datos](https://kalouk.xyz/api/datos)

Cada grupo hará solicitudes en este *endpoint* con el parámetro `grupo`. Si un grupo es, por ejemplo, el 000, entonces la solicitud de datos es:

```http
GET https://kalouk.xyz/api/datos?grupo=000
```

Esto devolverá un conjunto de datos con un formato *por determinar*. Con la recopilación de estos datos inicia el proyecto.

### :material-lightbulb-on: Consejos

- Es posible crear nuevos archivos con *scripts* para la solución de las preguntas planteadas. Por ejemplo: `pdf.py` para determinar una función de densidad de probabilidad, `wss.py` para la estacionaridad en sentido amplio, etc.
- Lo anterior es recomendable también para "aislar" el trabajo en diferentes archivos cuando varias personas están trabajando en un mismo proyecto en Git, para así editar de forma paralela.

### :material-eye-check: Requisitos

La documentación de ambas entregas debe cumplir con los requisitos de la [siguiente página](requisitos.md).

## Avance

![Static Badge](https://img.shields.io/badge/VALOR-10%25-blue)

En la documentación web deben presentar:

1. (2%) Modelos de la base de datos (`models.py`) y tareas de recolección de datos (`tasks.py`) 
2. (2%) Recolección preliminar de datos (al menos 12 horas continuas) en la base de datos 
3. Análisis exploratorio de los datos
    - (2%) Gráficas descriptivas de las variables (histogramas y otros, cuando aplica) 
    - (2%) Modelos de probabilidad para los datos cuando aplica y gráfica de la función de densidad sobre el histograma de los datos 
    - (2%) Momentos de los modelos (promedio, varianza, desviación estándar, inclinación, kurtosis) 

## Reporte final

![Static Badge](https://img.shields.io/badge/VALOR-20%25-blue)

Los datos recopilados representan una secuencia aleatoria, por cuanto son una sucesión de variables muestreadas en instantes discretos de tiempo, indexados por una marca temporal. En este sentido, es necesario hacer un análisis de *procesos aleatorios* a los datos recopilados.

Cada grupo hará solicitudes en el siguiente *endpoint*. Si un grupo es, por ejemplo, el 000, entonces la solicitud de datos es:

```http
GET https://kalouk.xyz/api/proceso?grupo=000
```

Esto devolverá un conjunto de datos con un formato *por determinar*.

Las asignaciones son:

1. (1%) Nueva recopilación de datos por 24 horas (con gráficas u otros elementos probatorios)
2. (5%) Determinación de la función de densidad de probabilidad
3. (5%) Determinación de la estacionaridad en sentido amplio y la ergodicidad
4. (4%) Determinación de la potencia promedio
5. (3%) Análisis de resultados y conclusiones
6. (2%) Documentación apropiada
