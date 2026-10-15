"""Pruebas del modelo matemático; T-003 se amplía con cada función nueva."""

from decimal import Decimal
from fractions import Fraction
import unittest

from src.matematica import (
    calcular_rectangulos,
    INTERVALO_EJEMPLO,
    N_SUBINTERVALOS_EJEMPLO,
    PARTICION_EJEMPLO,
    crear_particion_uniforme,
    funcion_ejemplo,
    seleccionar_muestra,
    validar_particion,
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


class TestValidarParticion(unittest.TestCase):
    def test_acepta_particiones_validas(self):
        for p in (
            [0, 0.5, 1, 1.5, 2],
            (0, 0.5, 1, 1.5, 2),
            [0, 0.1, 0.5, 2],
            [-3, -1, 0, 7.5],
            [0, 1],
            [Fraction(0), Fraction(1, 3), Decimal("1.5")],
        ):
            with self.subTest(p=p):
                self.assertEqual(validar_particion(p), tuple(p))

    def test_rechaza_entradas_invalidas(self):
        for p in (
            [], (), [1], [0, 0], [0, 1, 1, 2], [2, 1, 0], [0, 2, 1],
            [0, "1"], [0, None], [0, True], [0, 1j], "012", None, 5,
            {0, 1, 2}, [0, float("nan"), 2], [0, float("inf")],
            [float("-inf"), 0], [0, Decimal("NaN")],
        ):
            with self.subTest(p=p):
                with self.assertRaises(ValueError):
                    validar_particion(p)

    def test_no_modifica_la_secuencia(self):
        p = [0, 0.5, 1]
        copia = list(p)
        validar_particion(p)
        self.assertEqual(p, copia)

class TestCrearParticionUniforme(unittest.TestCase):
    def test_ejemplo_principal(self):
        self.assertEqual(crear_particion_uniforme(0, 2, 4), PARTICION_EJEMPLO)

    def test_n_8_y_16(self):
        for n in (8, 16):
            with self.subTest(n=n):
                p = crear_particion_uniforme(0, 2, n)
                self.assertEqual(len(p), n + 1)
                self.assertEqual((p[0], p[-1]), (0, 2))
                for i, x in enumerate(p):
                    self.assertEqual(x, 2 * i / n)  # exacto en binario

    def test_extremos_exactos_sin_redondeo(self):
        p = crear_particion_uniforme(0, 1, 3)
        self.assertEqual((p[0], p[-1]), (0, 1))
        self.assertEqual(p[1], 1 / 3)
        p = crear_particion_uniforme(Fraction(0), Fraction(1), 3)
        self.assertEqual(p[1], Fraction(1, 3))
        self.assertEqual(crear_particion_uniforme(-1, 1, 2), (-1, 0, 1))

    def test_resultado_es_particion_valida(self):
        p = crear_particion_uniforme(0.1, 0.7, 7)
        self.assertEqual(validar_particion(p), p)

    def test_rechaza_n_invalido(self):
        for n in (0, -1, -4, 2.5, 4.0, "4", None, True):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    crear_particion_uniforme(0, 2, n)

    def test_rechaza_limites_invalidos(self):
        for a, b in (
            (2, 0), (1, 1), (float("nan"), 1), (0, float("inf")),
            (float("-inf"), 0), ("0", 1), (0, None),
        ):
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    crear_particion_uniforme(a, b, 4)

class TestSeleccionarMuestra(unittest.TestCase):
    def test_izquierda_y_derecha(self):
        self.assertEqual(seleccionar_muestra(1, 1.5, "izquierda"), 1)
        self.assertEqual(seleccionar_muestra(1, 1.5, "derecha"), 1.5)

    def test_rechaza_criterio_desconocido(self):
        for c in ("centro", "", "Izquierda", None, 1):
            with self.subTest(criterio=c):
                with self.assertRaises(ValueError):
                    seleccionar_muestra(1, 1.5, c)

    def test_rechaza_intervalo_invalido(self):
        for a, b in ((1.5, 1), (1, 1)):
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    seleccionar_muestra(a, b, "izquierda")

class TestCalcularRectangulos(unittest.TestCase):
    def test_izquierda(self):
        r = calcular_rectangulos(funcion_ejemplo, PARTICION_EJEMPLO, "izquierda")
        self.assertEqual(len(r), 4)
        self.assertEqual([x["altura"] for x in r], [1, 1.25, 2, 3.25])
        self.assertEqual([x["aporte"] for x in r], [0.5, 0.625, 1, 1.625])

    def test_derecha(self):
        r = calcular_rectangulos(funcion_ejemplo, PARTICION_EJEMPLO, "derecha")
        self.assertEqual([x["altura"] for x in r], [1.25, 2, 3.25, 5])
        self.assertEqual([x["aporte"] for x in r], [0.625, 1, 1.625, 2.5])

    def test_formato_y_orden(self):
        r = calcular_rectangulos(funcion_ejemplo, (0, 1, 3), "derecha")
        self.assertEqual(r[0], {"izquierda": 0, "derecha": 1, "muestra": 1,
                                "ancho": 1, "altura": 2, "aporte": 2})
        self.assertEqual(r[1]["ancho"], 2)  # ancho propio, no uniforme
        self.assertEqual(r[1]["aporte"], 20)

    def test_no_modifica_particion(self):
        p = [0, 0.5, 1]
        calcular_rectangulos(funcion_ejemplo, p, "izquierda")
        self.assertEqual(p, [0, 0.5, 1])

    def test_rechaza_entradas_invalidas(self):
        with self.assertRaises(ValueError):
            calcular_rectangulos(funcion_ejemplo, PARTICION_EJEMPLO, "centro")
        with self.assertRaises(ValueError):
            calcular_rectangulos(funcion_ejemplo, (1, 1), "izquierda")

if __name__ == "__main__":
    unittest.main()
