import requests
import json


def requisition(title):
    try:
        url = requests.get(f'http://www.omdbapi.com/?apikey=52d86029&t={title}&plot=full')
        dicionario = json.loads(url.text)
        return dicionario
    except Exception:
        print('Erro na conexão')
        exit()
        return None


url = ''
while True:
    opcao = str(input('Escreva o nome do Filme ou escreva "SAIR" para sair: ').lower())
    if opcao == 'sair':
        break
    else:
        pesquisa = requisition(opcao)
        if pesquisa['Response'] == 'False':
            print('\n\033[7;33mFilme não encontrado!\033[m\n')
        else:
            print(f'O filme foi encontrado!')
            print('-' * 30)
            print(f'Titulo:{pesquisa["Title"]}\nAno de Lançamento:{pesquisa["Year"]}\nDiretor:{pesquisa["Director"]}\n'
                  f'Atores:{pesquisa["Actors"]}\nimdb Rating:{pesquisa["imdbRating"]}')
            print('-' * 30)
