#Funciones que pueden tomar una o mas funciones como argumentos y o devolver funciones como resultado
def cuadrado(x):
    return x*x


def cubo(x):
    return x ** 3


def aplicar_funcion(funcion,valor):
    return funcion(valor)

print("Imprimiendo las funciones de Orden Superior")
print("Funcion que calcula el cuadrado de un numero:")
resultado=aplicar_funcion(cuadrado,6)
print(resultado)
print("Funcion que calcula el cubo de un numero:")
resultado=aplicar_funcion(cubo,3)
print(resultado)
