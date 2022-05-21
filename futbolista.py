from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, años, goles, tarjetasR, pierna):
        Persona.__init__(self,  nombre, edad, altura, sexo)
        Deportista.__init__(self, años)
        self._golesMarcados = goles
        self._tarjetasRojas = tarjetasR
        self._piernaHabil = pierna
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self,x):
        self._golesMarcados = x

    def setTarjetasRojas(self,x):
        self._tarjetasRojas = x

    def setPiernaHabil(self,x):
        self._piernaHabil = x

    def __str__(self):
        salida = "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre,self.getDeporte,str(self.getEdad),str(self.getAñosPracticando))
        return salida

