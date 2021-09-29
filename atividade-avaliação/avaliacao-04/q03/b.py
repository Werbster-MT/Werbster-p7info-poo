class Conta:
    __total = 10000
    reserva = 0.1

    def __init__(self, id, saldo):
        self.__id = id
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        Conta.__total += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.__total -= valor

    def imprimirReserva(self):
        print(Conta.__total * Conta.reserva)

itau = Conta(123, 5000)
itau.deposito(1000)
print(itau.saldo)
Conta.imprimirReserva