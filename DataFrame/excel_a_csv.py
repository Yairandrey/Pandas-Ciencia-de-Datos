import pandas as pd

df = pd.read_excel('DataFrame/archivo_csv/estudiantes.xlsx')
print(df)

# Coniverto el archivo de extensión xlsx a csv
df.to_csv("DataFrame/archivo_csv/estudiantes.csv", index=None, header=True)
print(df)


# Acceso a posiciones
print(df.iloc[2,:2])


# Acceso a través de los headers(deben estar escritos tal cual)
print(df.loc[:1,("Edad","Codigo")])

# Añadir columnas al DataFrame
df["Turno"] = pd.Series(["tarde", "noche", "mañana", "medianoche", "tarde"])

print(df)

# Elimino elementos
Codigo = df.pop("Codigo")
print(df)

# Añado filas al DataFrame
df = df._append(pd.Series(["carlos",34,6, "tarde"], index=["Nombre", "Edad", "Semestre", "Turno"]), ignore_index = True)
print(df)

# Elimino fila del DataFrame
df.drop([1,2])
print(df)


