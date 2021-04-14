"""Módulo com funções que salvam e carregam informações sobre a agenda."""

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

    Parâmetros:
        data (str): Representação, em string, de uma data.
        compromisso (str): Uma string que descreve um compromisso    
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
