
print ('\n--------------------------------------------')
print('Tracebacks e exceções')
print ('--------------------------------------------\n')

try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

except:
    print('Numero invalido, tente novamente!')

finally:
    soma = int(num1) + int(num2)
    print(f'A soma dos números é: {soma}')

print('\n')