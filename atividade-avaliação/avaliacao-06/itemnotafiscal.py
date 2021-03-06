from produto import Produto
from DB import db

"""
    Módulo itemnotafiscal 
    Classe ItemNotaFiscal 
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.            
"""


class ItemNotaFiscal(db.Model):
    __tablename__ = 'TB_ITEM_NF'

    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    produtoID = db.Column(db.Integer, db.ForeignKey("TB_PRODUTO.id"), nullable=False)
    NotaFiscalID = db.Column(db.Integer, db.ForeignKey("TB_NOTA_FISCAL.id"), nullable=False)

    def __init__(self, id, sequencial, quantidade, produtoID, NotaFiscalID):
        super().__init__(id=id, sequencial=sequencial, quantidade=quantidade, produtoID=produtoID,
                         NotaFiscalID=NotaFiscalID)
        produto = Produto.query.filter_by(id=self.produtoID)
        self.descricao = produto[0].descricao
        self.valorUnitario = produto[0].valorUnitario
        self.valorItem = self.quantidade * self.valorUnitario

    def str(self):
        string = "\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(
            self.valorItem,
            self.valorUnitario,
            self.descricao,
            self.quantidade,
            self.sequencial,
            self.id)
        return string


if __name__ == '__main__':
    it1 = ItemNotaFiscal(1, 1, 10, 1, 0)
    print(it1.str())

