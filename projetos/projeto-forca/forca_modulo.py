def encaixar_letra(letra_esc, palavra_maquina, palavra_secreta):
    """Coloca a letra escolhida pelo usuário na palavra secreta, 
    no lugar e na quantidade de vezes que ela aparece na palavra escolhida pela máquina."""
    palavra_lista = list(palavra_secreta)

    for index, letra in enumerate(list(palavra_maquina)):
        if letra == letra_esc:
            palavra_lista[index] = letra_esc
        
    palavra_secreta = "".join(palavra_lista)

    return palavra_secreta
    