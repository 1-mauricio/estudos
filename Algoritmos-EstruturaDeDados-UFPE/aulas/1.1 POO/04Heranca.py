#HERANÇA : A classe herda os atributos(variáveis) e métodos(funções) da classe "mãe"/"pai"
class Conta:
    def __init__(self, initCPF, initValorInicial):
        self.__cpf = initCPF
        self.__saldo = initValorInicial
        self.__taxaSaque = 0.001

    def fazerSaque(self, valor):
        self.__saldo -= valor + valor*self.__taxaSaque
        
    def retornaSaldo(self):
        return self.__saldo

class Poupanca(Conta):
    def __init__(self, initCPF, initValorInicial):
        super().__init__(initCPF, initValorInicial)
        self.__jurosMes = 0.02

    def fazerSaque(self, valor): #sobreescreve método
        self._Conta__saldo -= valor

    def aplicaRendimento(self):
        self._Conta__saldo = self._Conta__saldo + self._Conta__saldo*self.__jurosMes


conta1 = Conta("111-222-333-4", 100)
conta1.fazerSaque(40)

contaPoupanca1 = Poupanca("333-444-55-7", 400)
contaPoupanca1.fazerSaque(100)

print(conta1.retornaSaldo())
contaPoupanca1.aplicaRendimento()
print(contaPoupanca1.retornaSaldo())