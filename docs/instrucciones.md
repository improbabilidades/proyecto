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

**Valor: 5%**

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

**Valor: 15%**

En formato por definir, cada equipo presenta:

1. Documentación completa (5%)
    - Todo lo del avance, mejorado si es el caso
    - Especificación de la pregunta de investigación
2. Respuesta a la pregunta de investigación (5%)
    - Modelado de los datos obtenidos
    - Resultados estadísticos (correlaciones, etc.)
3. Análisis y conclusiones (5%)
