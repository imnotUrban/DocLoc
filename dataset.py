import pandas as pd

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('train_data.csv')

# Selecciona las columnas que necesitas
columnas_seleccionadas = df[['date', 'title', 'text', 'url', 'clase']]

muestras_aleatorias = columnas_seleccionadas.sample(n=700, random_state=42)  # Puedes cambiar el valor de random_state si lo deseas
muestras_aleatorias.to_csv('muestras_aleatorias.csv', index=False)