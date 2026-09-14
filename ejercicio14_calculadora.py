class calcuradora:

    def __init__(self,numero,cuadrado,cubo):
        self.numero=numero
        self.cuadrado=cuadrado
        self.cubo=cubo

    def proceso(self):
        self.cuadrado=self.numero**2
        self.cubo=self.numero**3

    def resultado (self):
        print(self.cuadrado)
        print(self.cubo)
tuki=calcuradora(int(input("Ingrese numero:")), 8, 0)
tuki.proceso()
tuki.resultado()
