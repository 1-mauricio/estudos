def media(nome, peso1 = 1, peso2 = 1):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1*peso1 + nota2*peso2) / (peso1 + peso2)

    if media >= 7:
        resultado = "está aprovado."
    elif media < 3 :
        resultado = "está reprovado."
    elif media < 7 and media >= 3:
        resultado = "fará prova final."

    print(f"O aluno {nome} obteve média {media} e {resultado}")


nome = input("Digite o nome do aluno: ")
p1 = float(input("Digite o peso da primeira prova (digite 0 ou negativo para usar o padrão[1]):"))
if p1 > 0:
    p2 = float(input("Digite o peso da segunda prova:"))
    media(nome, p1, p2)
else:
    media(nome)
