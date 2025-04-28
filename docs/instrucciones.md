# Enunciado del proyecto

## :material-format-list-bulleted-type: Instrucciones

### Configuración

Siguiendo las instrucciones de esta documentación y el archivo `README.md` instalar y ejecutar localmente el proyecto. También, habilitar el control de versiones con Git y GitHub para todo el equipo en los repositorios de [MPSS-EIE](https://github.com/mpss-eie).

### Fuente de datos

En el sitio web [Kalouk](https://kalouk.xyz/) estará disponible un API, disponible en el siguiente *endpoint*:

- [https://kalouk.xyz/api/datos](https://kalouk.xyz/api/datos)

Cada grupo hará solicitudes en este *endpoint* con el parámetro `grupo`. Si un grupo es, por ejemplo, el 000, entonces la solicitud de datos es:

```http
GET https://kalouk.xyz/api/datos?grupo=000
```

Esto devolverá un conjunto de datos con un formato por determinar. Con la recopilación de estos datos inicia el proyecto.

### Presentación de avance

***Valor: 10%***

En la documentación web deben presentar:

1. (1%) Modelos de la base de datos (`models.py`) y tareas de recolección de datos (`tasks.py`) 
3. (1%) Recolección preliminar de datos (al menos 12 horas continuas) en la base de datos 
4. Análisis exploratorio de los datos
    - (1%) Gráficas descriptivas de `variable_1` y `variable_2` (histogramas y otros, si aplica) 
    - (1%) Modelos de probabilidad para los datos donde aplica y gráfica sobre el histograma de los datos 
    - (1%) Momentos de los modelos (promedio, varianza, desviación estándar, inclinación, kurtosis) 

**Notas**

- Todo el código debe cumplir con PEP 8 y será evaluado usando, por ejemplo, `$ flake8 tasks.py`.
- El desarrollo debe estar ampliamente comentado.
- La buena ortografía y gramática son esenciales.

### Presentación del reporte final

***Valor: 20%***

Los datos recopilados representan una secuencia aleatoria, por cuanto son una sucesión de variables muestreadas en instantes discretos de tiempo, indexados por una marca temporal. En este sentido, es necesario hacer un análisis de procesos aleatorios a los datos recopilados.

Algunos elementos por determinar son:

- Función de densidad de probabilidad
- Estacionaridad en sentido amplio
- Promedios temporales de funciones muestra
- Ergodicidad
- Funciones de correlación y covarianza
- Potencia promedio
- Densidad espectral de potencia
- Análisis de ruido

Cada grupo hará solicitudes en este *endpoint* con el parámetro `proceso`. Si un grupo es, por ejemplo, el 000, entonces la solicitud de datos es:

```http
GET https://kalouk.xyz/api/proceso?grupo=000
```

Esto devolverá un conjunto de datos con un formato por determinar. Con la recopilación de estos datos inicia el proyecto.

Las asignaciones son:

1. (1%) Nueva recopilación de datos por 24 horas (con gráficas u otros elementos probatorios)
2. (4%) Determinación de la función de densidad de probabilidad
3. (4%) Determinación de la estacionaridad en sentido amplio y ergodicidad
5. (3%) Determinación de la potencia promedio
6. (2%) Análisis de resultados y conclusiones
7. (1%) Documentación apropiada

Todo esto debe ser presentado en la documentación tal y como en el avance del proyecto, siguiendo las mismas normas de PEP 8, ortografía, etc.

**Consejos**

- Es posible crear nuevos archivos con *scripts* para la solución de las preguntas planteadas. Por ejemplo: `pdf.py` para determinar la función de densidad de probabilidad del punto 1., `wss.py` para la estacionaridad en sentido amplio, etc.
- Lo anterior es recomendable también para "aislar" el trabajo en diferentes archivos cuando varias personas están trabajando en un mismo proyecto en Git, para así editar de forma paralela.
