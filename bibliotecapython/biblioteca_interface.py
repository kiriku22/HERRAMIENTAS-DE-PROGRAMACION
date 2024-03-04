from abc import ABC, abstractmethod

class BibliotecaInterface(ABC):
    @abstractmethod
    def agregar_libro(self, libro):
        pass

    @abstractmethod
    def buscar_libro(self, titulo):
        pass

    @abstractmethod
    def prestar_libro(self, titulo, usuario):
        pass

    @abstractmethod
    def devolver_libro(self, titulo):
        pass