class Conta1:
    def __init__(self,saldo, limite):

        self.saldo = saldo
        self.limite = 0 - limite        # 0 - limite devido ao saldo negativo, esse é o menor valor que a conta poderá ter e deve ser definido quando criar a conta

    def depositar(self, quantidade):    # Método para depositar na conta
        if quantidade > 0:
            self.saldo += quantidade

        else:
            return False

    def consulta_saldo(self):           # Método para consultar o saldo do cliente
        return self.saldo

    def sacar(self, quant):             # Método para sacar na conta
        if self.saldo - quant < self.limite:
            return False
        else:
            self.saldo -= quant


    def __str__(self):      # Método para alterar o print de objetos da classe cliente
        return 'Saldo atual: R$' + str(self.saldo) + '\nLimite atual: R$' + str(self.limite)