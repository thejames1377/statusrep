

class formageometrica:
    def calcular_a_área(self, raio):
        return 3.14*(raio**2)

class circulo(formageometrica):
     pass
    
class retangulo(formageometrica):   
     def calcular_a_área(self, base, altura):
         return base*altura

circulo = circulo()
area = circulo.calcular_a_área(20)     
print(area)

retangulo = retangulo()
area = retangulo.calcular_a_área(5,10)
