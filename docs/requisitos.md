# Requisitos del proyecto

Asegúrense de cumplir con cada una de las siguientes indicaciones (¡son, mayormente, sencillas!).

## Documentación

- [ ] Exista la documentación en MkDocs
- [ ] Hay una "portada" con información general básica (en `index.md`)
- [ ] Fue borrada la nota y la advertencia de la portada (en `index.md`)
- [ ] Fueron eliminadas las páginas del enunciado del proyecto y solamente están los resultados del proyecto (en `mkdocs.yml:nav`)
- [ ] Muestra las fórmulas utilizadas en el desarrollo del proyecto
- [ ] Hay buena ortografía, en general
- [ ] La redacción es buena, en general
- [ ] Coloca las variables en el texto y las fórmulas de forma nativa en LaTeX

## Análisis de datos

- [ ] Hay una elección de la distribución y es apropiada o razonable
- [ ] El modelo de probabilidad de los datos es un *modelo de distribución estadística* y no un KDE (*kernel density estimation*)
- [ ] La determinación de la distribución de las variables es hecha con "pruebas de bondad de ajuste", como las que hace `fitter` (Py5), y no solamente con "inspección visual"
- [ ] La documentación especifica el modelo de la(s) tabla(s) utilizadas en la base de datos (ejemplo: `class TestData`)
- [ ] Adapta correctamente la escala horizontal (*bins*) del histograma de los datos
- [ ] La gráficas están bien rotuladas (nombres y unidades en los ejes, cuando aplica)
- [ ] Presenta una síntesis de los resultados numéricos importantes en una tabla, cuando es pertinente

## Código

- [ ] El desarrollo del código está ampliamente comentado
- [ ] Las variables tienen nombres pertinentes (claridad mata brevedad)
- [ ] Adopta la convención de escritura de código [PEP 8](https://realpython.com/python-pep8/)
- [ ] Adopta la convención de documentación con *docstrings* [PEP 257](https://realpython.com/documenting-python-code/)

### Cómo dar formato al código

La mejor recomendación es instalar una extensión de formato automático en el editor (como VS Code). [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) o [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) son buenos y recomendados. Así, será posible dar formato automáticamente con, por ejemplo, `Alt` + `Shift` + `F`.

El código será evaluado usando `$ uv run ruff check .`, que devuelve una lista de errores (o violaciones a la norma) encontrados y habrá deducciones de puntos por esto. Para corregir esos problemas, simplemente es necesario hacer `$ uv run ruff format .` antes de enviar el proyecto.
