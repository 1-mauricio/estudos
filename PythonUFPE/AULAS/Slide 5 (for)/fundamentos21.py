#Questão que verifica se uma string S é um palindromo

S = input("Digite uma palavra ou um número: ")
tamanho = len(S)
direita = len(S)-1
palindromo = True
for esquerda in range (0, tamanho//2):
    if S[esquerda] != S[direita]:
        palindromo = False
    direita -= 1

if palindromo: 
    print(f"A string {S} é um palíndromo.")
else:
    print(f"A string {S} não é um palíndromo.")
