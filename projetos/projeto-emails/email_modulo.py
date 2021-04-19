"""Printa emails encontrados em um arquivo de texto.

Módulo que verifica a existência do arquivo inserido e, caso exista,
printa os emails encontrados nele (Caso haja algum email).
"""

import re


def verificar_arquivo(arquivo_user: str) -> str:
    """Verifica existência do arquivo de texto.
    
    Args:
        arquivo_user: caminho do arquivo inserido pelo usuário.

    Retorna:
        Retorna None caso o arquivo não exista.
        Retorna o info (conteúdo do arquivo) caso o arquivo exista.
        Caso o arquivo esteja vazio, será retornado None.
    """

    try:
        with open(arquivo_user, "r") as arquivo:
            info = arquivo.read()
    except FileNotFoundError:
        return None
    else:
        return info


def encontrar_emails(arquivo_user: str):
    """Printa emails encontrados no arquivo inserido.

    Caso o arquivo de texto exista e possua emails, eles serão
    printados em sequência.

    Args:
        arquivo_user: caminho do arquivo inserido pelo usuário.
    """

    info = verificar_arquivo(arquivo_user)

    if info:
        email_regex = re.compile(r"[\w\d\.-]+@{1}[\w\d\.-]+")
        emails_encontrados = re.findall(email_regex, info)

        if emails_encontrados:
            print("Emails encontrados:\n")

            for email in emails_encontrados:
                print(f"-> {email}")
        else:
            print("Nenhum email foi encontrado neste arquivo!")
    else:
        print("Esse arquivo não foi encontrado ou está vazio! Tente novamente!")

 