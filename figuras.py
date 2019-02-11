class Figura():
    def __init__(self):
        pass
    def get_area(self):
        return print("La figura no tiene área")
    def get_perimetro(self):
        return print("La figura no tiene perímetro") #Clase abstracta

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def get_area(self):
        return (self.lado * self.lado)
    def get_perimetro(self):
        perimetro = (self.lado * 4)
        return perimetro
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
    def get_area(self):
        return (self.base * self.altura)
    def get_perimetro(self):
        return (self.base*2 + self.altura*2)


a = Cuadrado(7)
print(a.get_area())
b = Rectangulo(2,3)
print(b.get_area())

