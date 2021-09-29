import math

class Ponto:
    # Construtor
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    # Métodos getters e setters
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valor):
        self.__x = int(valor)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, valor):
        self.__y = int(valor)

    def imprimirPonto(self):
        return '({},{})'.format(self.__x, self.__y)

class Reta:
    # Construtor
    def __init__(self, a: any, b: any):
        self.__a = a
        self.__b = b

    # Métodos getters e setters
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, valor):
        self.__a = valor

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, valor):
        self.__b = valor

    # Método para calcular a distância
    def distancia(self):
        termoX = math.pow((self.__b.x - self.__a.x), 2)
        termoY = math.pow((self.__b.y - self.__a.y), 2)
        return math.sqrt(termoX + termoY)

p1 = Ponto(2, 4)
p2 = Ponto(2, 6)
reta = Reta(p1, p2)
print('A distância entre os pontos {} e {} é: {}'.format(p1.imprimirPonto(), p2.imprimirPonto(), reta.distancia()))