#Tratando a la funcion como un objeto
def Saludar(nombre):
    return f"Hola ,{nombre}"


saludo=Saludar#Referenciando la funcion, no llamandola
print(saludo("Patricia"))