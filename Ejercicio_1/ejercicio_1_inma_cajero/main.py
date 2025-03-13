from cuentaBancaria import CuentaBancaria
from cuentaPremium import CuentaPremium

"""cuenta por defecto mia"""
cuenta = CuentaBancaria("63", 'inma')



cuentasBizum = {
    "60": CuentaPremium("Ana Pérez", 1000.0, "60"),  # Cuenta principal
    "62": CuentaPremium("Carlos Gómez", 800.0, "62"),
    "61": CuentaPremium("Laura Díaz", 500.0, "61")
}


cuentaPremium = cuentasBizum["60"]

print("____________- Menú -___________")
print("1- Ingresar dinero             |")
print("2- Retirar dinero              |")
print("3- Consultar saldo             |")
print("4- Trasferencia bancaria       |")
print("5- Trasferencia bizum          |")
print("6- Salir                       |")
print("_______________________________|")
print("Bienvenido")


while True:
    try:
        
        eleccion= input("Elija una opción: ")

        if eleccion == "1":
            dineroIngresar= float(input("Ingrese la cantidad a ingresar: "))
            dineroIngresar=round(dineroIngresar,2)
            cuentaPremium.ingresar(dineroIngresar)
            
        elif eleccion == "2":
            dineroRetirar= float(input("Ingrese la cantidad que desea retirar: "))
            dineroRetirar=round(dineroRetirar,2)
            cuentaPremium.retirar(dineroRetirar)
        elif eleccion == "3":
            cuentaPremium.consultar()     
        elif eleccion == "4":
            cantidad = float(input("Ingrese la cantidad a transferir: "))
            cantidad = round(cantidad, 2)
            cuentaPremium.transferir(cantidad, cuenta) 
        
        elif eleccion == "5":
            if not cuentaPremium.telefono:
                telefono = input("Ingrese su teléfono para Bizum: ")
                cuentaPremium.configurar_telefono_bizum(telefono)

            telefono_destino = input("Teléfono del destinatario: ")
            cantidad = float(input("Cantidad a transferir: "))

   
            if telefono_destino in cuentasBizum:
                cuenta_destino = cuentasBizum[telefono_destino]
                cuentaPremium.transferencia_bizum(cantidad, cuenta_destino)
            else:
                print("Teléfono no registrado en Bizum")
                  
        elif eleccion == "6":
            print("Gracias por usar Cajeros Inma. ¡Hasta luego!")
            break
        else:
                print("Opción no válida. Por favor, intente de nuevo.")
        
    except ValueError:
        print("Entrada no válida")  