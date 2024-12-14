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
    def getListado(cls):
        return cls._listado
