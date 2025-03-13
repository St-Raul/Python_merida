
class CuentaBancaria:
    def __init__(self, numero_cuenta, persona, saldo=0):
       self.numero_cuenta=numero_cuenta
       self.persona=persona
       self.saldo=saldo
       
       
    def ingresar(self, cantidad):
        if cantidad>0:
            self.saldo+=cantidad
            print(f"Se ha ingresado {cantidad}€ correctamente. ") #Nueva cantidad {self.saldo} €
            
    def retirar(self, cantidad):  
        if cantidad < self.saldo and cantidad >0:
            self.saldo-=cantidad
            print(f"Se ha retirado {cantidad}€ correctamente. Nuevo saldo: {self.saldo} €")
        else:
                print("Saldo insuficiente.")
                
    def consultar(self):
        print(f"Tu saldo actual de la cuenta es: {self.saldo} €") 
    
    