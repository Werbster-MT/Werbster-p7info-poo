class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def inseri_endereco(self, cidade):
        self.__enderecos.append(Endereco(cidade))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade)

class Endereco:
    def __init__(self, cidade):
        self.__cidade = cidade

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

cliente1 = Cliente('João')
cliente1.inseri_endereco('Florianópolis')
print(cliente1.nome)
# João
cliente1.lista_enderecos()
# Florianópolis
del cliente1