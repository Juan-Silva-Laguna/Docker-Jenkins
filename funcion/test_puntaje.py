# test_puntaje.py

import unittest
from calcular_puntaje import calcular_puntaje

class TestCalcularPuntaje(unittest.TestCase):

    def test_varias_combinaciones(self):
        # Arrange
        datos = [
            (4.0, 4.0, 12, True, 3.3),
            (5.0, 5.0, 0, False, 5.0),
            (2.0, 3.0, 9, False, 1.6),
            (2.0, 3.0, 9, True, 2.1)
        ]
        # Act & Assert
        for nota_teoria, nota_practica, asistencias, entrego, esperado in datos:
            resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
            self.assertEqual(resultado, esperado)

class TestCalcularPuntajeIndividual(unittest.TestCase):

    def test_caso_1(self):
        # Arrange
        nota_teoria, nota_practica, asistencias, entrego = 5.0, 4.5, 0, False
        esperado = 4.75
        # Act
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        # Assert
        self.assertEqual(resultado, esperado)

    def test_caso_2(self):
        nota_teoria, nota_practica, asistencias, entrego = 3.5, 4.0, 2, False
        esperado = 3.55
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_3(self):
        nota_teoria, nota_practica, asistencias, entrego = 4.0, 4.0, 5, True
        esperado = 4.0
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_4(self):
        nota_teoria, nota_practica, asistencias, entrego = 2.0, 3.0, 7, False
        esperado = 1.8
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_5(self):
        nota_teoria, nota_practica, asistencias, entrego = 4.8, 5.0, 1, False
        esperado = 4.8
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_6(self):
        nota_teoria, nota_practica, asistencias, entrego = 1.0, 2.0, 10, False
        esperado = 0.5
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_7(self):
        nota_teoria, nota_practica, asistencias, entrego = 3.5, 3.5, 0, True
        esperado = 4.0
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_8(self):
        nota_teoria, nota_practica, asistencias, entrego = 4.2, 4.3, 3, False
        esperado = 3.95
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_9(self):
        nota_teoria, nota_practica, asistencias, entrego = 2.5, 3.5, 8, False
        esperado = 2.2
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_10(self):
        nota_teoria, nota_practica, asistencias, entrego = 5.0, 5.0, 2, True
        esperado = 5.3
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_11(self):
        nota_teoria, nota_practica, asistencias, entrego = 3.8, 3.8, 4, False
        esperado = 3.4
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_12(self):
        nota_teoria, nota_practica, asistencias, entrego = 2.0, 2.0, 6, False
        esperado = 1.4
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_13(self):
        nota_teoria, nota_practica, asistencias, entrego = 4.5, 4.5, 1, True
        esperado = 4.9
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_14(self):
        nota_teoria, nota_practica, asistencias, entrego = 1.5, 2.5, 10, False
        esperado = 1.0
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_15(self):
        nota_teoria, nota_practica, asistencias, entrego = 3.0, 4.0, 4, True
        esperado = 3.6
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_16(self):
        nota_teoria, nota_practica, asistencias, entrego = 4.0, 4.0, 9, False
        esperado = 3.1
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_17(self):
        nota_teoria, nota_practica, asistencias, entrego = 2.0, 3.0, 7, True
        esperado = 2.3
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_18(self):
        nota_teoria, nota_practica, asistencias, entrego = 3.5, 3.0, 2, False
        esperado = 3.05
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_19(self):
        nota_teoria, nota_practica, asistencias, entrego = 5.0, 5.0, 0, True
        esperado = 5.5
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

    def test_caso_20(self):
        nota_teoria, nota_practica, asistencias, entrego = 3.0, 3.0, 5, False
        esperado = 2.5
        resultado = calcular_puntaje(nota_teoria, nota_practica, asistencias, entrego)
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
