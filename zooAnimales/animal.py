from gestion.zona import Zona


class Animal:
    _totalAnimales = 0
    _zona = None

    def __init__(self, nom, edad, hab, gen):
        self._nombre = nom
        self._edad = edad
        self._habitat = hab
        self._genero = gen
        Animal._totalAnimales += 1

    @classmethod
    def setZona(cls, zona):
        cls._zona = zona

    @classmethod
    def getZona(cls):
        return cls._zona

    def setNombre(self, nom):
        self._nombre = nom
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, hab):
        self._habitat = hab 
    def getHabitat(self):
        return self._habitat

    def setGenero(self, gen):
        self._genero = gen
    def getGenero(self):
        return self._genero
    
    @classmethod
    def setTotalAnimales(cls, newTAnimales):
        cls._totalAnimales = newTAnimales
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return (f"Mamiferos: {len(Mamifero.getListado())}\n" f"Aves: {len(Ave.getListado())}\n" f"Reptiles: {len(Reptil.getListado())}\n" f"Peces: {len(Pez.getListado())}\n" f"Anfibios: {len(Anfibio.getListado())}")
    
    def toString(self):
        if self.getZona() is None:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"
        else:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona en la que me ubico es {self.getZona()}, en el {self.getZona().getZoo().getNombre()}"
        
    def movimiento(self):
        return "desplazarse"
        