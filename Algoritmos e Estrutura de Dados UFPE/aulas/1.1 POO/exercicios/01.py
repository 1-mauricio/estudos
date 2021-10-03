class Aluno:
    def __init__(self, initCPF, initNome):
        self.__cpf = initCPF
        self.__nome = initNome

    def inicializarNota(self, nota, numeroProva):
        if self.__numeroNota == 1:
            self.__nota = nota
        self.__numeroNota = numeroProva

    def verificaSituacaoMedia(self):
        media = self.__numero
        if media > 7:
            True
        else:
            False

    def imprimeInformacoes(self):
        print(self.__nome, self.__cpf,)

aluno1 = Aluno("12345678901", "Maurício")
for i in range(1,4):
    nota = float(input(f"Digite a {i} nota: "))
    aluno1.inicializarNota(nota, i)

