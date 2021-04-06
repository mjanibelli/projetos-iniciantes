import os

nome_arquivo = "lista.txt"

while True:
    print(" Lista de compras de mercado ".center(45, "="))

    qnt_itens = int(input("\nDigite a quantidade de itens que deseja inserir na sua lista: "))
    lista_mercado = dict()

    for item in range(qnt_itens):
        nome_item = input(f"\nDigite o nome do {item + 1}º item: ").capitalize()
        qnt_item = input(f"Digite a quantidade de {nome_item.lower()}: ")
        lista_mercado[nome_item] = qnt_item

    os.system("cls")

    print("Lista gerada com sucesso! Confira ela abaixo:\n")

    for item, quantidade in lista_mercado.items():
        print(f"Item: {item.capitalize()} -> Quantidade: {quantidade}")

    escolha = input("\n[1] -> Salvar lista\n[0] -> Sair\n[Qualquer outro botão] -> Gerar nova lista\nEscolha: ")

    if escolha == "1":
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            for item, quantidade in lista_mercado.items():
                arquivo.write(f"Item: {item.capitalize()} -> Quantidade: {quantidade}\n")

        print("\nSenha salva com sucesso! Confira em 'lista.txt' !\n")
        break
            
    elif escolha == "0":
        break

    else:
        os.system("cls")

print(" Obrigado por usar o programa! ".center(47, "="))