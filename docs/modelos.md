# Modelos de Datos

### Cálculos realizados
Para cada variable se calcularon los siguientes momentos estadísticos:

1. **Promedio (Media)**
   $$ \mu = \frac{1}{n} \sum_{i=1}^{n} x_i $$

2. **Varianza**
   $$ \sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \mu)^2 $$

3. **Desviación estándar**
   $$ \sigma = \sqrt{\sigma^2} $$

4. **Inclinación (skewness)**
   $$ \text{skew}(x) = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{x_i - \mu}{\sigma} \right)^3 $$

5. **Curtosis (kurtosis)**
   $$ \text{kurt}(x) = \frac{1}{n} \sum_{i=1}^{n} \left( \frac{x_i - \mu}{\sigma} \right)^4 $$

### Resultados obtenidos
| Momento               | variable_1 | variable_2 | variable_3 |
|-----------------------|------------|------------|------------|
| **Promedio**          | 1.182916 | 2.131259 | 2.447002 |
| **Varianza**          | 8.837140 | 0.385909 | 0.037444 |
| **Desviación estándar** | 2.972733 | 0.621216 | 0.193504 |
| **Inclinación (skew)** | 43.915523 | 2.713515 | 1.479704 |
| **Curtosis**          | 6403.742860 | 24.254801 | 5.312837 |

### Interpretación de los resultados
Aquí puedes agregar tu interpretación de los resultados...
