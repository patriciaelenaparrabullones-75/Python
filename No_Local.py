def Funcion_Exterior():
    a=50


    def Funcion_Interior():
        nonlocal a
        a=40
        print("Hola funcion trabajando con variable no local o ambito encerrado:s",a)

    Funcion_Interior()
    

Funcion_Exterior()