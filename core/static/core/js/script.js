// Espera a que el documento HTML esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
  // Obtén todos los elementos de la clase "card-text"
  var descripciones = document.getElementsByClassName('card-text');

  // Itera sobre cada elemento de descripción
  for (var i = 0; i < descripciones.length; i++) {
    var descripcion = descripciones[i];
    var botonMostrar = document.createElement('button');
    botonMostrar.textContent = 'Mostrar descripción';
    botonMostrar.classList.add('btn');
    botonMostrar.classList.add('btn-sm');
    botonMostrar.classList.add('btn-primary');
    botonMostrar.addEventListener('click', function() {
      var descripcion = this.parentNode.querySelector('.card-text');
      if (descripcion.style.display === 'none') {
        descripcion.style.display = 'block';
        this.textContent = 'Ocultar descripción';
      } else {
        descripcion.style.display = 'none';
        this.textContent = 'Mostrar descripción';
      }
    });

    // Inserta el botón antes de la descripción
    descripcion.parentNode.insertBefore(botonMostrar, descripcion);
    descripcion.style.display = 'none';
  }
});