import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)
if response.status_code ==200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        # se o nome do restaurante n existir, criar uma nova lista
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
            
        dados_restaurante[nome_restaurante].append({
			"Item": item['Item'],
			"Preço": item['price'],
			"Descrição": item['description']
		})

else:
    print(f'Erro a listar os dados: {response.status_code}')
    
    # pegar o nome do restaurante e os seus dados, depois criar um arquivo
for nome_restaurante, dados in dados_restaurante.items():
    # indicar o nome do arquivo que no caso, vais ser o nome do restaurante convertido em json
    nome_arquivo = f'{nome_restaurante}.json'
    # criar o arquivo
    with open(nome_arquivo,'w') as arquivo_restaurante:
        # criar um json
        json.dump(dados,arquivo_restaurante,indent=4)
    