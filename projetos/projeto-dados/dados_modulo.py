"""Módulo que contem uma função para simular a rolagem de um dado de N faces."""
from random import randint


def rolar_dado(faces):
    """Rola um dado com uma quantidade determinada de faces."""
    return randint(1, faces)
