"""Manipula o arquivo .json.

Módulo que possui funções para carregar o dicionário contido no arquivo, 
e para salvar o dicionário no arquivo.

Atributos:
    nome_arquivo (str): Nome do arquivo .json a ser manipulado.
"""

import json

nome_arquivo = "agenda.json"


def carregar_info() -> dict:
    """Caso haja arquivo, carrega o dict contido nele e o retorna.
    
    Retorna: 
        Um dicionário, caso o arquivo exista
        None, caso o arquivo não exista
    """

    try:
        with open(nome_arquivo) as arquivo:
            info = json.load(arquivo)
    except FileNotFoundError:
        return None
    else:
        return info


def salvar_info(data: str, compromisso: str):
    """Transforma data e compromisso em um dict e salva ele em um arquivo .json.

    Args:
        data: Representação, em string, de uma data.
        compromisso: Uma string que descreve um compromisso    
    """

    info = carregar_info()

    if info:
        info[data] = compromisso
        with open(nome_arquivo, "w") as arquivo:
            json.dump(info, arquivo, sort_keys=True, indent=4)
    else:
        info = {data: compromisso}
        with open(nome_arquivo, "w") as arquivo:
            json.dump(info, arquivo, sort_keys=True, indent=4)
