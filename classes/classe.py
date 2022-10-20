class carro():
    def __init__(self):
        self.nome = "Honda"
        self.velocidade = 80
        print("o carro do ano")
    def printar(self):
        print(f"o carro é o {self.nome} e tem a velocidade máxima de  {self.velocidade}")

novo_carro = carro()
print(novo_carro.nome)
novo_carro.printar()