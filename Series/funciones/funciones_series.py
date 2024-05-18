import pandas as pd
numeros = pd.Series([100,2000,456,34,-3,123,123,567])
suma = numeros.sum()
print(f'suma: {suma}')
minimo = numeros.min()
print(f'minimo: {minimo}')
maximo = numeros.max()
print(f'maximo:{maximo}')

desviacion_estandar = numeros.std()
print(f'desviacion estandar: {desviacion_estandar}')

descripcion = numeros.describe()
print(f'descripcion:{descripcion}')

serie = pd.Series({'ingles':12, 'economia':34, 'programacion':50,'religion': 23, 'historia':12})
# Filtrar contenido a partir de alguna condicion
print(serie[serie >20])

# Ordenando de acuerdo al valor almacenado
print(serie.sort_values())

# Orden por index
print(serie.sort_index(ascending=False))

# Crear una serie a partir de una dato (escalar)
data = 10
# El index genera las posiciones de la Serie
serie_2 = pd.Series(data,index=[0,1,2,3,4,5])
print(serie_2)