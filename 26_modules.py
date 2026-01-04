import collections
import re  # Busca patrones en texto con expresiones regulares
import sys  # verifica SO y ruta del archivo
import time

print("Uso del modulo sys")
print(sys.path)

print("\nUso del modulo re")
text = "Mi numero de telefono es 35698748999, el codigo del pais es 57, numero de la suerte 5"

result = re.findall("[0-9]+", text)
print(result)

print("\nUso del modulo time")
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(result)

print("\nUso del modulo collections")
numbers = [
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    3,
    3,
    4,
    2,
    2,
    1,
    1,
    2,
    43,
    4,
    5,
    6,
    677,
    8,
    6,
    6,
    54,
    4,
    3,
    3,
    4,
    56,
]

counter = collections.Counter(numbers)
print(counter)
print(type(counter))
