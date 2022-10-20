arquivo = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\teste.txt", "w+")
arquivo.write("olá, isso é um teste.\nTestando as funções nativas de análise de dados do Python")
arquivo.close()
arquivo = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\teste.txt", "r")
print(arquivo.read())
arquivo.seek(0)
print(arquivo.readlines())

lista=[]

for line in open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\teste.txt"):
    lista.append(line)

print(lista)

