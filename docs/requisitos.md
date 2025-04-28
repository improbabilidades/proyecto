# Requisitos del proyecto

## Lista de revisión

Asegúrense de cumplir con cada una de las siguientes indicaciones (¡son mayormente sencillas!).

### Documentación

- [ ] Tiene documentación en MkDocs
- [ ] Hay una "portada" con información general básica (en `index.md`)
- [ ] Fue borrada la nota y la advertencia de la portada (en `index.md`)
- [ ] Fueron eliminadas las páginas del enunciado del proyecto y solamente están los resultados del proyecto (en `mkdocs.yml:nav`)
- [ ] Coloca las fórmulas apropiadas utilizadas en el desarrollo
- [ ] Hay buena ortografía, en general
- [ ] La redacción es buena, en general

### Análisis de datos

- [ ] Hay una elección de la distribución y es apropiada o razonable.
- [ ] El modelo de probabilidad de los datos es un modelo de distribución estadística y no un KDE (*kernel density estimation*)
- [ ] La determinación de la distribución de las variables es hecha con "pruebas de bondad de ajuste", como las que hace `fitter` (Py5), no solamente con "inspección visual"
- [ ] La documentación especifica el modelo de la(s) tabla(s) utilizadas en la base de datos
- [ ] Adapta correctamente la escala horizontal (*bins*) del histograma de los datos
- [ ] La gráficas están bien rotuladas

### Recomendaciones

- [ ] Presenta los resultados numéricos importantes en una tabla, cuando es pertinente
- [ ] Coloca las variables en el texto y las fórmulas de forma nativa en LaTeX

### Código

- [ ] Convención de código PEP 8
- [ ] Convención de docstrings PEP 257

## Algunas recomendaciones para Markdown

La documentación está en Markdown, que tiene muchas posibilidades.

### Ejemplo de ecuaciones matemáticas

Sea $X$ (variable en línea) una variable aleatoria con:

$$
x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

donde $a \neq 0$ (ecuación en línea).

### Ejemplos de tablas

Herramienta recomendada: [TableConvert](https://tableconvert.com/).

| Producto | Precio |
|----------|--------|
| Piña     | 1500   |
| Melón    | 1250   |
| Manzana  | 2100   |
| Papaya   | 1200   |
