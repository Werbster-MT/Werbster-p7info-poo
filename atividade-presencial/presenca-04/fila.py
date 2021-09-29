class Fila(object):
    def __init__(self):
        self.dados = []

    def inserir(self, elemento):
        self.dados.append(elemento)

    def retirar(self):
        return self.dados.pop(0)

    def estaVazia(self):
        return len(self.dados) == 0

    def exibir(self):
        for i in self.dados:
            print(i)

seq = Fila()
print('Está vazia: {}'.format(seq.estaVazia()))
seq.inserir(1)
seq.inserir(2)
seq.inserir(3)
seq.exibir()
seq.retirar()
print('Após Remover:')
seq.exibir()