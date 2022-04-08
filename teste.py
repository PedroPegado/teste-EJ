import requests

response = requests.get('https://www.uol.com.br')
print(response.json())

