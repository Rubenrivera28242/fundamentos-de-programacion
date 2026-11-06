import pandas as pd

#cargar datos
ruta = "https://raw.githubusercontent.com/VMjavier/claseAnalisisDatos/refs/heads/main/veterinaria_colombia.csv"
df = pd.read_csv(ruta)

print("="*50)
print(df.head())
print("-"*50)

print("="*50)
print(df.info())
print("-"*50)

print("="*50)
print(df.describe())
print("-"*50)

print("="*50)
print(df.columns)
print("-"*50)

print("="*50)
df.isnull().sum()

print("="*50)
df.shape #filas columnas

print("="*50)
df['Raza']

print("="*50)
df[['Raza','Especie']]

print("="*50)
df[df['Raza'] =='Criollo']
