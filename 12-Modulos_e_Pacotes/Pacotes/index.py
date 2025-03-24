
print ('\n--------------------------------------------')
print('Pacotes')
print ('--------------------------------------------\n')

print('Importando Pacotes:')
print('\n')

""" 
Importando calculadora_soma que faz parte do pacote calc. 
Essa sintaxe 'calc.calculadora_soma' indica que calc é uma 
subpasta onde se encontra o módulo calculadora_soma.
"""
import calc.calculadora_soma


# Importando a função soma, do módulo calculadora_soma, do pacote calc.
from calc.calculadora_soma import soma


# Importando a função soma do módulo calculadora_soma do pacote calc e a referenciando como sm.
from calc.calculadora_soma import soma as sm


print('\n')