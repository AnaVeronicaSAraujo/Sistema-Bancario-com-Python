from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        print(f"Depósito de R${self.valor} realizado com sucesso.")
        conta.historico.adicionar_transacao(f"Depósito de R${self.valor}")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            print(f"Saque de R${self.valor} realizado com sucesso.")
            conta.historico.adicionar_transacao(f"Saque de R${self.valor}")
        else:
            print(f"Saldo insuficiente para realizar o saque de R${self.valor}")

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        self.transacoes.append(descricao)

    def exibir(self):
        for transacao in self.transacoes:
            print(transacao)

class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def exibir_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        self.saldo += valor

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Testando o sistema bancário
if __name__ == "__main__":
    cliente = PessoaFisica("Rua Edson Evangelista, 140", "000.000.000-00", "Ana Verônica", date(1999, 12, 05))
    conta_corrente = ContaCorrente(cliente, 1001, "0001", limite=500.0, limite_saques=3)

    cliente.adicionar_conta(conta_corrente)

    deposito = Deposito(250.0)
    cliente.realizar_transacao(conta_corrente, deposito)

    saque = Saque(100.0)
    cliente.realizar_transacao(conta_corrente, saque)

    print(f"Saldo atual: R${conta_corrente.exibir_saldo()}")
    print("Histórico de transações:")
    conta_corrente.historico.exibir()
