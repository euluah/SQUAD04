import requests

def verifica_cep(cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    data=response.json()

    if 'erro' in data:
        return None

    uf = data['uf']

    return uf
    