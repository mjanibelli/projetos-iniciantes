import random 
import os 
import time

import forca_modulo

print(" Jogo da Forca ".center(25, "="))

lista_palavras = ["amigos", "programação", "computador",
                    "jogos", "musicas", "guarda-chuva"]
palavra_maquina = random.choice(lista_palavras)
chances = 6

print("\nBem vindo ao jogo da forca! Você tem 6 chances para adivinhar a palavra que pensei!")
palavra_secreta = "_" * len(palavra_maquina)
time.sleep(3)
os.system("cls")

while chances > 0 and palavra_secreta != palavra_maquina:
    print(f"\nPalavra: {palavra_secreta}")
    print(f"Chances: {chances}")
    letra_esc = input("Digite uma letra: ").lower()
    os.system("cls")

    if letra_esc in palavra_maquina and letra_esc != "":
        print(f"A letra '{letra_esc}' pertence a palavra que pensei!")
        palavra_secreta = forca_modulo.encaixar_letra(letra_esc, palavra_maquina, palavra_secreta)

    else:
        print(f"A letra '{letra_esc}' não pertence a palavra que eu pensei!")
        chances -= 1

if chances == 0:
    os.system("cls")
    print(f"\nInfelizmente você perdeu! A palavra que pensei era: '{palavra_maquina}'")
    
if palavra_secreta == palavra_maquina:
    os.system("cls")
    print("\nParabéns, você venceu!! ")
