from gestion.zona import Zona

class Zoologico:
    def __init__(self, nom, ubi, zonas):
        self.nombre = nom
        self.ubicacion = ubi
        self.zonas = zonas
    
    def agregarZonas(self, zona):
        self.zonas = zona

    def cantidadTotalAnimales(self):
        pass