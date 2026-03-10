# son argumentos llamados args y sumando con la funcion sum()
def suma_Varios(*num):
    print(num)
    resultado=sum(num)
    print(resultado)

# Logrando colocar varios argumentos arbitrarios en un solo parametro con el uso de anteponer un asterisco
#al crear la funcion
suma_Varios(7,8,9,12,13,15,20)    