def pagamento_semanal(valor_por_hora, num_horas = 40):
    assert valor_por_hora >= 0 and num_horas > 0
    #verifica a execução de uma condição qualquer
    return valor_por_hora * num_horas

try:
    valor = int(input("Digite o valor por hora: "))
    horas = int(input("Digite a quantidade de horas: "))
    print(pagamento_semanal(valor, horas))
except AssertionError:
    print("Erro de Assert, os valores precisam ser positivos")