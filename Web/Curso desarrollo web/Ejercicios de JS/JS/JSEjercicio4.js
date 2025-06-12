function esPalindromo(texto) {
    // Convertimos el texto a minúsculas y eliminamos los espacios en blanco
    texto = texto.toLowerCase().replace(/\s/g, '');

    // Obtenemos el texto invertido
    var texto_invertido = texto.split('').reverse().join('');

    // Verificamos si el texto original y el invertido son iguales
    if (texto == texto_invertido) {
        return true;
    } else {
        return false;
    }
}
//Evaluaremos sí es o no polindromo
function evaluarPalindromo() {
    var texto = document.getElementById('texto').value;
    //decisión de si es o no polindromo
    if (esPalindromo(texto)) {
        document.getElementById('resultado').innerHTML = "Es un palíndromo";
    } else {
        document.getElementById('resultado').innerHTML = "No es un palíndromo";
    }
    //aquí contamos la longitud del texto
    document.getElementById('longitud').innerHTML = "Longitud del texto: " + texto.length;
    //aquí colocamos el texto normal
    document.getElementById('texto_original').innerHTML = "Texto original: " + texto;
    //aquí colocamos el texto invertido
    document.getElementById('texto_invertido').innerHTML = "Texto invertido: " + texto.split('').reverse().join('');
}