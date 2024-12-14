from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nom, edad, hab, gen, pelaje, patas):
        super().__init__(nom, edad, hab, gen)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado
