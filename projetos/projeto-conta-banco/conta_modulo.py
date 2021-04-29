"""Módulo para simular uma conta bancária."""


class ContaBancaria:
    """Classe que representa uma conta bancária.
    
    Atributos:
        nome (str): Primeiro nome do usuário.
        sobrenome (str): Último nome do usuário.
        saldo (float): Saldo dispoível na conta. Default = 0.0
    """

    def __init__(self, nome, sobrenome):
        """Inicializa os atributos.
        
        Args:
            nome (str): Primeiro nome do usuário.
            sobrenome (str): Último nome do usuário.
        """
        
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.saldo = 0.0

    def mostrar_conta(self):
        """Printa as informações sobre a conta."""
        print(f"Nome: {self.nome}\nSobrenome: {self.sobrenome}")
        print(f"Saldo: R$ {self.saldo}")

    def depositar(self, quantia):
        """Adiciona uma quantia ao saldo da conta.
        
        Args:
            quantia (float): Quantia a ser adicionada.

        Retorna: 
            self.saldo, caso a quantia seja maior do que zero.
            None, caso a quantia seja menor ou igual a zero.
        """

        if quantia > 0:
            self.saldo += quantia
            return self.saldo
        else:
            return None
        
    def sacar(self, quantia):
        """Retira uma quantia do saldo da conta.
        
        Args:
            quantia (float): Quantia a ser retirada.

        Retorna:
            self.saldo, caso a quantia seja menor que o saldo e maior que 0.
            None, caso a quantia seja maior que o saldo ou menor ou igual a 0.
        """

        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            return self.saldo
        else:
            return None
