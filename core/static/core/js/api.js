const selectElement = document.getElementById("regiones");

// Realizar una solicitud GET a la API
fetch("https://api.shipit.cl/v/regions")
  .then(response => response.json())
  .then(data => {
    // Iterar sobre los datos recibidos de la API
    data.forEach(region => {

      const option = document.createElement("option");
      option.value = region.id;
      option.text = region.name;
      // Agregar la opción al elemento select
      selectElement.appendChild(option);
    });
  })
  .catch(error => {
    console.error("Error al obtener las regiones:", error);
  });