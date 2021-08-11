should_continue = True
persons = []
while should_continue and len(persons) <= 300:
    cpf = float(input("Digite o CPF: "))
    if cpf < 0:
        should_continue = False
    else:
        current_person = {}
        current_person['cpf'] = cpf
        nome = input('Digite o seu nome: ')
        current_person['nome'] = nome
        current_person['salario'] = float(input("Digite o seu salario: "))
        persons.append(current_person)

is_correct = False
limite_inferior = 0
limite_superior = 0

while not is_correct:
    limite_inferior = float(input("Digite um limite inferior: "))
    limite_superior = float(input("Dgitie um limite superior: "))
    if limite_superior < 0 or limite_inferior < 0:
        print("Os limites devem ser positivos!")
    elif limite_superior < limite_inferior:
        print("O limite superior precisa ser maior que o inferior!")
    else:
        is_correct = True


maior_salario = 0
soma_salarios = 0
quantidade_pessoas = 0
aux_cont = 0


print("Se encontram neste intervalo: ")
for person in persons:
    if person['salario'] >= limite_inferior and person['salario'] <= limite_superior:
        print(person['nome'], person['cpf'], person['salario'])
        soma_salarios += person['salario']
        quantidade_pessoas += 1
        if person['salario'] > maior_salario:
            maior_salario = person['salario']

    if person['salario'] > limite_superior:
            aux_cont += 1

print(f"{aux_cont} pessoas recebem mais do que o limite superior.")
print(f"o maior salario vale R$: {maior_salario}")
print(f"a média dos salários é de R$: {soma_salarios/quantidade_pessoas}")