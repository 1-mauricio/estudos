def main():
    carro1 = Carro('brasilia', 1968, 'amarela', 80)
    carro2 = Carro('fusca', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, vel_max):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.vel = 0
        self.vel_max = vel_max

    def imprima(self):
        if self.vel == 0:
            print("%s %s %d"%(self.modelo, self.cor, self.ano)) #parado dá pra ver o ano
        elif self.vel < self.vel_max:
            print(f"{self.modelo} {self.cor} indo a {self.vel} Km/h")
        else:
            print(f"{self.modelo} {self.cor} indo muito raaaaapiiiiidoooooo")

    def acelere(self, vel):
        self.vel = vel
        if self.vel > self.vel_max:
            self.vel = self.vel_max
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()