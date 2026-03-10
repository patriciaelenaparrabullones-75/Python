def contar_hasta_cero(n):
    if n<=0:
        print("He llegado a cero!")
    else:
        print(n)
        contar_hasta_cero(n-1)
                          
                          
print("Funcion Factorial!")
contar_hasta_cero(10)