eleccion=-1
menu= """
    [1] - Ingresar dinero
    [2] - Retirar dinero
    [3] - Conusltar saldo
    [4] - Transferencia bancariaç
    [5] - Transferencia por Bizum
    [0] - Salir
    
    Por favor, introduzca una opcion:
"""

print("-------------------------------------------------------------------------------")
print("Bienvenido a tu cajero automático interactivo\n")

while True:
    eleccion=float(input(menu))
    if(eleccion==1):
        print("eleccion 1")
    elif(eleccion==2):
        print("eleccion 2")
    elif(eleccion==3):
        print("eleccion 3")
    elif(eleccion==4):
        print("eleccion 4")
    elif(eleccion==5):
        print("eleccion 5")
    elif(eleccion==0):
        print("Hasta pronto!!")
        break
    else:
        print ("numero invalido")
                


