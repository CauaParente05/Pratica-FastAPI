import requests
import json
from pathlib import Path

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurantes = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurantes:
            dados_restaurantes[nome_do_restaurante] = []
            
        dados_restaurantes[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']  
        })
else:
    print(f'Erro: {response.status_code}')
    
pasta_dados = Path(__file__).parent / 'data'
pasta_dados.mkdir(exist_ok=True)

for nome_do_restaurante, dados in dados_restaurantes.items():
    nome_do_arquivo = pasta_dados / f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4, ensure_ascii=False)