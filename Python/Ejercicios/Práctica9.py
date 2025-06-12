import re
import string
num = input("Número de télefono: ")
if re.match("638(.+)", num):
 print("valido")
else:
    print("no es valido") 