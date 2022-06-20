"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
O Motor terá a responsabilidade de controlar a velocidade.
Ele oforece os seguintes atributos:
a) Atributo de dado velocidade
b) Metodo acelerar, que devera incrementar a velocidade de um unidade
c) Metodo frear que  deverar decrementar a velocidade em duas unidades.


2) Direção
A direcao tera a responsabilidade de controlar a direcao.
Ela oferece os seguintes atributos
a) Valor de derecao com os valores possiveis: Norte, Sul, Leste, Oeste
b)Metodo girar_a_direita
c) Metodo girar_a_esquerda

    # Testando o motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    # Tentando a direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    # Classe carro
    >>> carro = Carro(motor, direcao)
    >>> carro.calcular_velocidade
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade
    1
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
"""


class Carro:

    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1


    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

# Classe direcao

class Direcao:

    rotacao_a_direita_dict = {
        'Norte': 'Leste',
        'Leste': 'Sul',
        'Sul': 'Oeste',
        'Oeste': 'Norte'
    }

    rotacao_a_esquerda_dict = {
        'Norte': 'Oeste',
        'Oeste': 'Sul',
        'Sul': 'Leste',
        'Leste': 'Norte'
    }

    def __init__(self):
        self.valor = 'Norte'

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]



