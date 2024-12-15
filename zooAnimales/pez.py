from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nom, edad, hab, gen, cEscamas, cAletas):
        super().__init__(nom, edad, hab, gen)
        self._colorEscamas = cEscamas
        self._cantidadAletas = cAletas
        Pez._listado.append(self)

    @classmethod
    def setListado(cls, list):
        Pez._listado = list

    @classmethod
    def getListado(cls):
        return Pez._listado
    
    def setColorEscamas(self, cEscamas):
        self._colorEscamas = cEscamas
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cAletas):
        self._cantidadAletas = cAletas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def movimiento(self):
        return "nadar"
    
    @classmethod
    def crearSalmon(cls, nom, edad, hab= "oceano", gen= None, cEscamas= "rojo", cAletas= 6):
        Pez(nom, edad, hab, gen, cEscamas, cAletas)
        Pez.salmones += 1

    @classmethod
    def crearBacalao(cls, nom, edad, hab= "oceano", gen= None, cEscamas= "gris", cAletas= 6):
        Pez(nom, edad, hab, gen, cEscamas, cAletas)
        Pez.bacalaos += 1

    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)