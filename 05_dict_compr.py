import random

dictionari = {}
print("\nEjemplo 1:\n")
for i in range(1, 6):
    dictionari[i] = i * 2

print(dictionari)

dict_comprehension: dict = {i: i * 2 for i in range(1, 6)}
print(dict_comprehension)

print("\nEjemplo 2:\n")
countries = ["col", "mex", "bol", "per"]
population = {}
for pais in countries:
    population[pais] = random.randint(1, 2000)

print(population)

countries_comprehension = {pais: random.randint(1, 2000) for pais in countries}
print(countries_comprehension)

print("\nEjemplo 3:\n")
names = ["Laura", "Pipe", "Ronald", "Maria", "Bili"]
ages = [14, 17, 36, 46, 74]

# forma pythonica
users: dict[str, int] = dict(zip(names, ages))
print(users)
print(type(users))

# forma tradicional
users_1 = {names[i]: ages[i] for i in range(len(names))}
print(users_1)

# forma mas pythonica
users_final = {name: age for name, age in zip(names, ages)}
print(users_final)
