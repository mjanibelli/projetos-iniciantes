"""Simula rolagem de um dado."""
from random import randint


def rolar_dado(faces: int) -> int:
    """Retorna o número sorteado.
    
    Args:
        faces: Número de faces que o dado possui.

    Retorna:
        Retorna um número aleatório entre 1 e o número de faces do dado.
    """

    return randint(1, faces)


