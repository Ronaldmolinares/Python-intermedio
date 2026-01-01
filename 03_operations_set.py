set_cars = {"BMW", "FERRARI", "BUGATI", "MASERATI", "PORCHE"}
set_cars_low = {"renult, chevrolet", "BMW"}
set_other = {"renoult", "corvete"}

# Union
union_set = set_cars_low.union(set_cars)
print(union_set)

# Intersección
intersection_set = set_cars_low.intersection(set_cars)
print(intersection_set)

# Diferencia
difference_set = set_cars.difference(set_cars_low)
print(difference_set)

# Diferencia simetrica
# dif_sim_set = set_cars.symmetric_difference(set_cars_low)
dif_sim_set = set_cars ^ set_cars_low ^ set_other
print(dif_sim_set)

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = (southAm ^ northAm).union(centralAm)


print(new_set)
