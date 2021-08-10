# Ler 2 strings e dizer quantas vezes o primeiro aparece
# no segundo.

completo = input("Digite a string completa: ")
procura = input("Digite a string a ser contada: ")
qtd = 0
pos = completo.find(procura)
while pos != -1:
    qtd += 1
    pos = completo.find(procura, pos + 1)
print(qtd)