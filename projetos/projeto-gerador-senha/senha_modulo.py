import random
import string

alfabeto = list(string.ascii_letters)
numeros = list(string.digits)
chars_especiais = list(string.punctuation)


def verificar_tamanho(tamanho_senha):
    """Verifica o tamanho da senha. Caso ela tenha menos que 10 caracteres, retorna False."""
    if int(tamanho_senha) < 10:
        return False
    else:
        return True


def gerar_senha(tamanho_senha):
    """Gera a senha final."""
    senha_lista = []
    pedaco_senha = tamanho_senha // 3

    for _ in range(0, pedaco_senha):
        letra = random.choice(alfabeto)
        senha_lista.append(letra)

    for _ in range(pedaco_senha, (pedaco_senha * 2)):
        numero = random.choice(numeros)
        senha_lista.append(numero)

    for _ in range((pedaco_senha * 2), tamanho_senha):
        char_espec = random.choice(chars_especiais)
        senha_lista.append(char_espec)

    random.shuffle(senha_lista)

    return "".join(senha_lista)
