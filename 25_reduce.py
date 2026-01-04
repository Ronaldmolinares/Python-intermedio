import functools

numbers = [1, 2, 3, 4, 5, 6, 7, 89]


def cont(lista):
    counter = 0
    for numero in lista:
        counter += numero
    return counter


result_1 = cont(numbers)
print(result_1)


result_2 = functools.reduce(lambda counter, item: counter + item, numbers)
print(result_2)


def accum(counter, item):
    return counter + item


result_3 = functools.reduce(accum, numbers)
print(result_3)
