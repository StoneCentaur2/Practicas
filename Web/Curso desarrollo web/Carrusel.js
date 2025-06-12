    var imagenes =[
        'star wars 1.jpg', 
        'star wars 2.jpeg', 
        'star wars 3.jpg'];
//Mostrar la primera imagen
document.Imagen.src = imagenes[0];
//variables para los botones y un contador
var SliderRight = document.querySelector('.Btn_Next');
var SliderPrev = document.querySelector('.Btn_Prev');
var Cont = 0;
// función para pasar a la siguiente image
function MoveNext() {
    Cont++;
    if (Cont > imagenes.length -1) {
        Cont = 0;
    }
    document.Imagen.src = imagenes[Cont];
}
// variable para el tiempo que pasará antes de cambiar de image
var Interval = setInterval(MoveNext, 3000);
// función para cuando hagan click actualizar el contador
SliderRight.addEventListener('click', function() 
 {
    clearInterval(Interval);
    MoveNext();
    Interval = setInterval(MoveNext, 3000);
});
// función para pasar al anterior image
function MovePrev() {
    Cont--;
    if (Cont < 0) {
        Cont = imagenes.length -1;
    }
    document.Imagen.src = imagenes[Cont];
}
// función para cuando hagan click actualizar el contador
SliderPrev.addEventListener('click', function() 
 {
    clearInterval(Interval);
    MovePrev();
    Interval = setInterval(MovePrev, 3000);
 });