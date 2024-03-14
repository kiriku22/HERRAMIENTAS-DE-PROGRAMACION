
  // Función para validar el formulario
  function validarFormulario() {
    var nombre = document.getElementById("nombre").value.trim();
    var correo = document.getElementById("correo").value.trim();
    var mensaje = document.getElementById("mensaje").value.trim();

    // Verificar si los campos están vacíos o si el correo es inválido
    if (!nombre || !correo || !mensaje || !/\S+@\S+\.\S+/.test(correo)) {
      alert("Por favor, complete todos los campos del formulario y asegúrese de que el correo electrónico sea válido.");
      return false;
    }

    // Si todo está bien, enviar el formulario
    alert("Formulario enviado con éxito.");
    return true;
  }