class Conta:
    def __init__(self, initCPF, initValorInicial):
        self.__cpf = initCPF
        self.__saldo = initValorInicial
        self.__taxaSaque = 0.001

    def fazerSaque(self, valor):
        self.__saldo -= valor + valor*self.__taxaSaque
        
    def retornaSaldo(self):
        return self.__saldo

conta1 = Conta("111-222-333-4", 100)
conta1.fazerSaque(40)
print(conta1.retornaSaldo())

conta1._Conta__saldo = 2
print(conta1._Conta__saldo) #o nome da variável é na verdade conta1_Conta__saldo, do contrario (conta1.__saldo) o python irá criar outra variavel
print(conta1.retornaSaldo())

# quando declaramos uma variável com dois underlines no inicio estamos informando ao programador que esperamos que essa variável não seja acessada diretamente
# mas, na verdade, ela pode ser acessada assim: conta1._Conta__saldo = 2