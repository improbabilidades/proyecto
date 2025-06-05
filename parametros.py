from scipy import stats
import pandas as pd


# Leer datos
df = pd.read_csv("docs/files/datos.csv")

variable_1 = df['variable_1']
variable_2 = df['variable_2']
variable_3 = df['variable_3']

# Ajustar haldnorm a variable_1
params_halfnorm = stats.halfnorm.fit(variable_1)
print("Parámetros haldnorm para variable_1:", params_halfnorm)

# Ajustar lognorm a variable_2
params_lognorm = stats.lognorm.fit(variable_2)
print("Parámetros lognorm para variable_2:", params_lognorm)

# Ajustar gumbel_r a variable_3
params_gumbel_r = stats.gumbel_r.fit(variable_3)
print("Parámetros gumbel_r para variable_3:", params_gumbel_r)