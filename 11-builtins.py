
print ('\n--------------------------------------------')
print('Builtins')
print ('--------------------------------------------\n')

print(dir(__builtins__))    # Utilizado para ver tudo o que está disponível em sua IDE em tempo real.
print('\n')


print('\nImportando bibliotecas')

import math
raio = 15.3
print('Area do circulo: ', math.pi * raio ** 2)


print('\nImportando apenas a funcao da bibliotecas')

from math import pi
raio = 15.3
print('Area do circulo: ', pi * raio ** 2)


print('\n')
