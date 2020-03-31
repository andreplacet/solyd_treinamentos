import re

import requests

url = 'http://www.umc.br/grad/'
ulr_imprensa = 'http://uniesp.edu.br/sites/suzano/imprensa.php'
req = requests.get(url)
req2 = requests.get(ulr_imprensa)

email = re.findall(r'\w+[-\w+]+\w+@\w+.\w+.\w+', req.text)
email2 = re.findall(r'\w+[-\w+]+\w+@\w+.\w+.\w+', req2.text)

for _ in email2:
    if _ not in email:
        email.append(_)

if email:
    print(f'\nBusca efetuada com sucesso!\n'
          f'Imprimindo lista de e-mails encontrados na pagina web requisitada\n')
    for _ in range(len(email)):
        print(f'{_ + 1} - {email[_]}')
else:
    print('E-mail ou forma de contato nao econtrados!')