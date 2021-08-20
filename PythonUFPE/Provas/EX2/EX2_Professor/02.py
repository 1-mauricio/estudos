def serieR(n, num1=105, num2=-130, den=25.0, pos=1):
    # Parâmetro den definido como float para funcionar também em Python 2
    if pos == 1:  # Termos ímpares (positivos)
        res = num1 / den
    else:
        res = num2 / den
    if n > 1:  # Caso geral -> recursão
        if pos == 1:
            res = res + serieR(n - 1, num1 + 35, num2, den + 10, 2)
        else:
            res = res + serieR(n - 1, num1, num2 - 30, den + 10, 1)
    return res
