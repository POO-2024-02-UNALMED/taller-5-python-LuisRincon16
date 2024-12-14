from gestion.zona import Zona

class Animal:
    _totalAnimales = 0
    _zona = None

    def __init__(self, nom, edad, hab, gen):
        self._nombre = nom
        self._edad = edad
        self._habitat = hab
        self._genero = gen
        