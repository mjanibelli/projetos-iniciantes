import os
import pathlib

import renomear_modulo

print(" Renomeador de arquivos ".center(40, "="))
qnt_arquivos = int(input("\nDigite quantos arquivos deseja renomear: "))

for arquivo in range(qnt_arquivos):
    dir_antigo = pathlib.Path(input("Digite o diretório do arquivo a ser renomeado ou arraste-o: "))
    os.system("cls")

    if os.path.exists(dir_antigo):
        nome_novo = input("Digite o novo nome do arquivo: ") + dir_antigo.suffix
        dir_novo = os.path.join(os.path.dirname(dir_antigo), nome_novo)

        try:       
            os.rename(dir_antigo, dir_novo)
        except:
            renomear_modulo.aviso(f"\nO arquivo '{nome_novo}{dir_antigo.suffix}' já existe!")
        else:
            renomear_modulo.aviso("\nArquivo renomeado com sucesso!")
    else:
        renomear_modulo.aviso("Arquivo não encontrado!")

print(" Obrigado por usar o programa! ".center(45, "="))