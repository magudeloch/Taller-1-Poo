# en github---> nombre completo de la uni___numero de actividad__ numero del estudiante__nombre del docente

class Personas:

    def __init__(self, nombre, edad):
            self.nombre=nombre
            self.edad=edad
            
Alberto =Personas("Alberto",2/3)
Ana =Personas("Ana",4/3)
juan=Personas("juan",int(input("edad de juan:")))
edalberto=(Alberto.edad)*(juan.edad)
edana=(Ana.edad)*(juan.edad)
edmami= (edalberto)+(edana)+(juan.edad)

print(f"Edad de Alberto: {edalberto}")
print(f"Edad de Ana: {edana}")
print(f"Edad de Juan: {juan.edad}")
print(f"Edad de la Mama: {edmami}")