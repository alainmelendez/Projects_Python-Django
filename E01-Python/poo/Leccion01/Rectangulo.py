class Rectangulo:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))
rectangulo1 = Rectangulo(base, altura)

print(f'Area Rectángulo: {rectangulo1.calcularArea()}')

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))
rectangulo2 = Rectangulo(base, altura)

print(f'Area Rectángulo: {rectangulo2.calcularArea()}')
