vogais = ["a", "e", "i", "o", "u"]

palavra = input("Escreva uma palavra: ")

cont = 0
for letra in palavra:
    if letra.lower() in vogais:  # Use .lower() para considerar maiúsculas e minúsculas
        cont += 1

print(f"A palavra '{palavra}' possui {cont} vogais.")