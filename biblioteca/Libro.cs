class Libro
{
    public string Titulo { get; set; }
    public string Autor { get; set; }
    public string Año { get; set; }
    public int Id { get; set; }
    public bool EnPrestamo { get; set; }

    public Libro(int id,string titulo,string autor,string año  )
    {
        Id = id;
        Titulo = titulo;
        Autor = autor;
        Año = año;
        EnPrestamo = false;
    }
}
