class carro():
    def __init__(self, nome, velocidade):
        self.nome = nome
        self.velocidade = velocidade
    def printar(self):
        print(f"o carro é o {self.nome} e tem a velocidade máxima de  {self.velocidade}")

carro_new = carro("Fox", 98)
print(carro_new.velocidade)
