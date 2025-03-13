class CuentaBancaria:
    def __init__(self, nombre, telefono, saldo=0):
        self.nombre=nombre
        self.telefono=telefono
        self.saldo=saldo
    
    def ingresar(self, cantidad):
        self.saldo+=cantidad
        print("Se ha añadido la cantidad de", cantidad, "€")
        print("Su nuevo saldo es de", self.saldo, "€")
    
    def retirada(self, cantidad):
        if(cantidad>self.saldo):
            print("Saldo insuficiente.")
        else:
            self.saldo-=cantidad
            print("Se ha retirado un total de", cantidad)
            print("Su nuevo saldo es de", self.saldo, "€")
    
    def consultar(self):
        print(self.nombre , ", el saldo de tu cuenta es de", self.saldo, "€")
        