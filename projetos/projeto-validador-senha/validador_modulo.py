import re

maiuscula_regex = r"[A-Z]+"
numero_regex = r"\d+"
char_especial_regex = r"[^A-Za-z0-9]"
tamanho_regex = r".{8,}"


def validador_senha(senha: str) -> bool:
    maisc_encontrada = re.search(maiuscula_regex, senha)
    num_encontrado = re.search(numero_regex, senha)
    chars_encontrado = re.search(char_especial_regex, senha)
    tam_encontrado = re.search(tamanho_regex, senha)

    if maisc_encontrada and num_encontrado and chars_encontrado and tam_encontrado:
        return True
    else:
        return False
