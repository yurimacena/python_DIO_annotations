class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor
    
class Motocicleta(Veiculo): ## Herdando veiculo
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def esta_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "xfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)