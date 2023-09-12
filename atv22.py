import requests

def verifica_cep(cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    data=response.json()
    uf = data['uf']

    return uf