class ContaBancaria:

    def __init__(self, nome, sobrenome):
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.saldo = 0.0

    def mostrar_conta(self):
        print(f"Nome: {self.nome}\nSobrenome: {self.sobrenome}")
        print(f"Saldo: R$ {self.saldo}")

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            return self.saldo
        else:
            return None
        
    def sacar(self, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            return self.saldo
        else:
            return None