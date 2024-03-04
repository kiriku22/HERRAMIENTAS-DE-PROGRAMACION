from prestable import Prestable

class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libro_prestado = None

    @property
    def nombre(self):
        return self.__nombre

    @property
    def libro_prestado(self):
        return self.__libro_prestado

    def prestar_libro(self, libro):
        if isinstance(libro, Prestable):
            if libro.prestar():
                self.__libro_prestado = libro
                return True
        return False

    def devolver_libro(self):
        if self.__libro_prestado:
            self.__libro_prestado.devolver()
            self.__libro_prestado = None
            return True
        return False