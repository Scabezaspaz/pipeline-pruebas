import unittest

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.calc = Calculadora()

    def test_sumar_dos_positivos(self):
        resultado = self.calc.sumar(2, 3)
        self.assertEqual(resultado, 5)

    def test_restar(self):
        resultado = self.calc.restar(6, 2)
        self.assertEqual(resultado, 4)

    def test_multiplicar(self):
        resultado = self.calc.multiplicar(5, 4)
        self.assertEqual(resultado, 20)

    def test_dividir(self):
        resultado = self.calc.dividir(15, 3)
        self.assertEqual(resultado, 5)

if __name__ == '__main__':
    unittest.main()