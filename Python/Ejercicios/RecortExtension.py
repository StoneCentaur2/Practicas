full_files = [
    'info.txt',
    'image.png',
    'script.c',
    'image.jpg',
    'info.3.txt'
]
import os
for file in full_files:
    name = os.path.splitext(file)[0]
    print(name)