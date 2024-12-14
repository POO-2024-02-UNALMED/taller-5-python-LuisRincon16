from gestion.zona import Zona

class Zoologico:
    def __init__(self, nom, ubi, zonas):
        self._nombre = nom
        self._ubicacion = ubi
        self._zonas = zonas
    
    def agregarZonas(self, zona):
        self._zonas = zona

    def cantidadTotalAnimales(self):
        pass