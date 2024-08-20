from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe a primeira msg da programacao'''
    
    return {'Hello':'world'}

# criando rotas para criar um caminho do endpoint
@app.get('/api/restaurantes/')
# indicando o endpoint
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardapios dos restaurantes'''
    # imprimir restaurante especificos
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)
 
    if response.status_code ==200:
        dados_json = response.json()
        # se n existir nenhuma informacao do restaurante
        if restaurante is None:
            return {'Dados':dados_json}
        
        dados_restaurante = []
        for item in dados_json:
        #verificar se o restaurante passado na api corresponde ao passado na url. Se tiver, adicionar dentro de dados_restaurante
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "Item": item['Item'],
                    "Preço": item['price'],
                    "Descrição": item['description']
                })
        return {'Restaurante': restaurante,'Cardapio': dados_restaurante}

    else:
        return{'Erro': f'{response.status_code} - {response.text}'}