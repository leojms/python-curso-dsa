arq = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\potencias.txt", "w")
arq.write("bom dia")
arq.close()
arq = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\potencias.txt", "r")
print(arq.read())
print(arq.tell())
arq.seek(0,0)
print(arq.read(4))
print("\n")
arq.close()
arq = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\potencias.txt", "a")
arq.write(". Tudo bem?")
arq.close()
arq = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\potencias.txt", "r")
print(arq.read())