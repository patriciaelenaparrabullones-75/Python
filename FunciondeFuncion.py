def multiplicador(factor):
    def funcion_interna(num):
        return num*factor
    return funcion_interna


multiplicar_por_dos=multiplicador(2)
multiplicar_por_tres=multiplicador(3)
multiplicar_por_cinco=multiplicador(5)



print(multiplicar_por_dos(2))
print(multiplicar_por_tres(3))
print(multiplicar_por_cinco(5))


        