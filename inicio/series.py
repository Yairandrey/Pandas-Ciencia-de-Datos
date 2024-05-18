import pandas as pd

#Series : es una matriz con 2 columnas y tantas filas
naranjas = pd.Series([4,9,2,6,10,200])
print(naranjas)
nombres = pd.Series(["Yair", "Jorge"])
print(nombres)

#Creación de una Serie a base de una lista
colores = pd.Series(["azul", "rojo", "verde", True])
print(colores)

#Creación de una Serie a base de un dicionario
materias = pd.Series({'matematicas':4.5, 'fisica': 5.0, 'biologia':3.4})
print(materias)

# Métodos de las Series
numeros = pd.Series([3,6,7,0,5,2])
cantida_de_elementos = numeros.size
print(cantida_de_elementos)

print(numeros.index)
print(numeros.dtype)

# Accesos a la serie. Se llama igual que una lista
print(numeros[3:4])

print(materias[['fisica','biologia']])