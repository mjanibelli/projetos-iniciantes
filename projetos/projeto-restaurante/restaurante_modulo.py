"""Módulo para simular um restaurante"""


class Restaurante:
    """Classe que representa um restaurante.

    Atributos:
        nome (str): Nome do restaurante.
        rendimento (float): Rendimento do restaurante. Default = 0.0
        clientes (int): Número de clientes atendidos. Default = 0
    """

    def __init__(self, nome):
        """Inicializa as variáveis de instância."""
        self.nome = nome
        self.rendimento = 0.0
        self.clientes = 0

    def atender_cliente(self, preco_produto: float) -> bool:
        """Simula o atendimento a um único cliente.
        
        Args:
            preco_produto: Preço da refeição do cliente.
        
        Retorna:
            True, caso preco_produto seja positivo.
            False, caso preco_produto seja negativo.
        """
        
        if preco_produto > 0:
            self.rendimento += preco_produto
            self.clientes += 1

            return True
        else:
            return False

    def gerar_resultado(self):
        print(f"O {self.nome} atendeu {self.clientes} cliente(s) e gerou R$ {self.rendimento}")
