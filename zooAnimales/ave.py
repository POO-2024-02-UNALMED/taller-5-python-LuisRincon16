from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nom, edad, hab, gen, cPlumas):
        super().__init__(nom, edad, hab, gen)
        self._colorPlumas = cPlumas
        Ave._listado.append(self)

    @classmethod
    def getListado(cls):
        return cls._listado
    
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearHalcon(cls, nom, edad, hab= "montanas", gen= None, cPlumas= "cafe glorioso"):
        Ave(nom, edad, hab, gen, cPlumas)
        Ave.halcones += 1

    @classmethod
    def crearAguila(cls, nom, edad, hab= "montanas", gen= None, cPlumas= "blanco y amarillo"):
        Ave(nom, edad, hab, gen, cPlumas)
        Ave.halcones += 1

    @classmethod
    def cantidadAves(cls):
        return len(Ave._listado)