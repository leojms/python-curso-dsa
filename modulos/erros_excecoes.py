try:
    8+"d"
except TypeError:
    print("Operação inválida")

try:
    a = open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\potencias.txt", "r")
except IOError:
    print("Arquivo não encontrado")
else:
    print("O arquivo pôde ser aberto")
    a.close()

while True:
    try:
        a=int(input("Digite um número: "))
    except:
        print("Você não digitou um número!")
        continue
    else:
        print(f"Seu número foi o {a}")
        break
    finally:
        print("Obrigado!")