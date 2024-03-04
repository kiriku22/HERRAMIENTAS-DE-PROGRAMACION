from biblioteca_interface import BibliotecaInterface

class Biblioteca(BibliotecaInterface):
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                return libro
        return None

    def prestar_libro(self, titulo, usuario):
        libro = self.buscar_libro(titulo)
        if libro and libro.disponible:
            if usuario.prestar_libro(libro):
                return True
        return False

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and not libro.disponible:
            libro.devolver()
            return True
        return False