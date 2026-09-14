class test:

    def __init__(self,suma,x,y):
        self.suma =suma
        self.x = x
        self.y = y

    def calculo(self):
        self.suma = self.suma + self.x
        self.x = self.x + self.y**2
        self.suma = self.suma + (self.x / self.y)

    def resultado(self):
        print(f"El valor de x es : {self.x}")
        print(f"El valor de y es : {self.y}")
        print(f"El valor de la suma es: {self.suma}")

tuki = test(0,20,40)
tuki.calculo()
tuki.resultado()