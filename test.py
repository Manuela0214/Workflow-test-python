import unittest

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

class TestOperacionesMatematicas(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 5), 8)
        self.assertEqual(sumar(-2, 7), 5)
        self.assertEqual(sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 3), 7)
        self.assertEqual(restar(5, -2), 7)
        self.assertEqual(restar(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 4), 8)
        self.assertEqual(multiplicar(-3, 6), -18)
        self.assertEqual(multiplicar(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
