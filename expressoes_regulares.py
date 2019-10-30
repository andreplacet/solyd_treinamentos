import re


string_teste = 'Python é uma linguagem, bonita, simples e muito poderosa' \
               'o Python é muito utilizado para analise de dados, segurança da informação,' \
               'desenvovilmento WEB e mobile entre outras possibilidades do Python.'

padrao = re.search(r'Python', string_teste) # RAW STRING

padrao2 = re.findall(r'Py\w+', string_teste) # busca todas as strings dentro dos parametros passados

padrao3 = re.findall(r'[Pyt]+', string_teste) # encontrar dentro de um grupo de caracteres

if padrao:
    print(f'A palavra \033[33m{padrao.group()}\033[m foi encontrada nos parametros passados')
else:
    print('Padrão não encontrado!')

if padrao2:
    print(f'A palavra(s) \033[33m{padrao2}\033[m foram encontradas nos parametros passadoa!')
else:
    print('Padrão não encontrado!')
if padrao3:
    print(f'A palavra(s) \033[33m{padrao3}\033[m foram encontradas nos parametros passados')
else:
    print('Padrão não encontrado')


# https://regex101.com - site te permite consultar expressões regulares em tempo real