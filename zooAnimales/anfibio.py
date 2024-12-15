from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nom, edad, hab, gen, cPiel, ven):
        super().__init__(nom, edad, hab, gen)
        self._colorPiel = cPiel
        self._venenoso = ven
        Anfibio._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado
    
    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls, nom, edad, hab= "selva", gen= None, cPiel= "rojo", ven= True):
        Anfibio(nom, edad, hab, gen, cPiel, ven)
        Anfibio.ranas += 1

    @classmethod
    def crearSalamandra(cls, nom, edad, hab= "selva", gen= None, cPiel= "negro y amarillo", ven= False):
        Anfibio(nom, edad, hab, gen, cPiel, ven)
        Anfibio.salamandras += 1

    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)