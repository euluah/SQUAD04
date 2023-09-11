import requests

squad04={
    "Luana":"72580-500",
    "Lara":"77019-090",
    "Rafaela":"59112400",
    "Angelica":"98050010"
}

for nome, cep in squad04.items():
    cep = cep
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    data=response.json()
    localidade =data['localidade']
    print(f"A cidade de {nome} é {localidade}")

