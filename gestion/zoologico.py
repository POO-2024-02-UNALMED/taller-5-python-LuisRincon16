from gestion.zona import Zona

class Zoologico:
    _zonas = []

    def __init__(self, nom, ubi):
        self._nombre = nom
        self._ubicacion = ubi
    
    def setNombre(self, nom):
        self._nombre = nom
    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self, ubi):
        self._ubicacion = ubi
    def getUbicacion(self):
        return self._ubicacion
    
    @classmethod
    def setZonas(cls, newZona):
        cls._zonas = newZona
        
    @classmethod
    def getZonas(cls):
        return cls._zonas

    @classmethod
    def agregarZonas(cls, zona):
        cls._zonas.append(zona)

    @classmethod
    def cantidadTotalAnimales(cls):
        totalAnimales = 0
        for zona in cls._zonas:
            totalAnimales += zona.cantidadAnimales()
        return totalAnimales