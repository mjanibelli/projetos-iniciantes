"""Mostra aviso no terminal."""
import os
import time


def aviso(mensagem: str):
    """Printa a mensagem de aviso por um tempo e limpa o terminal.
    
    Args:
        mensagem: Mensagem que vai ser printada.
    """
    print(mensagem)
    time.sleep(2.3)
    os.system("cls")