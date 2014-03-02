import math
import random
import ast


class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, punto):
        ValorX = abs(self.x - punto.x)
        ValorY = abs(self.y - punto.y)
        formula = math.pow(ValorX, 2) + math.pow(ValorY, 2)
        return math.sqrt(formula)


class Viaje:
    def __init__(self):
        self.Ciudades = []
        self.Solucion = []
        self.SolucionPrima = []
        self.DistanciaTotal = 0.0
        self.DistanciaPrima = 0.0
        self.CantidadCiudades = 0
        with open('AgenteViajero.txt') as file:
            for line in file:
                words = line.split()
                x = ast.literal_eval(words[0])
                y = ast.literal_eval(words[1])
                #x = float(words[0])
                #y = float(words[1])
                p = Coordenadas(x, y)
                self.Ciudades.append(p)
                self.CantidadCiudades += 1

    def IniciarViaje(self):

        for i in range(0, len(self.Ciudades)):
            numero = random.randint(0, len(self.Ciudades)-1)
            while( self.Solucion.count(self.Ciudades[numero]) >= 1):
                numero = random.randint(0, len(self.Ciudades)-1)
            self.Solucion.append(self.Ciudades[numero])

    def PerturbarSolucion(self):
        posicion1 = random.randint(0, len(self.Ciudades)-1)
        posicion2 = random.randint(0, len(self.Ciudades)-1)
        while (posicion2 == posicion1):
            posicion2 = random.randint(0, len(self.Ciudades)-1)
        self.SolucionPrima = self.Solucion
        self.SolucionPrima[posicion1] = self.Solucion[posicion2]
        self.SolucionPrima[posicion2] = self.Solucion[posicion1]

    def DistanciaSolucionTotal(self):
        DistanciaSolucion = 0.0
        for i in range(0, (len(self.Ciudades))):
            DistanciaSolucion += self.Solucion[i].Distancia(self.Solucion[i + 1])
        return DistanciaSolucion

    def DistanciaSolucionPrima(self):
        DistanciaSolucion = 0.0
        for i in range(0, (len(self.Ciudades))):
            DistanciaSolucion += self.SolucionPrima[i].Distancia(self.SolucionPrima[i + 1])
        return DistanciaSolucion

    def Recorrido(self, Temperatura, TemperaturaFinal, alfa):
        ProbabilidadDeCambio = 0.0
        self.IniciarViaje()
        while (Temperatura < TemperaturaFinal):
            self.PerturbarSolucion()
            if (self.DistanciaSolucionPrima() < self.DistanciaSolucionTotal()):
                self.Solucion = self.SolucionPrima
                Temperatura = alfa * Temperatura
            else:
                NumeroAleatorio = random.uniform(0.0, 1.0)
                ProbabilidadDeCambio = math.exp(-(self.DistanciaSolucionTotal() - self.DistanciaSolucionPrima()) / Temperatura)
                if (NumeroAleatorio < ProbabilidadDeCambio):
                    self.Solucion = self.SolucionPrima
                    Temperatura = alfa * Temperatura
                    #Termina el While si Tf>T

    def ImprimirSolucion(self):
        for i in range(0, len(self.Ciudades)):
            print "[",self.Solucion[i].x,",",self.Solucion[i].y,"]"


if __name__ == "__main__":
    Temperatura = input("Digite la Temperatura Inicial: ")
    while (Temperatura <= 0):
        Temperatura = input("Digite la Temperatura Inicial: ")

    TemperaturaFinal = input("Digite la Temperatura Final: ")
    while (TemperaturaFinal <= 0):
        TemperaturaFinal = input("Digite la Temperatura Inicial: ")

    alfa = input("Digite el coeficiente de descenso de la temperatura: ")
    while (alfa >= 1 and alfa <= 0):
        alfa = input("Digite el coeficiente de descenso de la temperatura: ")

    ViajeAgente = Viaje()
    ViajeAgente.Recorrido(Temperatura, TemperaturaFinal, alfa)
    ViajeAgente.ImprimirSolucion()