import os

texto = "Olá, isso é um teste.\nTestando as funções nativas de análise de dados do Python"

arquivo = open(os.path.join(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\teste2.txt"), "w")

for palavra in texto.split():
    arquivo.write(palavra+" ")

arquivo.close()

with open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\teste2.txt", "r") as arquivo:
    x = arquivo.read()

print(x)
print(len(x))

with open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\teste2.txt", "w") as arquivo:
    arquivo.write(texto[:21])
    arquivo.write(texto[21:])

arquivo.close()

with open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\teste2.txt", "r") as arquivo:
    print(arquivo.read())