#Un palindromo que devuelve verdadero si es palindromo y falso en caso de que no
def palindromo(txt: str):
    txt = txt.replace(' ', '').lower()
    return txt == txt[::-1]

txt1 = 'anita lava la tina'
txt2 = 'Reversa en chino'

print(palindromo(txt1))