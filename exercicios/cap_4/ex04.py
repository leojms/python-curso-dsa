def cubo(x):
    return x**3
def quadrado(x):
    return x**2

lista = [0, 1, 2, 3, 4]
func=[cubo, quadrado]

for i in range(len(func)):
    print(list(map(func[i], lista)))
