// Función que se ejecuta al presionar el botón "Sumar"
function sumarNumeros() {
    // Obtener los valores de los números ingresados por el usuario
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);
    
    // Calcular la suma de los números ingresados
    var resultado = num1 + num2;
    
    // Mostrar el resultado en la página en el div
    document.getElementById("resultado").innerHTML = "La operación: " + num1 + " + " + num2 + " = " + resultado;
  };  