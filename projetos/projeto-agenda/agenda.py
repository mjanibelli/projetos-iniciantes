import agenda_modulo

print(" Programa de agenda ".center(40, "="))
info = agenda_modulo.carregar_info()

if info:
    print("Seus compromissos salvos na agenda são:\n")

    for data, compromisso in info.items():
        print(f"{data} -> {compromisso}")
else:
    print("Nenhum compromisso foi salvo ainda!")

while True:
    escolha = input("\nAperte 0 para sair. Aperte qualquer outro botão para salvar um novo compromisso.")

    if escolha == "0":
        break
    else:
        data_agend = input("\nDigite a data do seu compromisso (Dia/Mês/Ano): ")
        compro_agend = input("Digite o seu compromisso: ")

        agenda_modulo.salvar_info(data_agend, compro_agend)
        print(f"\nCompromisso para o dia {data_agend} foi salvo com sucesso!")

print(" Obrigado por usar o programa! ".center(45, "="))
