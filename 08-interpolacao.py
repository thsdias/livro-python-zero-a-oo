
# Interpolacao
print ('\n--------------------------------------------')
print('Interpolacao')
print ('--------------------------------------------\n')

print('Mascara de substituicao de string com %s')
nome = input('Digite seu nome: ')
print('Ola %s!' % nome)

print('\nMascara de substituicao de inteiros com %d')
idade = int(input('Digite sua idade: '))
print('Voce tem %d anos!' % idade)

print('\nUsando mais de uma mascara de substituicao')
print('Nome: %s, Idade: %d' % (nome, idade))

nota1 = '{0} está reprovado, assim como seu colega {1}'
print(nota1.format('Pedro', 'Joao'))

print('\nUsando novo padrao de interpolacao')
print(f'Nome: {nome}, Idade: {idade}')



print('\n')
