import requests
informacoes = '{"Nome": "Luiza"}'

requisicao = requests.post("https://testeapi-c6cea-default-rtdb.firebaseio.com/.json", data=informacoes)
print(requisicao)
print(requisicao.json())