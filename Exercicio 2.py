# Crie classes Motor, Pneu, Veiculo, onde Veiculo herda tanto de Motor quanto de Pneu.
# Ambas as classes base (Motor e Pneu) devem ter um método chamado status() que retorna uma string.
# A classe Veiculo deve também ter um método status() que chama os métodos status() das classes base.
# Implemente a herança de modo que a classe Veiculo resolva o método status() de maneira correta.

# Classe Motor
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo  # tipo do motor (eletrico, a gasolina)
        self.potencia = potencia  # hp

    def status(self): # retorna o status do motor
        return f"Motor do tipo {self.tipo} com potência de {self.potencia}."

# Classe Pneu
class Pneu:
    def __init__(self, tamanho, tipo):
        self.tamanho = tamanho  # tamanho do pneu (195/65R15)
        self.tipo = tipo  # tipo de pneu (radial)

    def status(self): #retorna o status do pneu
        return f"Pneu do tipo {self.tipo} com tamanho {self.tamanho}."

# Classe Veículo
class Veiculo(Motor, Pneu):
    def __init__(self, tipo_motor, potencia_motor, tamanho_pneu, tipo_pneu):
        # inicializa as classes base (Motor e Pneu):
        Motor.__init__(self, tipo_motor, potencia_motor)
        Pneu.__init__(self, tamanho_pneu, tipo_pneu)

    def status(self): # retorna o status do veículo, chamando os status das classes motor e pneu
        motor_status = Motor.status(self)
        pneu_status = Pneu.status(self)
        return f"Veículo: {motor_status} | {pneu_status}"

# Objeto da classe Veiculo
veiculo = Veiculo("Gasolina", "200 HP", "195/65R15", "Radial")
print(veiculo.status())
