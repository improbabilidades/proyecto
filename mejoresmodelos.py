import pandas as pd
import os
from fitter import Fitter

# Leer datos
df = pd.read_csv("docs/files/datos.csv")

# Crear carpeta para guardar imágenes
output_dir = 'fitter_graficas'
os.makedirs(output_dir, exist_ok=True)

variables = ['variable_1', 'variable_2', 'variable_3']

for var in variables:
    data = df[var].values
    
    # Crear fitter y ajustar
    f = Fitter(data)
    f.fit()
    
    # Mostrar resumen en consola (opcional)
    print(f"--- Resultados para {var} ---")
    print(f.summary())                          # genera una tabla resumen con los mejores ajustes

