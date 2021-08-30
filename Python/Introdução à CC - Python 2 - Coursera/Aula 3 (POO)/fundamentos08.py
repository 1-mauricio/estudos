#objeto = dados + codigo
# - encapsulamento
#classes
# - definem os tipos de objetos
# - definem quais os dados e o código dos objetos
#dados => atributos ; codigo => métodos
#os objetos são chamados de instâncias das classes
class Carro:
    pass
meu_carro = Carro()
carro_do_joao = Carro()
print(meu_carro)
print(carro_do_joao)

meu_carro.ano = 1968
meu_carro.modelo = "Fusca"
meu_carro.cor = "azul"
print(meu_carro.cor)

carro_do_joao.ano = 1981
carro_do_joao.modelo = "Brasília"
carro_do_joao.cor = "amarelo"
print(carro_do_joao.modelo)

novo_fusca = meu_carro
novo_fusca.ano += 10
print(novo_fusca.ano)
print(meu_carro.ano)