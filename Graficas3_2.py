import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Crear carpeta para guardar gráficas
output_folder = "graficas_3_2"
os.makedirs(output_folder, exist_ok=True)

# Cargar archivo CSV
df = pd.read_csv("docs/files/datos.csv")

# Diccionario de variables y sus distribuciones con parámetros
modelos = {
    'variable_1': {
        'dist': stats.halfnorm,
        'params': (0.0022181829218035, 3.4052904159672317)
    },
    'variable_2': {
        'dist': stats.lognorm,
        'params': (0.4776347930822498, 0.9672797396860469, 1.036331010527072)
    },
    'variable_3': {
        'dist': stats.gumbel_r,
        'params': (2.361798203506733, 0.1461273648800006)
    }
}

# Estilo visual
sns.set(style="whitegrid")

# Recorrer cada variable y generar su gráfica
for var, modelo in modelos.items():
    datos = df[var].dropna()

    # Obtener distribución y parámetros
    dist = modelo['dist']
    params = modelo['params']

    # Crear figura
    plt.figure(figsize=(10, 6))
    sns.histplot(datos, bins=30, stat='density', color='skyblue', label='Histograma')

    # Rango de x para la función de densidad
    x = np.linspace(min(datos), max(datos), 338800)
    pdf = dist.pdf(x, *params)
    plt.plot(x, pdf, 'r-', lw=2, label=f'{dist.name} ajustada')

    # Etiquetas y estilo
    plt.title(f'{var} - Histograma y ajuste de {dist.name}')
    plt.xlabel(var)
    plt.ylabel('Densidad')
    plt.legend()
    plt.tight_layout()
 
    # Guardar imagen
    filename = os.path.join(output_folder, f"{var}_histograma.png")
    plt.savefig(filename)
    plt.close()

print(f"Gráficas guardadas en la carpeta: {output_folder}")