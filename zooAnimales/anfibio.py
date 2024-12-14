from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nom, edad, hab, gen, cPiel, ven):
        super().__init__(nom, edad, hab, gen)
        self._colorPiel = cPiel
        self._venenoso = ven