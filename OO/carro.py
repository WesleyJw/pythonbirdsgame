class Carro:

    # Classe motor

    class Motor:

        def __init__(self):
            self.velocidade = 0

        def acelerar(self):
            self.velocidade += 1

            return self.velocidade

        def frear(self):
            self.velocidade -= 2

            if (self.velocidade < 0):
                self.velocidade = 0

            return self.velocidade

    # Classe direcao

    class Direcao:

        def __init__(self):
            self.position = 0
            self.direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
            self.valor = self.direcoes[self.position]

        def girar_a_direita(self):

            self.position += 1
            if self.position >= 4:
                self.position = 0
            self.valor = self.direcoes[self.position]

            return self.valor

        def girar_a_esquerda(self):
            self.position -= 1

            if self.position < 0:
                self.position = 3
            self.valor = self.direcoes[self.position]

            return self.valor


if __name__ == "__main__":

    # Teste classe Motor
    carro = Carro()
    motor = carro.Motor()
    print("A velocidade é:", motor.velocidade)
    motor.acelerar()
    print("A velocidade é:", motor.velocidade)
    motor.acelerar()
    print("A velocidade é:", motor.velocidade)
    motor.acelerar()
    print("A velocidade é:", motor.velocidade)
    motor.frear()
    print("A velocidade é:", motor.velocidade)
    motor.frear()
    print("A velocidade é:", motor.velocidade)

    # Teste classe Direcao

    direcao = carro.Direcao()
    print("Virando a Direita")
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_direita()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_direita()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_direita()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_direita()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_direita()
    print("A direcao é: ", direcao.valor)

    print("Virando a Esquerda")
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_esquerda()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_esquerda()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_esquerda()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_esquerda()
    print("A direcao é: ", direcao.valor)
    direcao.girar_a_esquerda()

