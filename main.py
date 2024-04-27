import pandas as pd

# Leer el archivo CSV
#data = pd.read_csv('Cuadro_de_mando.xlsx')
# Acceder a la hoja de datos_limpios
#datos_limpios = data['datos_limpios']

# Obtener los datos de la columna de Price EUR
#precios = datos_limpios['Price EUR']

nombre_archivo = "Cuadro_de_mando.xlsx"

# Leer el archivo .xlsx y especificar la hoja que deseas leer (por ejemplo, la tercera hoja)
hoja_deseada = 2

# Especificar la fila que contiene los nombres de las columnas (encabezado)
fila_encabezado = 3

# Leer el archivo .xlsx en un DataFrame
archivo = pd.read_excel(io=nombre_archivo, sheet_name=hoja_deseada, header=fila_encabezado)
precios = archivo['Price EUR']
print(precios)
# Definir los rangos
rangos = range(0, 400000, 5000)

# Inicializar el contador para cada rango
contador_rangos = {rango: 0 for rango in rangos}

# Contar los datos en cada rango
for precio in precios:
    precio = str(precio)[:-1]
    precio = int(precio)
    for rango in rangos:
        if precio <= rango:
            contador_rangos[rango] += 1
            break

# Imprimir los resultados
for rango, count in contador_rangos.items():
    print(f"Rango {rango}-{rango+5000}: {count} datos")