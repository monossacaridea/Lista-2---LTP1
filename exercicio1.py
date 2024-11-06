#Exercício 1: Crie uma classe base Forma com um método desenhar() que desenha uma forma qualquer utilizando a biblioteca Turte. Em seguida, crie subclasses Círculo e Quadrado que herdam de Forma e sobrescrevem desenhar() para desenhar as formas específicas.

import turtle

class Forma:
    def desenhar():
        # método para desenhar a forma. deve ser sobrescrito pelas subclasses.
        pass

class Circulo(Forma):
    def desenhar(self):
        # desenha um círculo usando a biblioteca turtle
        turtle.circle(50) # 50 é o raio do círculo

class Quadrado(Forma):
    def desenhar(self):
        # desenha um quadrado usando a biblioteca turtle
        for _ in range(4):  # um quadrado tem 4 lados
            turtle.forward(100)  # avança 100 pixels
            turtle.right(90)     # vira 90 graus para a direita

# Criando e desenhando um círculo
circulo = Circulo()
turtle.penup()
turtle.goto(-75, 0)  # Move para a direita
turtle.pendown()
circulo.desenhar()

# Criando e desenhando um quadrado
quadrado = Quadrado()
turtle.penup()
turtle.goto(-75, 0)
turtle.pendown()
quadrado.desenhar()

# Finaliza a janela ao clicar
turtle.done()
