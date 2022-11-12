import pytest
import unittest
import ejercicio_leccion_2_Nicolas_serrano

#TEST CON PYTEST
def test_factorial_numero():
    m = 5
    re = 120
    assert re == ejercicio_leccion_2_Nicolas_serrano.factorial_numero(m)

def test_lista_pares():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ejercicio_leccion_2_Nicolas_serrano.lista_pares(l) == [0, 2, 4, 6, 8]

def test_numero_primo():
    t = 7
    assert ejercicio_leccion_2_Nicolas_serrano.numero_primo(t)

def test_numero_par():
    n = 6
    assert ejercicio_leccion_2_Nicolas_serrano.numero_par(n) 

def test_suma_lista_igual():
    t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    t2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ejercicio_leccion_2_Nicolas_serrano.suma_lista_igual(t1, t2)

def test_palindromo():
    p1 = 'reconocer'
    assert ejercicio_leccion_2_Nicolas_serrano.palindromo(p1)


# TEST CON UNITTEST
class PruebasconUnittest(unittest.TestCase):
    def test_factorial_numero(self):
        self.assertEqual(ejercicio_leccion_2_Nicolas_serrano.factorial_numero(5), 120)

    def test_lista_pares(self):
        self.assertEqual(ejercicio_leccion_2_Nicolas_serrano.lista_pares([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8])
        
    def test_numero_primo(self):
        self.assertEqual(ejercicio_leccion_2_Nicolas_serrano.numero_primo(10), False)

    def test_numero_par(self):
        self.assertEqual(ejercicio_leccion_2_Nicolas_serrano.numero_par(10), True)

    def test_suma_lista_igual(self):
        self.assertEqual(ejercicio_leccion_2_Nicolas_serrano.suma_lista_igual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8]), False)

    def test_palindromo(self):
        self.assertEqual(ejercicio_leccion_2_Nicolas_serrano.palindromo('reconocer'), True)


if __name__ == '__main__':
    unittest.main()