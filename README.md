# Praticando FastAPI

Projeto de prática da formação de Python da Alura, criado para aprofundar o conhecimento em **FastAPI**, no **protocolo HTTP** e na manipulação de **arquivos JSON**.

## Objetivo

- Consumir uma API externa com requisições HTTP (`GET`) e tratar o *status code* da resposta.
- Ler e transformar dados JSON em estruturas Python (listas e dicionários).
- Agrupar os dados e salvá-los em arquivos `.json` separados.
- Servir esses dados por meio de uma API própria com FastAPI (próximo passo).

## Estado atual

O `main.py` contém a aplicação FastAPI, por enquanto só com a rota `GET /api/hello`. Para rodá-la:

```powershell
uvicorn main:app --reload
```

A documentação automática fica em `http://127.0.0.1:8000/docs`.

O `app.py` é um script de coleta e organização de dados, independente da API:

1. Faz um `GET` em `https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json`.
2. Verifica se o *status code* é `200`.
3. Agrupa os itens do cardápio por restaurante (campo `Company`).
4. Grava um arquivo `.json` para cada restaurante na pasta `data/`, com os campos `item`, `price` e `description`.

## Estrutura

```
Praticando_FastAPI/
├── main.py                     # Aplicação FastAPI (rota /api/hello)
├── app.py                      # Script que busca, agrupa e salva os dados
├── requirements.txt            # Dependências do projeto
├── data/                       # JSONs gerados pelo app.py (um por restaurante)
│   ├── Burger King.json
│   ├── KFC.json
│   ├── McDonald’s.json
│   ├── Pizza Hut.json
│   ├── Taco Bell.json
│   └── Wendy’s.json
```

## Como executar

Pré-requisito: Python 3.10 ou superior.

```powershell
# Criar e ativar o ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instalar as dependências
pip install -r requirements.txt

# Gerar os arquivos JSON
python app.py
```

No Linux/macOS, ative o ambiente com `source venv/bin/activate`.

## Formato dos dados gerados

Cada arquivo contém uma lista de pratos:

```json
[
    {
        "item": "Limited Time ORIGINAL RECIPE CHICKEN Chicken Thigh",
        "price": 48.5,
        "description": "Perfeito para quem gosta de sabores picantes."
    }
]
```

## Tecnologias

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) e [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://requests.readthedocs.io/)

## Próximos passos

- [ ] Expor rotas `GET` para listar restaurantes e seus cardápios (lendo `data/`).
- [ ] Usar parâmetros de rota e de consulta (por exemplo, filtrar por restaurante).
- [ ] Retornar *status codes* adequados (`200`, `404`) com `HTTPException`.
