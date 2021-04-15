"""Altera palavra_secreta."""


def encaixar_letra(letra_esc: str, palavra_maquina: str,
                    palavra_secreta: str) -> str:
    """Realiza a troca de caracteres em palavra_secreta.
    
    Muda o caracter '_' (underline) de uma posição por letra_esc.

    Args:
        letra_esc: Letra inserida pelo usuário.
        palavra_maquina: Palavra escolhida pelo programa.
        palavra_secreta: Palavra formada inicialmente por '_'
                (underlines), que vai ser mudada pela função.
                    
    Retorna:
        Retorna a palavra_secreta já com as alterações feitas.
    """

    palavra_lista = list(palavra_secreta)

    for index, letra in enumerate(list(palavra_maquina)):
        if letra == letra_esc:
            palavra_lista[index] = letra_esc
        
    palavra_secreta = "".join(palavra_lista)

    return palavra_secreta
