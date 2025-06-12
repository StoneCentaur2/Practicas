// Ejemplo de setInterval()
let contador = 0;

let intervalo = setInterval(function() {
  contador++;
  console.log(contador);
}, 1000); // Se ejecuta cada 1000 milisegundos (1 segundo)

// Ejemplo de setTimeout()
setTimeout(function() {
  console.log("Este mensaje se muestra después de 5 segundos");
}, 5000); // Se ejecuta después de 5000 milisegundos (5 segundos)
