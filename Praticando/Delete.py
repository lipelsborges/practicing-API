import requests

requisicao = requests.delete("https://testeapi-c6cea-default-rtdb.firebaseio.com/-OYWaK10aZz6t-WLFbdZ.json")
print(requisicao)
print(requisicao.json())