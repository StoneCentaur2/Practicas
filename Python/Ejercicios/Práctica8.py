import re
import string
pal = input("Palabra con terminación 'on': ")
if re.match ("(.+)on", pal):
    print ("cierto")
else:
    print("Falso")