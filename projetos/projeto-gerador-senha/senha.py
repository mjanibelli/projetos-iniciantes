import senha_modulo

try:    
    tamanho = int(input("Digite o tamanho que deseja para sua senha: "))
except ValueError:
    print("O tamanho da senha deve ser um número inteiro! Tente novamente.")
else:

    if senha_modulo.verificar_tamanho(tamanho):
        print(f"Sua senha é: {senha_modulo.gerar_senha(tamanho)}")
    else:
        print("Tamanho inválido! Tente novamente!")
