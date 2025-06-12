import time
BAR_LEN = 24
elments = ['-', '\\', '||', '//']

for i in range(BAR_LEN+1):
    frame = 1 % len(elments) # direccion contraría cambiar < por >, y cargar del medio por ^
    print(f'\r[{elments[frame]*i:=^{BAR_LEN}}]', end='')
    time.sleep(0.2)