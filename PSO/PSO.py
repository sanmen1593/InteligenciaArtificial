__author__ = 'Santiago'

import math
import random

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, punto):
        ValorX = abs(self.x - punto.x)
        ValorY = abs(self.y - punto.y)
        formula = math.pow(ValorX, 2) + math.pow(ValorY, 2)
        return math.sqrt(formula)

class PSO:
    def __init__(self,cantidad_particulas, c1, cmax,iteraciones):
        self.VectorParticulas = []
        self.MejorPosicionParticula = []
        self.VelocidadParticulaX = []
        self.VelocidadParticulaY = []
        self.MejorPosicionEnjambre = Punto(6,6)
        self.xmin = -5
        self.xmax = 5
        self.ymin = -5
        self.ymax = 5
        self.CantidadParticulas = cantidad_particulas
        self.iteraciones = iteraciones
        self.c1 = c1
        self.cmax = cmax

    def PosicionesIniciales(self,cantidad_particulas):
        for i in range(0,cantidad_particulas):
            pos_x = self.xmin + ((self.xmax - self.xmin)*random.uniform(0,1))
            pos_y = self.ymin + ((self.ymax - self.ymin)*random.uniform(0,1))
            punto = Punto(0,0)
            punto.x = pos_x
            punto.y = pos_y
            self.VectorParticulas.append(punto)
            self.MejorPosicionParticula.append(punto)
            self.VelocidadParticulaX.append(0)
            self.VelocidadParticulaY.append(0)

    def FuncionObjetivo(self, punto):
        aptitud = 20 + math.pow(punto.x, 2) + math.pow(punto.y,2) - (10*((math.cos(2*math.pi*punto.x))+(math.cos(2*math.pi*punto.y))))
        return aptitud

    def CalcularAptitud(self):
        mejor_aptitud = 1000000000
        for i in range(0,len(self.VectorParticulas)):
            ValorAptitud = self.FuncionObjetivo(self.VectorParticulas[i])
            if(ValorAptitud < self.FuncionObjetivo(self.MejorPosicionParticula[i])):
                self.MejorPosicionParticula[i] = self.VectorParticulas[i]
            if(ValorAptitud < self.FuncionObjetivo(self.MejorPosicionEnjambre)):
                self.MejorPosicionEnjambre = self.VectorParticulas[i]

    def ActualizarPosicion(self):
        for i in range(0,len(self.VectorParticulas)):
            velocidadx = self.c1*self.VelocidadParticulaX[i] + (self.cmax*random.uniform(0,1)*(self.MejorPosicionParticula[i].x - self.VectorParticulas[i].x)) + (self.cmax*random.uniform(0, 1)*(self.MejorPosicionEnjambre.x - self.VectorParticulas[i].x))
            velocidady = self.c1*self.VelocidadParticulaY[i] + (self.cmax*random.uniform(0,1)*(self.MejorPosicionParticula[i].y - self.VectorParticulas[i].y)) + (self.cmax*random.uniform(0, 1)*(self.MejorPosicionEnjambre.y - self.VectorParticulas[i].y))
            nuevax = self.VectorParticulas[i].x + velocidadx
            nuevay = self.VectorParticulas[i].y + velocidady
            point = Punto(nuevax,nuevay)
            self.VelocidadParticulaX[i] = velocidadx
            self.VelocidadParticulaY[i] = velocidady
            self.VectorParticulas[i] = point

    def FueraDelEspacio(self):
        for i in range(0,len(self.VectorParticulas)):
                if(self.VectorParticulas[i].x > self.xmax):
                    self.VectorParticulas[i].x = self.xmax
                elif(self.VectorParticulas[i].x < self.xmin):
                    self.VectorParticulas[i].x = self.xmin
                elif(self.VectorParticulas[i].y > self.ymax):
                    self.VectorParticulas[i].y = self.ymax
                elif(self.VectorParticulas[i].y < self.ymin):
                    self.VectorParticulas[i].y = self.ymin

    def AlgoritmoPSO(self):
        a=0
        while(a<self.iteraciones):
            self.PosicionesIniciales(self.CantidadParticulas)
            self.CalcularAptitud()
            self.ActualizarPosicion()
            self.FueraDelEspacio()
            a+=1
        return self.MejorPosicionEnjambre

if __name__ == "__main__":
    variable = PSO(10, 0.729, 2.05, 500)
    Puntico = variable.AlgoritmoPSO()
    print(variable.FuncionObjetivo(Puntico))
    print(Puntico.x)
    print(Puntico.y)


