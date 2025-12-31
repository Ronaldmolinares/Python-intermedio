set_countries = {"Colombia", "Mexico", "Brazil", "mexico"}
print(set_countries)
print(type(set_countries))

set_numbers = {10, 20, 30, 40, 50, 60, 710}
print(set_numbers)
print(type(set_numbers))

set_types = {True, 50, "Hola", 96.3}
print(set_types)
print(type(set_types))

# Conjunto a partir de otras estructuras
set_from_string = set("hola")
print(set_from_string)
print(type(set_from_string))


set_from_tuples = set(("carro", "moto", "cicla"))
print(set_from_tuples)


nums = [1, 2, 3, 4, 5, 6, 6, 5, 1]
set_num = set(nums)
print(set_num)

unique_numbers = list(set_num)
print(unique_numbers)
print(type(unique_numbers))
