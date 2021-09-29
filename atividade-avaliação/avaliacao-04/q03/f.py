
class Casa:
    def __init__(self):
        self.__endereco = 'Rua ABC'

    def acenderLuzes(self):
        print('Estou acendendo as luzes!')

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def entrarNoLocal(self, local: any):
        local.acenderLuzes()

minhaCasa = Casa()
p1 = Pessoa('José')
p1.entrarNoLocal(minhaCasa)
