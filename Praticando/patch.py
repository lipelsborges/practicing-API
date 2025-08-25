import requests
informacoes = '{"Nome": "Daniel", "Sobrenome": "Candiotto", "Idade": "17"}'

requisicao = requests.patch("https://testeapi-c6cea-default-rtdb.firebaseio.com/-OYWaK10aZz6t-WLFbdZ.json", data=informacoes)
print(requisicao)
print(requisicao.json())