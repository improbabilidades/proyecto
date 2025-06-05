# Importa la biblioteca 'os' para trabajar con rutas de archivos y carpetas del sistema
import os

# Importa la biblioteca 'pandas' para manipulación y análisis de datos
import pandas as pd

# Importa 'pyplot' de la biblioteca 'matplotlib' para crear gráficos
import matplotlib.pyplot as plt

# Importa 'seaborn' para mejorar la apariencia visual de los gráficos
import seaborn as sns

# Obtiene la ruta del directorio donde se encuentra este script (.py)
base_dir = os.path.dirname(__file__)

# Construye la ruta completa hacia el archivo datos.csv que está dentro de la subcarpeta "files"
file_path = os.path.join(base_dir, 'files', 'datos.csv')

# Lee el archivo CSV y lo guarda como un DataFrame (estructura de tabla)
df = pd.read_csv(file_path)

# Configura el estilo visual de los gráficos con fondo blanco y cuadrícula
sns.set(style="whitegrid")

# Lista de nombres de columnas numéricas que se van a graficar
variables = ['variable_1', 'variable_2', 'variable_3']

# Crea una figura con 1 fila y 3 subgráficas (una para cada variable), tamaño 18x5 pulgadas
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Itera sobre cada par de eje (ax) y variable para graficar los histogramas
for ax, var in zip(axes, variables):
    ax.hist(df[var], bins=20, color='skyblue', edgecolor='black')  # Histograma con 20 barras, color azul claro
    ax.set_title(f'Histograma de {var}')  # Título del gráfico
    ax.set_xlabel(var)                    # Etiqueta del eje X
    ax.set_ylabel('Frecuencia')          # Etiqueta del eje Y

# Ajusta automáticamente los espacios entre los subgráficos
plt.tight_layout()

# Muestra los gráficos en una ventana emergente
plt.show()
