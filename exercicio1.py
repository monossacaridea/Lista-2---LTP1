#Exercício 1: Crie uma classe base Forma com um método desenhar() que desenha uma forma qualquer utilizando a biblioteca Turte. Em seguida, crie subclasses Círculo e Quadrado que herdam de Forma e sobrescrevem desenhar() para desenhar as formas específicas.

import turtle

# Classe base Forma
class Forma:
    def desenhar():
        pass

# Subclasse Circulo
class Circulo(Forma):
    def desenhar(self): # desenha um circulo
        turtle.color("purple")
        turtle.fillcolor("purple")
        turtle.begin_fill()
        turtle.circle(50) # 50 é o raio do círculo
        turtle.end_fill()

# Subclasse Quadrado
class Quadrado(Forma):
    def desenhar(self): # desenha um quadrado
        turtle.color("pink")
        turtle.fillcolor("pink")
        turtle.begin_fill()
        for _ in range(4):  # um quadrado tem 4 lados
            turtle.forward(100)  # avança 100 pixels
            turtle.right(90)     # vira 90 graus para a direita
        turtle.end_fill()

# Criando e desenhando um círculo
circulo = Circulo()
turtle.penup()
turtle.goto(-150, 0)  # Move para a direita
turtle.pendown()
circulo.desenhar()

# Criando e desenhando um quadrado
quadrado = Quadrado()
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
quadrado.desenhar()

# Finaliza a janela ao clicar
turtle.done()
