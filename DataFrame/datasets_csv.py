import pandas as pd
# Lectura de archivos csv 
dataframe = pd.read_csv('DataFrame/archivo_csv/ModalidadVirtual.csv')
print(dataframe)
print(dataframe['carrera'][1]) 

#Filtrado de elementos
filtrar = dataframe['edad'] > 23
df_filtrar = dataframe[filtrar]
print(df_filtrar)

# Llamando primeras n columnas
print(dataframe.head(10))

# Llamando las n últimas columnas
print(dataframe.tail(10))


