class Zona:
    def __init__(self, nom, zoologico):
        self._nombre = nom
        self._zoo = zoologico
        self._animales = []
    
    def setNombre(self, nom):
        self._nombre = nom
    def getNombre(self):
        return self._nombre
    
    def setZoo(self, zoo):
        self._zoo = zoo
    def getZoo(self):
        return self._zoo
    
    def setAnimales(self, animales):
        self._animales = animales
    def getAnimales(self):
        return self._animales

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)