class Pet:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('Olá sou um Pet')

class Cachorro(Pet):
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        super().falar()
        print('Au au')

class Gato(Pet):
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        super().falar()
        print('Miau')
