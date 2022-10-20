
def operacao(y):
    return y*6

lista = [0, 4, 3.5, 67]
lista2 = [7, 4, 20, 78]

print(list(map(operacao, lista)))
print(list(map(lambda y: y*6, lista)))
print(list(map(lambda x, y: x+2*y, lista, lista2)))
