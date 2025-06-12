$(document).ready (function(){
    habilitar();
    deshabilitar();
});

$('p').dblclick(function(){
    $(this).hide(1000);
});

$("#ocultar").click(function(){
    $('.esconder').hide(1000);
});

$('#agregar').click(function(){
    //Primera lista
    var posicion = $('ul li').length +1;
    $('<li>Elemento ' + posicion + '</li>').appendTo('ul').fadeIn();
    //segunda lista
    var posicion = $('ol li').length +1;
    $('<li>Elemento ' + posicion + '</li>').appendTo('ol').fadeIn();
});

$('#eliminar').bind('click', function(){
    $('ul li:last-child').remove();
    $('ol li:last-child').remove();
});

function habilitar (){
    //Primera lista
    $('ul li').hover(function(){
        $(this).addClass('rojo');
    });

    //Segunda lista
    $('ol li').hover(function(){
        $(this).addClass('rojo');
    });
};

function deshabilitar (){
    //Primera lista
    $('ul li').mouseout(function(){
        $(this).removeClass('rojo');
    });

    //Segunda lista
    $('ol li').mouseout(function(){
        $(this).removeClass('rojo');
    });
};
