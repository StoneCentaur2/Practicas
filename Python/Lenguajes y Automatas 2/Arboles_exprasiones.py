from collections import deque
 
# Estructura de datos para almacenar un nodo del árbol
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
# Función para verificar si un token dado es un operador
def Operador(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'
 
# Realiza la expresión en Postorden
def postorden(root):
    if root is None:
        return
    postorden(root.left)
    postorden(root.right)
    print(root.data, end='')

# Realiza la expresión en Preorden
def preorden(root):
     if root is None:
            return
     print(root.data, end='')
     preorden(root.left)
     preorden(root.right)
 
# Realiza la expresión en Inorden
def inorden(root):
    if root is None:
        return
 
    if Operador(root.data):
        print('(', end='')
 
    inorden(root.left)
    print(root.data, end='')
    inorden(root.right)
 
    if Operador(root.data):
        print(')', end='')
 
def construct(postfix):
    if not postfix:
        return
    s = deque()

    for c in postfix:
        if Operador(c):
            x = s.pop()
            y = s.pop()
            node = Node(c, y, x)
            s.append(node)

        else:
            s.append(Node(c))
    return s[-1]
  
if __name__ == '__main__':
 
    postfix = 'ab+cde+c/b**'
    root = construct(postfix)

    print("Arbol a resolver: " + postfix)

    print('Expresion en Inorden: ', end='')
    inorden(root)

    print('\nExpresion en Preorden: ', end='')
    preorden(root)
 
    print('\nExpresion en Postorden: ', end='')
    postorden(root)