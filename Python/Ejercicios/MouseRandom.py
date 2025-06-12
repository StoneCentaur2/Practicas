# pip install pyautogui
# pip install keyboard
"""
Crear ejecutable
pyinstaller --onefile --noconsole MouseRandom.py
"""
import pyautogui as pag
import random
import time
import keyboard as Keyboard
while True:
    if Keyboard.is_pressed('l'):
        break
    x = random.randint(200, 1800)
    y = random.randint(200, 1500)
    pag.moveTo(x, y, 0.01)
    time.sleep(0.01)

print("Programa finalizado...")