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

from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal
from DB import db
import datetime


class NotaFiscal(db.Model):
    __tablename__ = 'TB_NOTA_FISCAL'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    clienteID = db.Column(db.Integer, db.ForeignKey("TB_CLIENTE.id"), nullable=False)
    data = db.Column(db.String, nullable=False)
    itens = db.relationship("ItemNotaFiscal", backref="NotaFiscal", lazy=True)

    def __init__(self, id, codigo, clienteID):
        super().__init__(id=id, codigo=codigo, clienteID=clienteID, data=datetime.datetime.now().strftime("%d-%m-%Y"))

    def calcularNotaFiscal(self):
        itens = ItemNotaFiscal.query.filter_by(id=self.id)
        valor = 0.0
        for item in itens:
            valor = valor + item.valorItem
        self.valorNota = valor

    def getCliente(self):
        clientePesquisa = Cliente.query.filter_by(id=self.clienteID)
        cliente = dict()
        cliente["nome"] = clientePesquisa[0].nome
        cliente["codigo"] = clientePesquisa[0].codigo
        cliente["cnpjcpf"] = clientePesquisa[0].cnpjcpf
        return cliente

    def imprimirNotaFiscal(self):
        print(
            "---------------------------------------------------------------------------------------------------------------")
        print("{:101}{}".format("NOTA FISCAL", self.data))
        print("Cliente:     {:<10}Nome: {}".format(self.getCliente()["codigo"], self.getCliente()["nome"]))
        print("CPF/CNPJ:    {}".format(self.getCliente()["cnpjcpf"]))
        print(
            "---------------------------------------------------------------------------------------------------------------")
        print("ITENS")
        print(
            "---------------------------------------------------------------------------------------------------------------")
        print("{:4s} {:56s}      {:3s}       {:^10s}       {:^15s}".format("Seq", "Descrição", "QTD", "Valor unit",
                                                                           "preço"))
        print(
            "---- --------------------------------------------------------     -----     ------------     ------------------")
        for item in self.itens:
            print("{:4s} {:56s}      {:>3s}       {:>10s}       {:>15s}".format(str(item.sequencial),
                                                                                str(item.descricao),
                                                                                str(item.quantidade),
                                                                                str(item.valorUnitario),
                                                                                str(item.valorItem)
                                                                                ))
        print(
            "_______________________________________________________________________________________________________________")
        self.calcularNotaFiscal()
        print("Valor Nota Fiscal= " + str(self.valorNota))
