set_countries = {"Colombia", "Mexico", "Brazil", "mexico"}

# Ver tamaño del conjunto
size = len(set_countries)
print(size)

print("Colombia" in set_countries)

# añadir elementos
set_countries.add("Bolivia")
print(set_countries)

# actualizar
set_countries.update({"Argentina", "Ecuador"})
print(set_countries)


# remover

set_countries.remove("mexico")
print(set_countries)
# set_countries.remove("mexico")
set_countries.discard("mexico")
