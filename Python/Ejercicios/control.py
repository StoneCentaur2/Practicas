import pywhatkit
import flask
import pyautogui
import platform
import subprocess

if platform.system() == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
print("\nIntroduce la ip en el navegador del celular = '"+local+":8000'\n")

pywhatkit.start_server()