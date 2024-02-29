using System;
using System.Collections.Generic;

public class Biblioteca : IBiblioteca
{

    private List<Libro> catalogo;
    private List<Libro> librosPrestados;

    public Biblioteca()
    {
        catalogo = new List<Libro>();
        librosPrestados = new List<Libro>();

        Libro primerLibro = new Libro(
            1,
            "Cien años de soledad",
            "Gabriel Garcia Marquez",
            "1967");
        Libro segundoLibro = new Libro(
            1,
            "Homo Deus",
            "Yuval Noah Harari",
            "2015");


        // Agregar algunos libros al catálogo inicialmente
        catalogo.Add(primerLibro.Titulo,primerLibro);
        catalogo.Add(segumdoLibro.Titulo, primerLibro));
        catalogo.Add(new Libro("Don Quijote de la Mancha"));
    }

    // Método para mostrar el catálogo de libros
    public void MostrarCatalogo()
    {
        Console.WriteLine("Catálogo de libros:");
        foreach (var libro in catalogo)
        {
            Console.WriteLine(libro.Titulo + (libro.EnPrestamo ? " (En préstamo)" : ""));
        }

        public void Prestamo() { 

            Console.WriteLine("Prestamo de usuarios")
            Console.WriteLine("Escribe el id del libro que quieres prestar")
            Console.ReadLine()




        }
        public void IngresarComoUsuario()
        {
            Console.WriteLine("¡Bienvenido a la biblioteca!");
            Console.Write("Por favor, ingresa tu nombre: ");
            string nombreUsuario = Console.ReadLine();

            Usuario usuario = new Usuario(nombreUsuario);
            Console.WriteLine($"Hola {usuario.Nombre}, ¿en qué puedo ayudarte hoy?");
        }

        // Método para prestar un libro a un usuario
        public void PrestarLibro(Usuario usuario, Libro libro)
        {
            if (!libro.EnPrestamo)
            {
                libro.EnPrestamo = true;
                librosPrestados.Add(libro);
                Console.WriteLine($"El libro '{libro.Titulo}' ha sido prestado a {usuario.Nombre}.");
            }
            else
            {
                Console.WriteLine($"Lo siento, el libro '{libro.Titulo}' ya está en préstamo.");
            }
        }
    }

}
}
