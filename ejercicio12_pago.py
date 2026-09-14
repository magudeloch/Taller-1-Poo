class pago:
    def __init__(self,horas,valor):

        self.horas=horas
        self.valor=valor
        self.retencion=0
        self.ganancias=0
        self.salario=0

    def calculo(self):

        self.salario=self.valor*self.horas
        self.ganancias=self.salario*((100-12.5)/(100))
        self.retencion=self.salario*(12.5/100)
        
    def resultado(self):

        print(f"Salario Bruto: ${self.salario:,.0f}")
        print(f"Salario Neto: ${self.ganancias:,.0f}")
        print(f"Retención (12.5%): ${self.retencion:,.0f}") 

pago = pago(48,500)
pago.calculo()
pago.resultado()
 