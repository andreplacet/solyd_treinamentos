import re
import requests

url = 'http://colegioferreiralima.com.br/contato.html'
req = requests.get(url)

email = re.findall(r'\w+[-\w+]+\w+@\w+.\w+.\w+', req.text)

if email:
    print(email)
else:
    print('E-mail ou forma de contato nao econtrados!')
