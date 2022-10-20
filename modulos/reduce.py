from functools import reduce

lista = [1, 4, 3.5, 67]

print(reduce(lambda a, b: a*b, lista))

print(reduce(lambda a, b: a if (a>b) else b, lista))
