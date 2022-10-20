arquivo = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\salarios.csv", "r")
data = arquivo.read()
linhas = data.split("\n")
colunas = []

for linha in linhas:
    split_linha = str(linhas).split(",")
    colunas.append(split_linha)

print(colunas)