import os

lista = ["dado 1", "dado 2", "dado 3", "dado 4"]

path = os.getcwd()

arquivo_lista = "arquivo.txt"

if not os.path.exists(path):
    os.mkdir(path)

caminho_arquivo = os.path.join(path, arquivo_lista)


with open(caminho_arquivo, "w") as arquivo:
    for item in lista:
        arquivo.write(f"{item}\n")

