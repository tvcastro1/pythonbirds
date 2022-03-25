from unittest import TestCase
from OO.carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_aceleracao(self):
        motor = Motor()
        motor.acelerar()
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
