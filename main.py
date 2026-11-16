from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import requests
from pathlib import Path
import json

app = FastAPI()

DADOS = Path(__file__).parent / 'data'

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação! 
    '''
    return {'Hello' : 'World'}

@app.get('/api/restaurantes/')

def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes  
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        dados_restaurantes = []
        if restaurante is None:
            return {'Dados': dados_json}
        
        for item in dados_json:
            if item['Company'] == restaurante:   
                dados_restaurantes.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']  
                })             
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurantes}
    else:
        return f'Erro: {response.status_code} - {response.text}'
    
@app.get('/api/restaurantes/nomes', response_class=PlainTextResponse)
def listar_nomes():
    nomes = [arquivo.stem for arquivo in DADOS.glob('*.json')]
    return 'Restaurantes:\n' + '\n' .join(nomes)