def media(nome, peso1=1, peso2=1):
    nota1 = float(
        input('Digite primeira nota (0 a 10) do aluno ' + nome + ': '))
    while (nota1 < 0) or (nota1 > 10):
        nota1 = float(input('Primeira nota inválida. Digite novamente': '))

    nota2 = float(
        input('Digite segunda nota (0 a 10) do aluno ' + nome + ': '))
    while (nota2 < 0) or (nota2 > 10):
        nota2 = float(input('Segunda nota inválida. Digite novamente: '))

    media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    if media >= 7:
        sit = 'está aprovado.'
    elif media < 3:
        sit = 'está reprovado.'
    else:
        sit = 'fará prova final.'


print('O aluno %s obteve média %.2f e %s' % (nome, media, sit))
