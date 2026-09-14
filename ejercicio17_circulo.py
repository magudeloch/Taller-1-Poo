import math
print(math.pi)
class circulo:
    def __init__(self,radio):
        self.radio=radio

    def calculo(self):
        area=math.pi*(self.radio**2)
        longitud=2*math.pi*self.radio
        print(f'{area} \n {longitud}')
tuki=circulo(int(input("Valor del radio")))
tuki.calculo()
        