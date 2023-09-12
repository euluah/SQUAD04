from atv22 import verifica_cep

estados_norte_nordeste = [
    "AC", "AL", "AM", "AP", "BA", "CE", "MA", "PA", "PB", "PE", "PI", "RN", "RO", "RR", "SE", "TO"
]

try:
    cep = int(input("Informe o cep (apenas números): "))
    estado = verifica_cep(cep)
    estado.lower()
    verificador=False


    for uf in estados_norte_nordeste:
        if estado in uf:
            verificador= True

    if verificador == True:
        print(f"O estado de {estado} é elegível para frete")
    else:
        print(f"O estado de {estado} não elegível para frete")
except ValueError:
    print("O valor fornecido deve ser um número")


