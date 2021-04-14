import os

import validador_modulo

print(" Validador de senhas ".center(39, "="))
print("""\nPara ser considerada válida, a senha precisa ter, no mínimo,
uma letra maiúscula, um número, um caracter especial e 8 caracteres.""")
qnt_senhas = int(input("\nDigite a quantidade de senhas a verificar: "))
os.system("cls")

for senha in range(qnt_senhas):
    senha_usuario = input(f"\nDigite a {senha + 1}º senha: ")
    
    if validador_modulo.validador_senha(senha_usuario):
        print(f"A {senha + 1}º senha é válida!")
    else:
        print(f"A {senha + 1}º senha não é válida!")

print(" Obrigado por usar o programa! ".center(47, "="))
