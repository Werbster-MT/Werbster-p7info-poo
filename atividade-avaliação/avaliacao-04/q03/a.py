class Pai():
    def __init__(self):
        self.nome = 'Pedro'

    corCabelo = 'loiro'


class Filho(Pai):
    def __init__(self, nome):
        self.nome = nome
        self.corCabelo = super().corCabelo


p1 = Pai()
f1 = Filho('Marcos')
p1.corCabelo()
f1.corCabelo()