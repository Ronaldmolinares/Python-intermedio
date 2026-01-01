import random

print("\nEjemplo:\n")
countries = ["col", "mex", "bol", "per"]
# population = {}
countries_comprehension = {pais: random.randint(1, 100) for pais in countries}
print(countries_comprehension)

result = {
    pais: poblacion
    for pais, poblacion in countries_comprehension.items()
    if poblacion > 50
}

print(result)

print("\nEjemplo 2:\n")

text = "HOLA desde el años 2025 proximamente 2026"
unique = {char: char.upper() for char in text if char in "aeiouAEIOU"}
print(unique)


print("\nForma tradicional:")
lista: list[str] = []
word: str = ""
for i in text:
    if i == " ":
        lista.append(word)
        word = ""
    word += i

if word != "":
    lista.append(word)

print(lista)

vocales = "aeiouAEIOU"
contador = 0

word_dict = {}

for p in lista:
    for i in p:
        if i in vocales:
            contador += 1
    word_dict[p] = contador
    contador = 0

print(word_dict)


print("\nCon comprehension:")
word_dict_2 = {
    palabra: sum(1 for letra in palabra if letra in vocales) for palabra in lista
}

print(word_dict_2)


word_dict_3 = {
    palabra: len([letra for letra in palabra if letra in vocales]) for palabra in lista
}
print(word_dict_3)
