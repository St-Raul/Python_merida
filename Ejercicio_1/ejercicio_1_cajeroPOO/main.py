from modules.CuentaPremium import CuentaPremium
from modules.CuentaBancaria import CuentaBancaria     
cuenta1=CuentaBancaria("Juanma","01")
cuenta2=CuentaPremium("Juan", "02")
cuentaCajero=CuentaPremium("Cajero", -1)

dict_cuentas= {"1234": cuenta1, "4321":cuenta2}
dict_tlf = {"01": cuenta1, "02": cuenta2}

eleccion=-1
menu= """
    [1] - Ingresar cantidad
    [2] - Retirar cantidad
    [3] - Consultar saldo
    [4] - Transferencia bancaria
    [5] - Transferencia por Bizum
    [0] - Salir
    
    Por favor, introduzca una opcion:
"""

print("-------------------------------------------------------------------------------")
print("Bienvenido a tu cajero automático interactivo\n")



        

while True:
    eleccion=float(input(menu))
    if(eleccion==1):
        cantidad=float(input("Dinero a ingresar: "))
        cantidad=round(cantidad,2)
        cuentaCajero.ingresar(cantidad)
    elif(eleccion==2):
        cantidad=float(input("Dinero a retirar: "))
        cantidad=round(cantidad,2)
        cuentaCajero.retirada(cantidad)
    elif(eleccion==3):
        cuentaCajero.consultar()
    elif(eleccion==4):
        cantidad=float(input("Dinero a transferir: "))
        cantidad=round(cantidad,2)
        while True:
            numCuenta=input("Introduzca el numero de cuenta al que se le va a transferir el cantidad: ")
            if (numCuenta in dict_cuentas):
                cuentaCajero.transferir(dict_cuentas[numCuenta],cantidad)
                break
            else:
                print("Numero de cuenta inexistente. Pruebe de nuevo")
    elif(eleccion==5):
        if cuentaCajero.telefono==-1:
            cuentaCajero.telefono=input("Introduzca el num de tlf con el que va a transferir cantidad por bizum: ")
        cuentaDestino=0
        while True:
            numeroDestino=input("Introduzca el num de tlf al que le va a transferir cantidad: ")
            for cuenta in dict_cuentas.values():
                if cuenta.telefono == numeroDestino:
                    cuentaDestino=cuenta
                    break
            if cuentaDestino==0:
                print("Numero de telefono inexistente. Pruebe otro.")
            else:
                break
        cantidad=float(input("Dinero a transferir: "))
        cantidad=round(cantidad,2)
        cuentaCajero.transferirBizum(cuentaDestino, cantidad)
                    
                    
            
    elif(eleccion==0):
        print("Hasta pronto!!")
        break
    else:
        print ("numero invalido")
                
