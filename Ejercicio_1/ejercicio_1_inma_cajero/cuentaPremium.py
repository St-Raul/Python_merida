from cuentaBancaria import CuentaBancaria 

class CuentaPremium(CuentaBancaria):
    def __init__(self, persona, saldo=0, telefono=None):
        super().__init__( persona, saldo)
        self.telefono= telefono
        
        
    def transferir(self, cantidad, cuenta):
        if cantidad > 0:
            comision = cantidad * 0.05
            print("Comision:",comision )
            total = cantidad + comision
            print("Total a quitar: ", total)
            if self.saldo >= total:
                self.saldo=self.saldo-total
               # cuenta.ingresar(cantidad) esto no
                print(f"Transferencia de {cantidad}€ realizada. Comisión: {comision} €")
                print(f"Nuevo saldo: {self.saldo} €")
            else:
                print("Saldo insuficiente para realizar la transferencia.")
        else:
            print("La cantidad a transferir debe ser positiva.")



    def configurar_telefono_bizum(self, telefono):
        if not self.telefono:
            self.telefono = telefono
            print(f"Teléfono {telefono} registrado para Bizum")
        else:
            print("El teléfono ya estaba configurado")


    def transferencia_bizum(self, cantidad, cuenta_destino):
        if not self.telefono:
            print("Primero debe registrar su teléfono en Bizum")
            return
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
            return
        
        if self.saldo >= cantidad:
            #self.saldo =self.saldo-cantidad
            self.saldo -= cantidad
            cuenta_destino.ingresar(cantidad)
            print(f"Bizum de {cantidad}€ realizado")
            print(f"Nuevo saldo: {self.saldo}€")
        else:
            print("Saldo insuficiente para la transferencia.")