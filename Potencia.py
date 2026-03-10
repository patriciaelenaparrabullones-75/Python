def cuadrado(x):
    return x*x


def cubo(x):
    return x ** 3


def aplicar_funcion_a_Lista(funcion,lista):
    resultado=[]
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado


lista_num=[1, 2, 3, 4, 5, 6, 7]
aplicar_funcion_a_Lista(cuadrado,lista_num)
print("Imprimiendo la funcion cuadrado con funcion de Orden Superior")
print(aplicar_funcion_a_Lista(cuadrado,lista_num))
Re=aplicar_funcion_a_Lista(cubo,lista_num)
print("Imprimiendo la funcion cubo con funcion de Orden Superior")
print(Re)












"""print("Imprimiendo las funciones de Orden Superior")
print("Funcion que calcula el cuadrado de un numero:")
resultado=aplicar_funcion(cuadrado,6)
print(resultado)
print("Funcion que calcula el cubo de un numero:")
resultado=aplicar_funcion(cubo,3)
print(resultado)"""
