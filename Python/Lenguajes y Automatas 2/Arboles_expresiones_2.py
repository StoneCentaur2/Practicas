#Prueba 2
class Nodo:
    def __init__(self, dato):
        self.Izquierda = None
        self.Derecha = None
        self.dato = dato

def insertar(raiz, nodo):
    if raiz == None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.Derecha == None:
                raiz.Derecha = nodo
            else:
                insertar(raiz.Derecha,nodo)
        else:
            if raiz.Izquierda == None:
                raiz.Izquierda = nodo
            else:
                insertar(raiz.Izquierda, nodo)
#Función Inorden
def Inorden (raiz):
    if raiz != None:
        Inorden(raiz.Izquierda)
        print(raiz.dato)
        Inorden(raiz.Derecha)
#Función Preorden
def Preorden(raiz):
    if raiz != None:
        print(raiz.dato)
        Preorden(raiz.Izquierda)
        Preorden(raiz.Derecha)
#Función Postorden
def Postorden(raiz):
    if raiz != None:
        Postorden(raiz.Izquierda)
        Postorden(raiz.Derecha)
        print(raiz.dato)

#Arbol de expresiones    
raiz = Nodo(10)
insertar(raiz, Nodo(10))
insertar(raiz, Nodo(9))

print("Inorden: ")
Inorden(raiz)
print("Preorden: ")
Preorden(raiz)
print("Postorden: ")
Postorden(raiz)

from collections import deque
 
# Estructura de datos para almacenar un nodo de árbol binario
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Función para verificar si un token dado es un operador
def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'
 
# Imprime la expresión sufijo para un árbol de expresión
def postorden(root):
    if root is None:
        return
    postorden(root.left)
    postorden(root.right)
    print(root.data, end='')

def Preorden(root):
     if root is None:
            return
     print(root.data, end='')
     Preorden(root.left)
     Preorden(root.right)
 
# Imprime la expresión infija de un árbol de expresiones
def inorden(root):
    if root is None:
        return
 
    # si el token actual es un operador, imprima paréntesis abierto
    if isOperator(root.data):
        print('(', end='')
 
    inorden(root.left)
    print(root.data, end='')
    inorden(root.right)
 
    # si el token actual es un operador, imprima cerrar paréntesis
    if isOperator(root.data):
        print(')', end='')
 
# Función para construir un árbol de expresión a partir de la expresión sufijo dada
def construct(postfix):
 
    # Caja base
    if not postfix:
        return
 
    # crea una stack vacía para almacenar punteros de árbol
    s = deque()
 
    # atravesar la expresión sufijo
    for c in postfix:
        # si el token actual es un operador
        if isOperator(c):
            # extrae dos nodos `x` e `y` de la stack
            x = s.pop()
            y = s.pop()
 
            # construye un nuevo árbol binario cuya raíz es el operador y cuya
            # Los niños izquierdo y derecho apuntan a `y` y `x`, respectivamente
            node = Node(c, y, x)
 
            # empuja el nodo actual a la stack
            s.append(node)
 
        # si el token actual es un operando, cree un nuevo nodo de árbol binario
        # cuya raíz es el operando y lo empuja a la stack
        else:
            s.append(Node(c))
 
    # un puntero a la raíz del árbol de expresión permanece en la stack
    return s[-1]
 
 
if __name__ == '__main__':
 
    postfix = 'ab+cde+c/b**'
    root = construct(postfix)

    print("Arbol a resolver: " + postfix)

    print('\nExpresion Inorden: ', end='')
    inorden(root)

    print('\nExpresion Preorden: ', end='')
    Preorden(root)
 
    print('Expresion Postorden: ', end='')
    postorden(root)