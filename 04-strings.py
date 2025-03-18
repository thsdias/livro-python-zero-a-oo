
print ('\n--------------------------------------------')
print('Alterando a cor de um texto')
print ('--------------------------------------------\n')

# Exemplo de texto com cores

msg = 'Hello, World!'

cor_fundo_verde = '\033[1;42m'
cor_fundo_vermelho = '\033[1;41m'
cor_fundo_azul = '\033[1;44m'
cor_fundo_branco = '\033[1;107m'

cor_letra_vermelho = '\033[91m'
NORMAL = '\033[0m'

print(cor_fundo_branco, msg)


# Exemplo de texto posicionados na tela

frase1 = 'Bem vindo ao Python!'
print('\n', frase1.center(50), '\n')
print('\n', frase1.ljust(50), '\n')
print('\n', frase1.rjust(50), '\n')

# Mascara na exibiçao de valores numericos
print ('\n--------------------------------------------')
print('Mascara na exibiçao de valores numericos')
print ('--------------------------------------------\n')

num1 = 34.29545781214875432
print(f'Valor original: {num1}')
print(f'- {num1:.2f}')
print(f'- {num1:.5f}')


print('\n')
