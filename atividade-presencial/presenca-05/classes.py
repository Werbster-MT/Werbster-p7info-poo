# Sistema Para venda de produtos e armazenamento de alguns dados de cada cliente

class Cliente:

    # Atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__endereco = None
    # Metodos

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco


class Endereco:
    # Atributos
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


class CarinhoDeCompras:
    # Atributo
    def __init__(self):
        self.produtos = []
    # Metodo

    def inserirproduto(self, produto):
        if isinstance(produto, Produto):
            self.produtos.append(produto)

    def listaprodutos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def somatotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor

        return total

class Produto:
    # Atributo
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor