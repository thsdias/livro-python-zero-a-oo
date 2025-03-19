
print ('\n--------------------------------------------')
print('Dicionarios')
print ('--------------------------------------------\n')

user = { 
        'nome': 'Maria', 
        'idade': 25, 
        'formacao': ['Engenharia', 'Matematica']
        }

print('tipo: ', type(user))
print('Tamaho Dict: ', len(user))
print('Consulta campo Dict "nome": ', user.get('nome'))
print('Consulta quais sao as chaves: ', user.keys())
print('Consulta quais sao os valores: ', user.values())
print('Consulta todos os itens (chaves e valores): ', user.items())
print('Retorna Dicionario de dados: ', user)

print('\nAtualiza campo Dict "idade"')
user['idade'] = 30
print('Retorna novo valor campo "idade": ', user['idade'])

print('\nAdicionando mais dados ao campo Dict "formacao"')
user['formacao'].append('Fisica')
print('Dicionario Atualizado:', user)


print('\n')
