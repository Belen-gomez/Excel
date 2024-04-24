import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('car details v4.csv')

# Obtener el número de valores faltantes en cada columna
missing_values = data.isnull().sum()

# Imprimir los resultados
print(missing_values)