inv = [
    'Sword',
    'Shield',
    'Potion of invesibility',
    'Map'
]
for index, item in enumerate(inv):
    print(index,item)

################################################################
# Dictionaries
names = [
    'Daniel',
    'Mike',
    'William',
    'John'
]

#Dictionary Comprehension
length = {name:len(names) for name in names}
print(length)