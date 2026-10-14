"""Pruebas del modelo matemático; T-003 se amplía con cada función nueva."""

from decimal import Decimal
from fractions import Fraction
import unittest

from src.matematica import (
    INTERVALO_EJEMPLO,
    N_SUBINTERVALOS_EJEMPLO,
    PARTICION_EJEMPLO,
    funcion_ejemplo,
)


class TestFuncionEjemplo(unittest.TestCase):
    def test_valores_acordados(self):
        for x, esperado in ((0, 1), (0.5, 1.25), (1, 2), (1.5, 3.25), (2, 5)):
            with self.subTest(x=x):
                self.assertEqual(funcion_ejemplo(x), esperado)

    def test_otros_valores_numericos_del_intervalo(self):
        for x, esperado in (
            (0.25, 1.0625),
            (Decimal("0.5"), Decimal("1.25")),
            (Fraction(3, 2), Fraction(13, 4)),
        ):
            with self.subTest(x=x):
                self.assertEqual(funcion_ejemplo(x), esperado)

    def test_datos_del_ejemplo_principal(self):
        self.assertEqual(PARTICION_EJEMPLO, (0, 0.5, 1, 1.5, 2))
        self.assertEqual(INTERVALO_EJEMPLO, (0, 2))
        self.assertEqual(N_SUBINTERVALOS_EJEMPLO, 4)


if __name__ == "__main__":
    unittest.main()
