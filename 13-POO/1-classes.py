
print ('\n--------------------------------------------')
print('PROGRAMAÇÃO ORIENTADA A OBJETOS')
print ('--------------------------------------------\n')

print('Classes:')
print('\n')

class Carro:    # Por convencao o nome da classe deve ser case sensitive.
    carro1 = 'Gol modelo 2016 completo'
    carro2 = 'Celta ano 2015 4 portas'
    carro3 = 'Uno ano 2015 baixa quilometragem'
    carro4 = 'Clio 2018 flex doc. vencido'

print(Carro.carro1)
print('\n')


class Pessoa:
    pass    # Pass é utilizado para definir uma classe vazia, e evita erros de sintaxe.

pessoa1 = Pessoa()
pessoa1.nome = 'João'
pessoa1.idade = 30

print(pessoa1.nome)
print(pessoa1.idade)
print('\n')


class Pessoa2:
    def acao(self): # self representa a instância da classe Pessoa2 que chamou o método acao.
                    # Ele permite que você acesse ou modifique atributos da instância ou chame outros métodos da mesma instância.
        print('Ação 1 etá sendo executada....')

pessoa2 = Pessoa2()
pessoa2.acao()
print('\n')


print('Definindo uma classes:')
print('\n')

class Usuario:
    def __init__(self, nome, idade):    # __init__: construtor da classe, que sempre tera 'self' como parametro (instancia padrao), seguido de quantos parametros personalizados o usuario criar, desde que separados por virgula.
        self.nome = nome
        self.idade = idade

    def boas_vindas(self):
        print(f'Usuário: {self.nome}, Idade: {self.idade}')

usuario1 = Usuario('Fernando', 35) # || usuario1 = Usuario(nome='Fernando', idade=35)
usuario1.boas_vindas()

print(usuario1.nome)
print('\n')


print('Alterando dados/valores de uma instância:')
print('\n')

usuario1.nome = 'Fernando Feltrin'
print(usuario1.nome)
print('\n')


print('Manipulacao via funcao especifica:')
print('\n')

usuario2 = Usuario('Maria', 25)
usuario2.nome = 'Maria Silva'
usuario2.boas_vindas()

setattr(usuario2, 'nome', 'Maria B. Silva')   # setattr: funcao que permite alterar o valor de um atributo de uma instancia.
delattr(usuario2, 'idade')                    # delattr: funcao que permite deletar um atributo de uma instancia.
setattr(usuario2, 'idade', 30)

usuario2.boas_vindas()
print('\n')


print('Aplicando recursividade:')
print('\n')

def imprimir(maximo, atual):    # Funcao recursiva que usa conceito de incremento, visto em for (loop), mas aplicado a objetos.
    if atual >= maximo:
        return

    print(atual)
    imprimir(maximo, atual + 1)

imprimir(10, 1)


print('\n')