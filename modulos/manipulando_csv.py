import csv

with open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\testecsv.csv", "w") as arquivo:
    dados = csv.writer(arquivo)
    dados.writerow(["nome", "nota", "presente?"])
    dados.writerow(["Siclano", 7, "Sim"])
    dados.writerow(["Fulano", 9, "Não"])

with open(r"C:\Users\leonardo.simoes\OneDrive - Sistema FIEB\testecsv.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    data=list(leitor)
    print(data)

