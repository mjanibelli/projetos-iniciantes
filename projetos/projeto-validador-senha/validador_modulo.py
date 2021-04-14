"""Valida as senhas.

Atributos:
    maiuscula_regex (str): Regex para letras maiúsculas.
    numero_regex (str): Regex para números.
    char_especial_regex (str): Regex para caracteres especias.
    tamanho_regex (str): Regex para o tamanho.
"""

import re

maiuscula_regex = r"[A-Z]+"
numero_regex = r"\d+"
char_especial_regex = r"[^A-Za-z0-9]"
tamanho_regex = r".{8,}"


def validador_senha(senha: str) -> bool:
    """Verifica se a senha inserida é válida.
    
    Args: 
        senha: Senha a ser verificada.
    
    Retorna:
        True: Caso a senha seja válida.
        False: Caso a senha não seja válida.
    """

    maisc_encontrada = re.search(maiuscula_regex, senha)
    num_encontrado = re.search(numero_regex, senha)
    chars_encontrado = re.search(char_especial_regex, senha)
    tam_encontrado = re.search(tamanho_regex, senha)

    if maisc_encontrada and num_encontrado and chars_encontrado and tam_encontrado:
        return True
    else:
        return False
