# CLASSE ABSTRATA : Não define a assinatura dos métodos

class FiguraGeometrica:
    def calculaArea(self):
        pass
    def calculaPerimetro(self):
        pass

from math import pi
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.__raio = raio
    
    def calculaArea(self):
        return pi*self.__raio*self.__raio

    def imprimeArea(self):
        return self.__raio


circulo = Circulo(10)
print(circulo.imprimeArea())