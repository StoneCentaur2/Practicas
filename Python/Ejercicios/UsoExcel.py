import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('emails.xls', sheet_name='Hoja1')

# Convertir los correos electrónicos a minúsculas
df['email'] = df['email'].str.lower()

# Obtener los correos electrónicos únicos
unique_emails = df['email'].drop_duplicates()

# Mostrar los correos electrónicos únicos
print(unique_emails)
