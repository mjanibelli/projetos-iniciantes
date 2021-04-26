import os

import conta_modulo

print(" Conta Bancária ".center(30, "="))

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu último sobrenome: ")
cliente = conta_modulo.ContaBancaria(nome, sobrenome)
os.system("cls")

while True:
    print("Menu:\n[1] -> Depositar\n[2] -> Sacar\n[3] -> Conta\n[0] -> Sair")
    escolha = input("\nEscolha: ")

    if escolha == "1":
        os.system("cls")
        quantia = float(input("Digite a quantia que deseja depositar: "))

        if cliente.depositar(quantia):
            print("Quantia depositada com sucesso!")
        else:
            print("Não é possível depositar valores menores ou iguais a zero")

        _ = input("\nAperte qualquer botão para continuar: ")
        os.system("cls")
        

    elif escolha == "2":
        os.system("cls")
        quantia = float(input("Digite a quantia que deseja sacar: "))

        if cliente.sacar(quantia):
            print("Saque realizado com sucesso!")
        else:
            print("Não foi possível realizar o saque!")

        _ = input("\nAperte qualquer botão para continuar: ")
        os.system("cls")

    elif escolha == "3":
        os.system("cls")
        cliente.mostrar_conta()
        _ = input("\nAperte qualquer botão para continuar: ")
        os.system("cls")

    elif escolha == "0":
        os.system("cls")
        break

    else:
        os.system("cls")
        print("Essa opção não existe! Tente novamente!\n")

print(" Obrigado por usar o programa! ".center(46, "="))