class Persona():
    
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo



    #metodos get y set
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getAltura(self):
        return self._altura

    def getSexo(self):
        return self._sexo

    def setNombre(self, x):
        self._nombre = x

    def setEdad(self, x):
        self._edad = x

    def setAltura(self, x):
        self._altura = x

    def setSexo(self, x):
        self._sexo = x