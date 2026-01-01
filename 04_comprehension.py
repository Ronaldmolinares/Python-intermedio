numbers = []

for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

comprehension_number = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(comprehension_number)
