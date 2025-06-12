jugar :- como_jugar, jugardela([a,a,a,a,a,a,a,a,a]).

jugardela(Tabla) :- gana(Tabla, x), write('Tu ganaste').
jugardela(Tabla) :- gana(Tabla, o), write('IA gano').
jugardela(Tabla) :- read(N),
        xmovimiento(Tabla, N, NuevaTabla),
        mostrar(NuevaTabla),
        oresponder(NuevaTabla, NuevaNuevaTabla),
        mostrar(NuevaNuevaTabla),
        jugardela(NuevaNuevaTabla).

enfila([1,2,3]).
enfila([4,5,6]).
enfila([7,8,9]). % Gana en fila

encolumna([1,4,7]).
encolumna([2,5,8]).
encolumna([3,6,9]). % Gana en columna

endiagonal([1,5,9]).
endiagonal([3,5,7]). % Gana en diagonal

gana(Tabla, Jugador) :- genfila(Tabla, Jugador);
            encolumna(Tabla, Jugador);
            endiagonal(Tabla, Jugador).

enfila(Tabla, Jugador) :-
        Tabla = (Jugador, Jugador,Jugador,_,_,_,_,_,_);
        Tabla = (_,_,_,Jugador, Jugador,Jugador,_,_,_);
        Tabla = (_,_,_,_,_,_,Jugador, Jugador,Jugador).

encolumna(Tabla, Jugador) :-
        Tabla = (Jugador,_,_, Jugador,_,_,Jugador,_,_);
        Tabla = (_,Jugador,_,_, Jugador,_,_,Jugador,_);
        Tabla = (_,_,Jugador,_,_, Jugador,_,_,Jugador).

endiagonal(Tabal, Jugador) :-
        Tabla = (Jugador,_,_,_, Jugador,_,_,_,Jugador);
        Tabla = (_,_,Jugador,_,Jugador,_,Jugador,_,_).
