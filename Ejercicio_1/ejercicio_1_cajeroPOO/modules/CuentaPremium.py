from modules.CuentaBancaria import CuentaBancaria


class CuentaPremium(CuentaBancaria):
    def __init__(self, nombre, telefono, saldo=0):
        super().__init__(nombre, telefono, saldo)
        
    def transferir(self, cuenta, cantidad):
        #Posible mejora de codigo, implementando listas de cuentas con validaciones
        if(cantidad>self.saldo):
            print("Saldo insuficiente.")
        else:
            self.saldo-=(cantidad+cantidad*0.05)
            print("Se ha enviado", cantidad, "€")
            cuenta.saldo+=cantidad
            print("Su nuevo saldo es de", self.saldo, "€")
            
    def transferirBizum(self, cuenta, cantidad):
        #Posible mejora de codigo, implementando listas de cuentas con validaciones
        if(cantidad>self.saldo):
            print("Saldo insuficiente.")
        else:
            self.saldo-=cantidad
            print("Se ha enviado", cantidad, "€")
            cuenta.saldo+=cantidad
            print("Su nuevo saldo es de", self.saldo, "€")
            