tab = {}
tamPref = qtd = 0
media = 0.0

cod = input("Digite o código da disciplina: ")
while len(cod) != 5 :
    cod = input("Digite pelo menos um código válido: ")

while (cod != 'FIM') and (qtd < 500) :
    qtd = qtd + 1
    nome = input("Digite o nome da disciplina: ")
    cHor = int(input("Digite a carga horária: "))
    while cHor < 1 :
        cHor = int(input("Digite uma carga horária válida: "))
    cred = int(input("Digite o número de créditos: "))
    while cred < 1 :
        cred = int(input("Digite um número de créditos válido: "))
    tab[cod] = (nome, cHor, cred)

    cod = input("Digite outro código, FIM para parar: ")
    while (cod != "FIM") and (len(cod) != 5) :
        cod = input("Digite um código válido ou FIM para parar: ")

if len(cod) == 5 :
    print("Quantidade máxima de disciplinas atingida, último valor foi descartado!")
    
prefixo = input("Digite um prefixo de disciplinas: ")
while len(prefixo) > 4 :
    prefixo = input("Digite um prefixo válido (tamanho < 5): ")
tamPref = len(prefixo)
qtd = 0
print("Disciplinas com códigos começando por", prefixo)

for cod in tab :
    if prefixo == cod[:tamPref] :
        print(" ", cod, tab[cod])
        qtd = qtd + 1
        media = media + tab[cod][1]

if qtd > 0 :
    media = media / qtd
    print("Selecionada(s)", qtd, "disciplinas(s) com média de carga horária", media)
else:
    print("Não existe nenhuma disciplina com esse prefixo")