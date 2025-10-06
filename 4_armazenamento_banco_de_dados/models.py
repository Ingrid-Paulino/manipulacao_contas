class Conta():
    # Construtor
    def __init__(self, id, nome, saldo):
        # Atributos da classe
        self.id = id
        self.nome = nome
        self.saldo = saldo

    # Métodos
    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        self.saldo -= valor

    def retornar_lista(self):
        return [self.id, self.nome, self.saldo]

    def __str__(self):
        return f"{self.id} {self.nome} {self.saldo}"
    
'''
conta1 = Conta(1, "LP", 100)
conta1.creditar(10)
print(conta1)
print()
conta2 = Conta(2, "Luan", 200)
conta2.debitar(50)
print(conta2)
'''

##FORMA 2
# from dataclasses import dataclass

# @dataclass
# class Conta:
#     id: int
#     nome: str
#     saldo: float

#     def creditar(self, valor: float):
#         self.saldo += valor

#     def debitar(self, valor: float):
#         self.saldo -= valor

#     def __str__(self):
#         return f"{self.id} {self.nome} {self.saldo}"
    
# conta = Conta(1, "LP", 100)
# conta.id = 2
# print(conta)