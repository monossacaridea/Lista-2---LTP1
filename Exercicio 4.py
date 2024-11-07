# Exercicio 4: Criar um sistema de simulação bancária onde diferentes tipos de contas compartilham algumas operações comuns.
# Regras:
# Defina uma classe abstrata ContaBancaria com métodos abstratos para depositar, sacar e calcular saldo.
# Crie duas subclasses concretas, ContaCorrente e ContaPoupanca.
# A ContaCorrente deve permitir um saldo negativo até um certo limite (cheque especial).
# A ContaPoupanca não deve permitir saldo negativo e deve calcular juros sobre o saldo atual.
# Implementar métodos para exibir informações da conta.
# As contas devem ter atributos como número da conta, titular e saldo.
# A função sacar de ContaPoupanca deve recusar a operação se o saldo ficar negativo.

from abc import ABC, abstractmethod

# Classe abstrata
class ContaBancaria(ABC):
    def __init__(self, numero_conta, titular, saldo_inicial=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def calcular_saldo(self):
        pass

    def exibir_informacoes(self):
        print(f"Conta: {self.numero_conta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")

# Subclasse ContaCorrente
class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo_inicial=0.0, limite_cheque_especial=1000.0):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and (self.saldo - valor) >= -self.limite_cheque_especial:
            self.saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    def calcular_saldo(self):
        return self.saldo

# Subclasse ContaPoupanca
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo_inicial=0.0, taxa_juros=0.05):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and (self.saldo - valor) >= 0:
            self.saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    def calcular_saldo(self):
        return self.saldo * (1 + self.taxa_juros)

# Teste das classes
cc = ContaCorrente("001", "Beatriz", 500, 1000)
cp = ContaPoupanca("002", "Gabriela", 1000, 0.03)

# Exibindo as contas
cc.exibir_informacoes()
cp.exibir_informacoes()

# Realizando depósitos e saques
cc.depositar(200)
cp.depositar(500)

cc.sacar(300)
cp.sacar(200)

# Calculando e exibindo o saldo após os juros para a conta poupança
print(f"Saldo da Conta Corrente: R$ {cc.calcular_saldo():.2f}")
print(f"Saldo da Conta Poupança após juros: R$ {cp.calcular_saldo():.2f}")

# Exibindo as contas novamente
cc.exibir_informacoes()
cp.exibir_informacoes()
