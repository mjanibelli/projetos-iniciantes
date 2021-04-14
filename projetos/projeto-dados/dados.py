from dados_modulo import rolar_dado

print(" Rolagem de dados ".center(50, "="))

while True:
    print("\nMenu:\n[1] -> D6\n[2] -> D8\n[3] -> D10\n[4] -> D12\n[5] -> D20")

    try:
        escolha = int(input("Digite o que deseja: "))
    except ValueError:
        print("Essa escolha não existe! Tente novamente!")
        continue

    if escolha == 1:
        print(f"D6: {rolar_dado(6)}")
    elif escolha == 2:
        print(f"D8: {rolar_dado(8)}")
    elif escolha == 3:
        print(f"D10: {rolar_dado(10)}")
    elif escolha == 4:
        print(f"D12: {rolar_dado(12)}")
    elif escolha == 5:
        print(f"D20: {rolar_dado(20)}")
    else:
        print("Esssa escolha não existe! Tente novamente!")
