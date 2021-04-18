print(" Calculadora de Equação do 2º grau ".center(49, "="))

while True:
    coef_a = int(input("\nDigite o valor do coeficiente A: "))

    if coef_a == 0:
        print("""\nA equação não pode ser considerada de 2º grau!\nO coeficiente 'a' precisa ser diferente de 0!""")
        continue

    coef_b = int(input("Digite o valor do coeficiente B: "))
    coef_c = int(input("Digite o valor do coeficiente C: "))
    delta = ((coef_b**2) -4 * coef_a * coef_c)
    raiz1 = ((-coef_b + delta**0.5) / (2*coef_a))  # delta**0.5 é raiz quadrada de delta.
    raiz2 = ((-coef_b - delta**0.5) / (2*coef_a))
        
    if delta < 0:
        print(f"\nDelta: {delta}")
        print("Não existem raizes reais para essa equação!\n")
    elif delta == 0:
        print(f"\nDelta: {delta}")
        print("Existem duas raízes reais iguais para essa equação!\n")
        print(f"Raiz da equação: {raiz1}\n")
    else:
        print(f"\nDelta: {delta}")
        print("Existem duas raízes reais distintas para essa equação!\n")
        print(f"Primeira raiz: {raiz1:.1f}\nSegunda raiz: {raiz2:.1f}\n")

    continuar = input("""Aperte '0' para sair. Aperte qualquer outro botão para continuar: """)

    if continuar == "0":
        break

print("Obrigado por usar o programa!")
