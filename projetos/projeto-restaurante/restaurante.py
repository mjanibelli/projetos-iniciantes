import os
import time

import restaurante_modulo

nome = input("Digite o nome do restaurante: ")
os.system("cls")

restaurante = restaurante_modulo.Restaurante(nome)

while True:
    print(f" {nome.title()} ".center(30, "="))
    print("[1] -> Atender cliente\n[2] -> Gerar resultados\n[0] -> Sair")
    escolha = input("Escolha: ")

    if escolha == "1":
        preco = float(input("\nDigite o preço do prato do cliente: "))

        if restaurante.atender_cliente(preco):
            print("Cliente atendido!")
            time.sleep(1.5)
            os.system("cls")
        else:
            print("Esse valor não é válido!")
            time.sleep(1.0)
            os.system("cls")

    elif escolha == "2":
        restaurante.gerar_resultado()
        time.sleep(2.0)
        os.system("cls")

    elif escolha == "0":
        break

    else:
        print("Opção inválida!")
        time.sleep(1.0)
        os.system("cls")

print(" Obrigado por usar o programa! ".center(46, "="))