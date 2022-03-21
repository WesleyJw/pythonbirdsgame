from unittest import TestCase
from OO.carro import Carro

## Criando scprit com a bilbioteca unittest

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Carro.Motor()
        print(motor.velocidade)
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Carro.Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)