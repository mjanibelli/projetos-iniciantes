import os

import email_modulo

while True:
    print(" Encontra E-mails ".center(30, "="))

    arquivo_user = input("Digite o caminho do arquivo a ser pesquisado ou arraste-o: ")
    os.system("cls")
    email_modulo.encontrar_emails(fr"{arquivo_user}")

    esc = input("\nAperte '0' para sair.\nAperte qualquer outro botão para continuar: ")
    os.system("cls")

    if esc == "0":
        break

print(" Obrigado por usar o programa! ".center(45, "="))
