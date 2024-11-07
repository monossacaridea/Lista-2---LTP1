# Exercicio 3: Implemente uma classe Ponto com um construtor que aceita coordenadas x e y como atributos.
# Utilize o objeto ponto como parâmetro para o comando goto() da Turtle.

import turtle

class Ponto:
    def __init__(self, x, y):
        self.x = x # coordenada x
        self.y = y # coordenada y

    def __str__(self): # exibir como string
        return f"ponto({self.x}, {self.y})"

def desenhar_ponto(ponto):
    t = turtle.Turtle()
    t.penup() # mover sem desenhar
    t.goto(ponto.x, ponto.y) # vai até as coordenadas x e y
    t.pendown()
    t.dot(10, 'red') # tamanho e cor do ponto (para melhor visualização)

# Solicita ao usuário que entre com os valores de x e y
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

# Objeto ponto
p1 = Ponto(x, y)

desenhar_ponto(p1)

turtle.done()
