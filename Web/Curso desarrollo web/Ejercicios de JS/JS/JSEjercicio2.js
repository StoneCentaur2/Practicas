//funcion para realizar toda la operación
function calcularFactorial() {
    var num = document.getElementById("numero").value; //llamamos la variable del input
    var res = 1;
    //declaración de las variables para usar en el for
    for (var i = 1; i <= num; i++) {
      res *= i;
    }
    /*al terminar el recorrido de for, mandamos a imprimir el resultado en el html
    usamos el id de resultado para imprimir el mismo */
    document.getElementById("resultado").innerHTML = "El resultado del factorial es: " + res;
};