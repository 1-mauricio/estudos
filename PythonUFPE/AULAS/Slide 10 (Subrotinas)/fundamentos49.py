# Faça um programa que recebe do usuário duas strings. Em seguida, escreva uma função que recebe essas duas strings como parâmetro e retorna True/False informando se elas são um anagrama. Letras maiúsculas e minúsculas devem ser tratadas da mesma maneira. Ao final do programa, imprima a seguinte mensagem:
# - A palavra "string1" é um anagrama de "string2" (se for um anagrama)
# - A palavra "string1" não é um anagrama de "string2" (se não for um anagrama)

def anagrama(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    dic = {}
    for s in s1:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1

    i = 0
    anag = True
    while i < len(s2):
        if (s2[i] in dic) and (dic[s2[i]] > 0):
            dic[s2[i]] -= 1
        else:
            anag = False
        i += 1

    return anag

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
if anagrama(palavra1, palavra2):
    print(f"A palavra {palavra1} é um anagrama de {palavra2}")
else:
    print(f"A palavra {palavra1} NÃO é um anagrama de {palavra2}")