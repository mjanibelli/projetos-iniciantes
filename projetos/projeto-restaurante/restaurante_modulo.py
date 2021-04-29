class Restaurante:

    def __init__(self, nome):
        self.nome = nome
        self.rendimento = 0
        self.clientes = 0

    def atender_cliente(self, preco_produto):
        if preco_produto > 0:
            self.rendimento += preco_produto
            self.clientes += 1

            return True
        else:
            return False

    def gerar_resultado(self):
        print(f"O {self.nome} atendeu {self.clientes} cliente(s) e gerou R$ {self.rendimento}")
