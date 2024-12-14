from gestion.zona import Zona

class Zoologico:
    _zonas = []

    def __init__(self, nom, ubi):
        self._nombre = nom
        self._ubicacion = ubi
    
    @classmethod
    def agregarZonas(cls, zona):
        cls._zonas.append(zona)

    @classmethod
    def cantidadTotalAnimales(cls):
        totalAnimales = 0
        for zona in cls._zonas:
            totalAnimales += zona.cantidadAnimales()
        return totalAnimales