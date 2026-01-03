numbers = [1, 2, 3, 4, 5]
numbers_mult = []

for num in numbers:
    numbers_mult.append(num * 26)

print(numbers)
print(numbers_mult)

numbers_div = list(map(lambda x: x / 2, numbers))
print(numbers_div)


list_1 = [20, 30, 55, 75]
list_2 = [9, 5, 1]

result = list(map(lambda x, y: x + y, list_1, list_2))
print(result)
