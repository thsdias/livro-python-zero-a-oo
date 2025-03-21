
# Conjuntos Numericos
print ('\n--------------------------------------------')
print('Conjuntos Numericos')
print ('--------------------------------------------\n')

cj = { 1, 2, 3, 4, 5 } 
print(type(cj))

print('\nUniao de Conjuntos')
c1 = { 2, 3 }
c2 = { 7, 15 }
union = c1.union(c2)
print('c1:', c1)
print('c2:', c2)
print('union:', union)

print('\nIntersecao de Conjuntos')
c3 = { 2, 3, 4, 5 }
c4 = { 2, 20, 23, 5 }
inter = c3.intersection(c4)
print('c3:', c3)
print('c4:', c4)
print('intersecao: ', inter)

print('\nManter alteracoes em um conjunto')
c1.update(c2)
print(c1)

print('\nEsta contido')
print('c1:', c1)
print('c2:', c2)
print('c1 contem c2:', c2 <= c1)

print('\nDiferenca')
c5 = { 1, 2 }
c6 = { 2, 3 }
print('c5:', c5)
print('c6:', c6)
print('dif:', c5 - {6})


print('\n')
