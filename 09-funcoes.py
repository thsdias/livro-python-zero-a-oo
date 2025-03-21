
print ('\n--------------------------------------------')
print('Funcoes')
print ('--------------------------------------------\n')

print('Funcao simples sem parametros:')

def hello():
    print('Hello, World!')

print(hello())


print('\nFuncao simples com parametros:')

def eleva_numero_ao_cubo(numero):
    valor_a_retornar = numero ** 3
    return(valor_a_retornar)

num = eleva_numero_ao_cubo(3)
print(f'O numero 3 elevado ao cubo é: {num}')


print('\nFuncao composta com *args:')

def print_2_vezes(*args):
    for param in args:
        print(param + '!' + param + '!')

print_2_vezes('Hello World!! ')


print('\nFuncao composta com **kwargs:')

def informacoes(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} -> {value}')

pessoa = informacoes(nome='Joao', idade=30, cidade='Sao Paulo')


print('\n')
