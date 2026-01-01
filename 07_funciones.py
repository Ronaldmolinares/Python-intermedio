def find_volume(length, width, depth):
    return length * width * depth, "retorno multiple"


result, text = find_volume(1, 3, 5)

print(result)
print(text)

# Ignorar valores con _
result2, _ = find_volume(1, 3, 5)  # Ignora el segundo valor
print(result2)
