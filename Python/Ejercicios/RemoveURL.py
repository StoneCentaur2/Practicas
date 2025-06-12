links = [
    'www.google.com',
    'www.YouTube.com',
    'www.wikipedia.com',
    'www.facebook.store',
    'www.wikihouse.com',
    'https://www.twitter.com',
    'http://www.store.com',
    'https://www.com.com.store',
    'http://www.comercio.store',
    'https://www.uabc.org',
    'https://youtube.com/shorts/-rdlxFKrxOo?feature=share',
]
# Intento de poner todos los posibles terminos en un ciclo y no ponerlos directos
Final = [
    '.com',
    '.store'
]
# Los revome remuven cuando usas algun caracter distintivo (, .) seguido de lo que deseas remover
# removeprefix remueve el comienzo
# removesuffix remueve el final
for link in links:
    print(link.removeprefix('www.').removeprefix('https://www.').removeprefix('http://www.').removeprefix('http://').removeprefix('https://')
            .removesuffix('.com').removesuffix('.store').removesuffix('.org').removesuffix('.io'))