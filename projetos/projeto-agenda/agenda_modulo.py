import json

nome_arquivo = "agenda.json"


def carregar_info():
    try:
        with open(nome_arquivo) as arquivo:
            info = json.load(arquivo)
    except FileNotFoundError:
        return None
    else:
        return info


def salvar_info(data, compromisso):
    info = carregar_info()

    if info:
        info[data] = compromisso
        with open(nome_arquivo, "w") as arquivo:
            json.dump(info, arquivo, sort_keys=True, indent=4)
    else:
        info = {data: compromisso}
        with open(nome_arquivo, "w") as arquivo:
            json.dump(info, arquivo, sort_keys=True, indent=4)
