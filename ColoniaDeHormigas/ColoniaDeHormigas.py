__author__ = 'Santiago Mendoza Ramirez'

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


class RecorrerCoordenadas:
    def __init__(self):
        self.Ciudades = []
        self.MatrizDistancia = []
        self.MatrizDistanciaI = []
        self.MatrizFeromonas = []
        #Llenamos el array Ciudades con las coordenadas de cada ciudad provenientes del archivo
        with open('AgenteViajero.txt') as file:
                for line in file:
                    words = line.split()
                    x = ast.literal_eval(words[0])
                    y = ast.literal_eval(words[1])
                    #x = float(words[0])
                    #y = float(words[1])
                    p = Coordenadas(x, y)
                    self.Ciudades.append(p)
        self.CantCiudades=len(self.Ciudades) #Variable para saber el numero de ciudades del problema

        # Llenamos la matriz de distancia y la matriz de distancia inversa. Creamos la matriz de feromonas en 0 cada posicion
        # Utilizamos una array en el que cada miembro es a su vez otro array para crear las matrices.
        for i in self.Ciudades:
            DistanciaFila = []
            DistanciaFilaI = []
            FeromonasArray = []
            fila = self.Ciudades.index(i)
            CoordenadaPivote = self.Ciudades[fila]
            for j in self.Ciudades:
                col=self.Ciudades.index(j)
                DistanciaL = CoordenadaPivote.distance(self.Ciudades[col])
                DistanciaFila.append(DistanciaL)
                FeromonasArray.append(0)
                if DistanciaL == 0:
                    DistanciaFilaI.append(0)
                else:
                    DistanciaFilaI.append(1/DistanciaL)
        self.MatrizDistancia.append(DistanciaFilaI)
        self.MatrizDistanciaI.append(DistanciaFilaI)
        self.MatrizFeromonas.append(FeromonasArray)

    def HormigasExploradoras(self, numeroHormigas):
        j=0
        #Mandamos hormigas exploradoras: Hacen un recorrido aleatorio de todas las ciudades.
        #El numero de hormigas lo decide el usuario, es decir, es recibido en el "main".
        while(j<numeroHormigas):
            for i in range(0,self.CantCiudades):
                RecorridoHormiga = []
                ciudad = self.Ciudades(random.randint(0,self.CantCiudades))
                while(RecorridoHormiga.count(ciudad) != 0):
                    ciudad = self.Ciudades(random.randint(0,self.CantCiudades))
                RecorridoHormiga.append(ciudad)
            j+=1


