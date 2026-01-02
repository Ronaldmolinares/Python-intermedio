def increment(x):
    return x * 2


increment_v2 = lambda x: x * 2


def high_ord_function(x, func):
    return x + func(x)


high_ord_v2 = lambda x, func: x + func(x)

result = high_ord_function(30, increment)

print(result)

result_v2 = high_ord_v2(30, increment)
print(result_v2)


# Para este caso la mejor foma es:
result_v3 = high_ord_function(30, lambda x: x * 2)
print(result_v3)
