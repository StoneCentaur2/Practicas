Balance = 945.70

while True:
    try:
        num = float(input('Deposit / Deposito: '))
        break
    except ValueError:
        print('Must be a valid quantity / Monto no valido')

Balance += num
print(f'Balance / Balanza: {Balance}')