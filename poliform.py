
class Animal: 
    def __init__(self, tamanho, cor, peso):
        self.tamanho = tamanho 
        self.cor = cor 
        self.peso = peso 
    
    def __str__(self):
        return f'eu sou {self.cor}'

class Cachorro(Animal):
    def latir(self):
        print("au au")

cachorro = Cachorro("um metro", 'verde', 100)
print(cachorro.__str__()) 
cachorro.latir()



     