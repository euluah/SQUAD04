from atv22 import verifica_cep

estados_sudeste_sul = ["SP", "RJ", "MG", "ES", "RS", "SC", "PR"]

cep = int(input("Informe o cep: "))

estado = verifica_cep(cep)
estado.lower()
verificador=False


for uf in estados_sudeste_sul:
    if estado in uf:
        verificador= True

if verificador == True:
    print(f"O estado de {estado} é elegível para frete")
else:
    print(f"O estado de {estado} não elegível para frete")