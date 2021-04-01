import json

nome_arquivo = "agenda.json"

def carregarInfo():
    try:
        with open(nome_arquivo) as arquivo:
            info = json.load(arquivo)
    except FileNotFoundError:
        return None
    else:
        return info


def salvarInfo(data, compromisso):
    info = carregarInfo()

    if info:
        info[data] = compromisso
        with open(nome_arquivo, "w") as arquivo:
            json.dump(info, arquivo, sort_keys=True, indent=4)
    else:
        info = {data : compromisso}
        with open(nome_arquivo, "w") as arquivo:
            json.dump(info, arquivo, sort_keys=True, indent=4)