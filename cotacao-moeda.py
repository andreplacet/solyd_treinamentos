import requests
import json
from datetime import datetime
from time import sleep

url = 'https://economia.awesomeapi.com.br/all/USD,EUR,BTC'
cotacao = requests.get(url).text
#print(cotacao)
dicionario = json.loads(cotacao)
while True:
    print(f'\n{"-" * 5}COTAÇÃO DE MOEDAS{"-" * 5} {datetime.now()}')
    print(f'''\n{dicionario['USD']['name']}/Alta: {dicionario['USD']['high']}
{dicionario['USD']['name']}/Baixa: {dicionario['USD']['low']}
{dicionario['EUR']['name']}/Alta: {dicionario['EUR']['high']}
{dicionario['EUR']['name']}/Baixa: {dicionario['EUR']['low']}''')
    sleep(4)
