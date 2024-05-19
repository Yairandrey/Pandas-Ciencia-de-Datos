# data: diccionario
# index: filas
# columns = columnas
import pandas as pd
import numpy as np
# DataFrame a partir de un dicionario
data = {
    'nombre':["Yair","Andrey","Jose"], 
    'carrera': ["Ing.Sistemas", "Zootecnia", "Física"],
    'correo': ["yair@gmail.com", "andrey@gmail.com", "jose@gmail.com"]
    }
dataframe = pd.DataFrame(data)
print(dataframe)

# DataFrame a partir de un lista
df = pd.DataFrame([['Maria', 27], ['Pedro', 79], ['Pepito', 3]], columns=['NOMBRE', 'EDAD'])
print(df)

# DataFrame a partir de un array definiendo sus dimensiones
df = pd.DataFrame(np.random.randn(4,5), columns=['a','b','c','d','e'])
print(df)
