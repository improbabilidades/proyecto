# Modelos de probabilidad de los datos

Una parte central del proyecto es modelar estadísticamente los datos con distribuciones de probabilidad.

En el `PyX` número 5 [Py5](https://github.com/fabianabarca/python) hay una discusión sobre modelado de datos con SciPy y Fitter.

En general, con el módulo `stats` del paquete SciPy es posible encontrar los parámetros de mejor ajuste para una distribución particular, utilizando el método `fit()` de las clases de variables aleatorias. Por ejemplo, para una distribución normal:

```python
from scipy import stats

params = stats.norm.fit(data)

print(params)
```

donde `data` es un conjunto de datos univariados.
