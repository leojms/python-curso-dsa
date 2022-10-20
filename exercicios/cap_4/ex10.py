lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i, val in enumerate(lista):
    if i<=5:
        continue
    else:
        print(val)