# Importamos las librerías necesarias
import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base de datos SQLite utilizando SQLAlchemy
# Esto nos permitirá interactuar con la base de datos 'proyecto.db'
engine = create_engine('sqlite:///proyecto.db')

# Cargar los datos de la tabla 'test_data' en un DataFrame de pandas
# El DataFrame nos permite manipular y analizar los datos fácilmente
df = pd.read_sql_table('test_data', con=engine)

# Convertimos las columnas a formato numérico
# Esto asegura que los datos numéricos en las columnas 'variable_1', 'variable_2', 'variable_3' sean tratados correctamente
df['variable_1'] = pd.to_numeric(df['variable_1'], errors='coerce')  # Coerce convierte valores no numéricos a NaN
df['variable_2'] = pd.to_numeric(df['variable_2'], errors='coerce')
df['variable_3'] = pd.to_numeric(df['variable_3'], errors='coerce')

# Calculamos los momentos estadísticos básicos de las tres variables
# Estos cálculos nos proporcionan información descriptiva sobre la distribución de los datos

# Promedio (Media)
mean_values = df[['variable_1', 'variable_2', 'variable_3']].mean()

# Varianza
variance_values = df[['variable_1', 'variable_2', 'variable_3']].var()

# Desviación estándar (raíz cuadrada de la varianza)
std_deviation = df[['variable_1', 'variable_2', 'variable_3']].std()

# Inclinación (skewness) mide la asimetría de la distribución de los datos
skewness = df[['variable_1', 'variable_2', 'variable_3']].skew()

# Curtosis (kurtosis) mide el "peso" de las colas de la distribución
kurtosis = df[['variable_1', 'variable_2', 'variable_3']].kurt()

# Imprimimos los resultados en consola para tener una vista rápida de los valores calculados
# Esto ayuda a verificar si todo está correcto antes de escribir los resultados en el archivo Markdown
print("📊 Momentos estadísticos calculados:\n")

# Mostramos el cálculo del promedio (media)
print("**Promedio (Media):**")
print(f"variable_1: {mean_values['variable_1']:.6f}")
print(f"variable_2: {mean_values['variable_2']:.6f}")
print(f"variable_3: {mean_values['variable_3']:.6f}\n")

# Mostramos la varianza calculada
print("**Varianza:**")
print(f"variable_1: {variance_values['variable_1']:.6f}")
print(f"variable_2: {variance_values['variable_2']:.6f}")
print(f"variable_3: {variance_values['variable_3']:.6f}\n")

# Mostramos la desviación estándar
print("**Desviación estándar:**")
print(f"variable_1: {std_deviation['variable_1']:.6f}")
print(f"variable_2: {std_deviation['variable_2']:.6f}")
print(f"variable_3: {std_deviation['variable_3']:.6f}\n")

# Mostramos la inclinación (skewness)
print("**Inclinación (skewness):**")
print(f"variable_1: {skewness['variable_1']:.6f}")
print(f"variable_2: {skewness['variable_2']:.6f}")
print(f"variable_3: {skewness['variable_3']:.6f}\n")

# Mostramos la curtosis (kurtosis)
print("**Curtosis (kurtosis):**")
print(f"variable_1: {kurtosis['variable_1']:.6f}")
print(f"variable_2: {kurtosis['variable_2']:.6f}")
print(f"variable_3: {kurtosis['variable_3']:.6f}\n")

# Ahora escribimos los resultados en un archivo Markdown (modelos.md) para documentar el análisis
# Esto es útil para la presentación de los resultados en una página web o para compartir con otros miembros del equipo
with open('docs/modelos.md', 'w') as file:
    # Escribimos el título del documento
    file.write("# Modelos de Datos\n\n")
    
    # Escribimos las fórmulas que utilizamos para calcular los momentos estadísticos
    file.write("### Cálculos realizados\n")
    file.write("Para cada variable se calcularon los siguientes momentos estadísticos:\n\n")
    
    file.write("1. **Promedio (Media)**\n")
    file.write("   $$ \\mu = \\frac{1}{n} \\sum_{i=1}^{n} x_i $$\n\n")
    
    file.write("2. **Varianza**\n")
    file.write("   $$ \\sigma^2 = \\frac{1}{n-1} \\sum_{i=1}^{n} (x_i - \\mu)^2 $$\n\n")
    
    file.write("3. **Desviación estándar**\n")
    file.write("   $$ \\sigma = \\sqrt{\\sigma^2} $$\n\n")
    
    file.write("4. **Inclinación (skewness)**\n")
    file.write("   $$ \\text{skew}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\left( \\frac{x_i - \\mu}{\\sigma} \\right)^3 $$\n\n")
    
    file.write("5. **Curtosis (kurtosis)**\n")
    file.write("   $$ \\text{kurt}(x) = \\frac{1}{n} \\sum_{i=1}^{n} \\left( \\frac{x_i - \\mu}{\\sigma} \\right)^4 $$\n\n")
    
    # Escribimos los resultados obtenidos en formato tabla Markdown
    file.write("### Resultados obtenidos\n")
    file.write("| Momento               | variable_1 | variable_2 | variable_3 |\n")
    file.write("|-----------------------|------------|------------|------------|\n")
    file.write(f"| **Promedio**          | {mean_values['variable_1']:.6f} | {mean_values['variable_2']:.6f} | {mean_values['variable_3']:.6f} |\n")
    file.write(f"| **Varianza**          | {variance_values['variable_1']:.6f} | {variance_values['variable_2']:.6f} | {variance_values['variable_3']:.6f} |\n")
    file.write(f"| **Desviación estándar** | {std_deviation['variable_1']:.6f} | {std_deviation['variable_2']:.6f} | {std_deviation['variable_3']:.6f} |\n")
    file.write(f"| **Inclinación (skew)** | {skewness['variable_1']:.6f} | {skewness['variable_2']:.6f} | {skewness['variable_3']:.6f} |\n")
    file.write(f"| **Curtosis**          | {kurtosis['variable_1']:.6f} | {kurtosis['variable_2']:.6f} | {kurtosis['variable_3']:.6f} |\n")

    # Sección para la interpretación de los resultados
    file.write("\n### Interpretación de los resultados\n")
    file.write("Aquí puedes agregar tu interpretación de los resultados...\n")
