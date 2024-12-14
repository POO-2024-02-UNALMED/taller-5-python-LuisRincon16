class Zona:
    def __init__(self, nom, zoologico):
        self._nombre = nom
        self._zoo = zoologico
        self._animales = []
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)