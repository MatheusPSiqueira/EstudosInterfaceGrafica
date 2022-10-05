class Conta1:
    def __init__(self,saldo, limite):

        self.saldo = saldo
        self.limite = 0 - limite

    def depositar(self, quantidade):
        if quantidade > 0:
            self.saldo += quantidade

        else:
            return False

    def consulta_saldo(self):
        return self.saldo

    def sacar(self, quant):
        if self.saldo - quant < self.limite:
            return False
        else:
            self.saldo -= quant