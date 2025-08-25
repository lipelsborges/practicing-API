import requests

requisicao = requests.get("https://testeapi-c6cea-default-rtdb.firebaseio.com/.json")
print(requisicao)
print(requisicao.json())
