def increment(x):
    return x + 1


result = increment(10)
print(result)

result_lambda = lambda x: x + 1

print(result_lambda(32))

full_name = (
    lambda name, last_name: f" Nombre completo: {name.title()} {last_name.title()} "
)

print(full_name("chepe", "san"))
