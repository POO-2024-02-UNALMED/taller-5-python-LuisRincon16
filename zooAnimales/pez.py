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