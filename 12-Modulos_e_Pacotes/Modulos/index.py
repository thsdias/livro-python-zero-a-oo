
print ('\n--------------------------------------------')
print('Modulos')
print ('--------------------------------------------\n')

print('Importando Modulos:')
print('\n')

import boasvindas
boasvindas.msg_boas_vindas()
boasvindas.msg_para_o_usuario('Usuario Teste')
print('\n')

import soma
print(f'O resultado da soma é: {soma.soma(10, 20)}')
print('\n')

print(f'O resultado da soma é: {soma.soma2()}')
print('\n')

# Importa apenas a função soma2:
from soma import soma2
print(f'O resultado da soma é: {soma2()}')

# Adiciona um alias para o modulo
import soma as s
print(f'O resultado da soma é: {s.soma(5, 4)}')


print('\n')