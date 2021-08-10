

nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("A nota digitada deve estar no intervalo [0,10].")

else:
    if nota < 3:
        print("Aluno reprovado.")
    elif nota >= 3 and nota < 7:
        print("Aluno vai para final.")
    else:
        print("Aluno aprovado")



