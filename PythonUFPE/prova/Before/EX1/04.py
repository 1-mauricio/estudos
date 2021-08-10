should_continue = True
quantidade_alunos = 0
alunos = {}

while should_continue and quantidade_alunos < 200:
    matricula = int(input("Digite a matrícula: "))
    if matricula < 0:
        should_continue = False
    else:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        alunos[str(matricula)] = {'nome': nome, 'idade': idade}
        quantidade_alunos += 1

intervalos = int(input("Digite o número de intervalos: "))

for current in range(intervalos):
    idade_minima = 0
    idade_maxima = 0
    count = 0
    limite_inferior = int(input("Digite o limite inferior: "))
    limite_superior = int( input("Digite o limite superior: "))
    if limite_superior < limite_superior:
        print("O limite superior deve ser maior que o inferior")
    else: 
        for matricula in alunos.keys():
            aluno = alunos[matricula]
            if aluno['idade'] >= limite_inferior and aluno['idade'] <= limite_superior:
                count += 1
                if aluno['idade'] > idade_maxima: idade_maxima = aluno['idade']
                if aluno['idade'] < idade_minima: idade_minima = aluno ['idade']
                print('nome: {}, idade: {}'.format(aluno['nome'], aluno['idade']))

        print(f"A idade mínima para o intervalo é de {idade_minima}")
        print(f"A idade máxima para o intervalo é de {idade_maxima}")
        print(f'Existem {count} alunos no intervalo')
