#**kwargs
def Imprimir_info(**info):
    print(info)
    for clave, valor in info.items():
        print(f"{clave}:{valor}")



Imprimir_info( Nombre="Juan", edad=25, ciudad="Espana")
