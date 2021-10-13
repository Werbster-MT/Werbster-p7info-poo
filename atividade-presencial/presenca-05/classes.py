class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insereEndereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listaEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print('{} foi apagado!'.format(self.nome))

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print('{}/{} foi apagado!'.format(self.cidade, self.estado))

class CarinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserirProduto(self, produto):
        if isinstance(produto, Produto):
            self.produtos.append(produto)

    def listaProdutos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def somaTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor

        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

