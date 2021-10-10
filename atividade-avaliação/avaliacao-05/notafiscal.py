"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado.
"""

import datetime
from cliente import Cliente
from produto import Produto
from itemnotafiscal import ItemNotaFiscal

class NotaFiscal():
    def __init__(self, Id, codigo, cliente : any):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota = valor

    # Atributo da classe
    data = str(datetime.date.today())
    data = data.replace("-", '/')

    #Métodos de classe
    @classmethod
    def linha(cls):
        print('-'*110)

    @classmethod
    def preencherCabecalho(cls, lista):
        NotaFiscal.linha()
        print('{:<100s}{:20s}'.format('Nota Fiscal', NotaFiscal.data))
        for linha in range(0, len(lista)):
            print('{:<10s}{:<16s}{:<5s}{:30s}'.format(lista[linha][0], lista[linha][1],
                                                      lista[linha][2], lista[linha][3]))
        NotaFiscal.linha()
        print('ITENS')
        NotaFiscal.linha()
        print('Seq   {:70s}{:>5s}{:^20s} {:<10s}'.format('Descrição', 'QTD', 'Valor Unit', 'Preço'))
        print('{}  {}  {}   {}   {}'.format('-'* 4, '-' * 69, '-' * 5, '-'*12, '-'*10))

    @classmethod
    def preencherFinal(cls, value):
        print('_' * 110)
        print('Valor Total:  {:.2f}'.format(value))

    # Juntando os métodos de classe para printar a nota fiscal
    def imprimirNotaFiscal(self):
        # cabeçalho
        cabecalho = [['Cliente: ', str(self._cliente._id), 'Nome: ', self._cliente._nome],
                     ['CPF/CNPJ', self._cliente._cnpjcpf, '', '']]
        NotaFiscal.preencherCabecalho(cabecalho)

        # Conteudo Principal
        valorTotal = 0

        for i in range(0, len(self._itens)):
            # pegando a sequência no formato "001"
            if self._itens[i]._produto._id > 0 and self._itens[i]._produto._id < 10:
                aux = '00'
                seq = aux + aux.join(str(self._itens[i]._produto._id))

            elif self._itens[i]._produto._id > 10 and self._itens[i]._produto._id < 100:
                aux = '0'
                seq = aux + aux.join(str(self._itens[i]._produto._id))

            else:
                seq = aux + aux.join(str(self._itens[i]._produto._id))

            # printando os itens
            print('{:<4s}  {:69s} {:>5s}{:^20s} {:<10s}'.format(seq,
                                                                self._itens[i]._produto._descricao,
                                                                str(self._itens[i]._quantidade),
                                                                str(self._itens[i]._valorUnitario),
                                                                str(self._itens[i]._valorItem)))
            valorTotal += self._itens[i]._valorItem

        # Resultado Final
        NotaFiscal.preencherFinal(valorTotal)