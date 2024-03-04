from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def mostrar_menu(usuario):
    print("\nMenú de opciones:")
    print("1. Mostrar catálogo de libros")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Cambiar de usuario")
    print("5. Salir")
    print(f"\nUsuario actual: {usuario.nombre}")

def mostrar_catalogo(biblioteca):
    print("\nCatálogo de libros:")
    for i, libro in enumerate(biblioteca.catalogo, start=1):
        print(f"{i}. {libro.titulo} - {libro.autor} ({'Disponible' if libro.disponible else 'No disponible'})")

def prestar_libro(biblioteca, usuario):
    mostrar_catalogo(biblioteca)
    try:
        opcion = int(input("\nSeleccione el número de libro que desea prestar (0 para cancelar): "))
        if opcion == 0:
            return
        elif opcion < 1 or opcion > len(biblioteca.catalogo):
            print("Opción inválida. Intente de nuevo.")
            return
        libro_elegido = biblioteca.catalogo[opcion - 1]

        if biblioteca.prestar_libro(libro_elegido.titulo, usuario):
            print(f"'{libro_elegido.titulo}' prestado a {usuario.nombre}")
        else:
            print(f"No se pudo prestar '{libro_elegido.titulo}' a {usuario.nombre}")
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")

def devolver_libro(biblioteca, usuario):
    libro_prestado = usuario.libro_prestado
    if libro_prestado:
        print(f"\nDevolviendo '{libro_prestado.titulo}' prestado por {usuario.nombre}...")
        if biblioteca.devolver_libro(libro_prestado.titulo):
            print(f"'{libro_prestado.titulo}' devuelto correctamente")
        else:
            print(f"No se pudo devolver '{libro_prestado.titulo}'")
    else:
        print("\nNo tiene ningún libro prestado.")

# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Crear algunos libros
libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling")

# Agregar los libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Juan")
usuario2 = Usuario("María")

usuarios = [usuario1, usuario2]
usuario_actual = usuario1  # Comenzamos con el usuario1

while True:
    mostrar_menu(usuario_actual)
    try:
        opcion = int(input("\nSeleccione una opción: "))
        if opcion == 1:
            mostrar_catalogo(biblioteca)
        elif opcion == 2:
            prestar_libro(biblioteca, usuario_actual)
        elif opcion == 3:
            devolver_libro(biblioteca, usuario_actual)
        elif opcion == 4:
            print("Seleccione el usuario:")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. {usuario.nombre}")
            seleccion_usuario = int(input("Seleccione el número de usuario: "))
            if seleccion_usuario < 1 or seleccion_usuario > len(usuarios):
                print("Usuario inválido. Intente de nuevo.")
            else:
                usuario_actual = usuarios[seleccion_usuario - 1]
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Intente de nuevo.")