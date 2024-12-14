from gestion.zona import Zona
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio

class Animal:
    _totalAnimales = 0
    _zona = None

    def __init__(self, nom, edad, hab, gen):
        self._nombre = nom
        self._edad = edad
        self._habitat = hab
        self._genero = gen
        Animal._totalAnimales += 1

    def totalPorTipo(self):
        return f"Mamiferos: {len(Mamifero._listado)}\n Aves: {len(Ave._listado)}\n Reptiles: {len(Reptil._listado)}\n Peces: {len(Pez._listado)} \n Anfibios: {len(Anfibio._listado)}"
        