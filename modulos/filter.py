lista = range(0, 121)
print(list(filter(lambda n: True if(n%2==0) else False, lista)))
print(list(filter(lambda n: n%2==0, lista)))
print(list(filter(lambda n: n>70 and n%2==0, lista)))