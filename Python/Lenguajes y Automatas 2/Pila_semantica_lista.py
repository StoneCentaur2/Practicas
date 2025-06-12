from collections import deque
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def Operador(c):    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'
def inorden(root):
    if root is None:        return
    inorden(root.left)
    print(root.data, end='')
    inorden(root.right)
def construct(postfix):
    if not postfix:        return
    s = deque()
    for c in postfix:
        if Operador(c):
            x = s.pop()
            y = s.pop()
            node = Node(c, y, x)
            s.append(node)
        else:   s.append(Node(c))
    return s[-1]
if __name__ == '__main__':
    postfix = input('ingresar operacion: ')
    root = construct(postfix)
    print('Expresion en Inorden: ', end='')
    inorden(root)