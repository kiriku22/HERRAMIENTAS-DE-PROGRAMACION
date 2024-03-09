document.addEventListener('DOMcontentLoaded', function(){
const formularioLibros=document.getElementById('formularioLibro');
const formularioTabla=document.getElementById('formulariotabla');

formularioLibros.addEventListener('submit',function(event) {

    event.defaultPrevented();
    const tituloLibro=document.getElementById('titulolibro');
    
    const autorLibro=document.getElementById('autor');
    
    const editorialLibro=document.getElementById('editorial');

    const categoriaLibro=document.getElementById('categoria');
    
    const fechaLibro=document.getElementById('fecha');
    
    


    const libro={
        tituloLibro:titulolibro,
        autor:autor,
        editorial:editorial,
        categoria:categoria,
        fecha:fecha

    };
    librosRegistrados.push(libro);
    agregarLibro();
});

function agregarLibro(){
    filaTabla.innerHTML='';

    librosRegistrados.forEach(function(Libro,indice){

        const fila=`  
        <tr>
            <td>${Libro.tituloLibro}</td>
            <td>${Libro.autor}</td>
            <td>${Libro.editorial}</td>
            <td>${Libro.categoria}</td>
            <td>${Libro.fecha}</td>
        </tr>
    `;
    filaTabla.innerHTML += fila;
    });
  
}

})   
