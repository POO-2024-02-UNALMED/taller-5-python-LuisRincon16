from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nom, edad, hab, gen, cEscamas, lCola):
        super().__init__(nom, edad, hab, gen)
        self._colorEscamas = cEscamas
        self._largoCola = lCola
        Reptil._listado.append(self)

    @classmethod
    def setListado(cls, list):
        Reptil._listado = list

    @classmethod
    def getListado(cls):
        return Reptil._listado
    
    def setColorEscamas(self, cEscamas):
        self._colorEscamas = cEscamas
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, lCola):
        self._largoCola = lCola
    def getLargoCola(self):
        return self._largoCola
    
    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nom, edad, hab= "humedal", gen= None, cEscamas= "verde", lCola= 3):
        Reptil(nom, edad, hab, gen, cEscamas, lCola)
        Reptil.iguanas += 1

    @classmethod
    def crearSerpiente(cls, nom, edad, hab= "jungla", gen= None, cEscamas= "blanco", lCola= 1):
        Reptil(nom, edad, hab, gen, cEscamas, lCola)
        Reptil.serpientes += 1

    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)