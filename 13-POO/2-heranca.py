
print ('\n--------------------------------------------')
print('PROGRAMAÇÃO ORIENTADA A OBJETOS')
print ('--------------------------------------------\n')

print('Herança:')
print('\n')

class Carros():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def descricao(self):
        print(f'O carro: {self.nome} é {self.cor}')

class Gol(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Corsa(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


gol1 = Gol('Gol 2019 completo', 'preto')
corsa2 = Corsa('Corsa 2017 2 portas', 'prata')

print(gol1.descricao())
print(corsa2.descricao())


print('\n')