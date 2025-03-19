
print ('\n--------------------------------------------')
print('Listas')
print ('--------------------------------------------\n')

lista = [1, 5, 'Maria', 3.14, 'Python', 7, 9]
print(lista)
lista.append('Joao')
print(lista)
print('index of Python: ', lista.index('Python'))
# print('index of NewItem: ', lista.index('NewItem')) // retorna erro - indice nao existe

print('NewItem' in lista)

print('\n')
lista2 = []
lista2.append('Maria')
lista2.append('Joao')
print('lista2: ', lista2)

lista2.reverse()
print('reverse lista2: ', lista2)

lista3 = [1, 2, 3, ['Python', 'Java']]
print('\nlista3: ', lista3)


# Tuplas
print ('\n--------------------------------------------')
print('Tuplas')
print ('--------------------------------------------\n')

tuplaSimples = (1, )
tupla = (1, 5, 'Maria', 3.14, 'Python', 7, 9)

print('tupla simples: ', tuplaSimples)
print('tupla: ', tupla)


# Pilhas
print ('\n--------------------------------------------')
print('Pilhas')
print ('--------------------------------------------\n')

pilha = [1, 2, 3, 4, 5]
print('pilha: ', pilha)
print('tamanho:',len(pilha))

pilha.append(70) # Add elemento no topo da pilha.
print('\npilha: ', pilha)

pilha.pop() # Remove elemento do topo da pilha.
print('pilha: ', pilha)


print('\n')
