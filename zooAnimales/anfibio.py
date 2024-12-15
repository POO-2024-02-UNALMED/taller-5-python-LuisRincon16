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
    def setListado(cls, list):
        Anfibio._listado = list

    @classmethod
    def getListado(cls):
        return Anfibio._listado
    
    def setColorPiel(self, cPiel):
        self._colorPiel = cPiel
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, ven):
        self._venenoso = ven
    def isVenenoso(self):
        return self._venenoso
    
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