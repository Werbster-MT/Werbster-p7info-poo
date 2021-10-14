from classes import *

if __name__ == '__main__':
    cliente = Cliente('Joãozinho', 30)
    endereco = Endereco('Fortaleza', 'Ceara')
    produto = Produto('feijao', 35)
    carinho = CarinhoDeCompras()
    carinho.inserirproduto(produto)  # ultilizando agregação
    carinho.listaprodutos()
    cliente.set_endereco(endereco)  # ultilizando associação