"""Pruebas de Rodrigo. El doble reemplaza temporalmente el módulo de Daniel.

Así se puede probar esta pieza mientras ``src.matematica`` está en desarrollo.
Al existir ese módulo, la prueba de integración adicional se activa sola.
"""

import importlib.util
import sys
import types
import unittest
from unittest.mock import patch

from src.comparacion import (
    calcular_refinamientos,
    comparar_sumas,
    extraer_detalle_intervalo,
)


def modulo_matematico_de_prueba():
    """Interfaz mínima acordada; no forma parte del producto."""
    modulo = types.ModuleType("src.matematica")

    def crear_particion_uniforme(a, b, n):
        if not a < b:
            raise ValueError("Intervalo inválido")
        return [a + (b - a) * i / n for i in range(n + 1)]

    def calcular_rectangulos(funcion, particion, criterio):
        registros = []
        for izquierda, derecha in zip(particion[:-1], particion[1:]):
            muestra = izquierda if criterio == "izquierda" else derecha
            ancho = derecha - izquierda
            altura = funcion(muestra)
            registros.append({
                "izquierda": izquierda,
                "derecha": derecha,
                "muestra": muestra,
                "ancho": ancho,
                "altura": altura,
                "aporte": altura * ancho,
            })
        return registros

    def suma_riemann(funcion, particion, criterio):
        return sum(r["aporte"] for r in calcular_rectangulos(funcion, particion, criterio))

    modulo.crear_particion_uniforme = crear_particion_uniforme
    modulo.calcular_rectangulos = calcular_rectangulos
    modulo.suma_riemann = suma_riemann
    return modulo


class TestComparacion(unittest.TestCase):
    def setUp(self):
        self.sustitucion = patch.dict(sys.modules, {"src.matematica": modulo_matematico_de_prueba()})
        self.sustitucion.start()
        self.addCleanup(self.sustitucion.stop)
        self.funcion = lambda x: x * x + 1
        self.particion = [0, 0.5, 1, 1.5, 2]

    def test_totales_y_aportes_del_ejemplo(self):
        resultado = comparar_sumas(self.funcion, self.particion)
        self.assertEqual(resultado["total_izquierda"], 3.75)
        self.assertEqual(resultado["total_derecha"], 5.75)
        self.assertEqual(resultado["diferencia_total"], 2)
        self.assertEqual(resultado["diferencias_aportes"], [0.125, 0.375, 0.625, 0.875])
        self.assertAlmostEqual(sum(resultado["diferencias_aportes"]), resultado["diferencia_total"])

    def test_detalle_tercer_intervalo_sin_mutar_entrada(self):
        resultado = comparar_sumas(self.funcion, self.particion)
        detalle = extraer_detalle_intervalo(resultado, 2)
        self.assertEqual((detalle["izquierda"]["izquierda"], detalle["izquierda"]["derecha"]), (1, 1.5))
        self.assertEqual(detalle["izquierda"]["ancho"], 0.5)
        self.assertEqual(detalle["derecha"]["ancho"], 0.5)
        self.assertEqual((detalle["izquierda"]["altura"], detalle["derecha"]["altura"]), (2, 3.25))
        self.assertEqual((detalle["izquierda"]["aporte"], detalle["derecha"]["aporte"]), (1, 1.625))
        self.assertEqual(detalle["diferencia_aporte"], 0.625)
        detalle["izquierda"]["altura"] = -99
        self.assertEqual(resultado["rectangulos_izquierda"][2]["altura"], 2)

    def test_indices_invalidos(self):
        resultado = comparar_sumas(self.funcion, self.particion)
        for indice in (-1, 4, 2.0, True):
            with self.subTest(indice=indice), self.assertRaises(IndexError):
                extraer_detalle_intervalo(resultado, indice)

    def test_refinamiento(self):
        filas = calcular_refinamientos(self.funcion, 0, 2, [4, 8, 16])
        esperados = [
            (4, 0.5, 3.75, 5.75, 2),
            (8, 0.25, 4.1875, 5.1875, 1),
            (16, 0.125, 4.421875, 4.921875, 0.5),
        ]
        self.assertEqual([
            (f["n"], f["ancho"], f["total_izquierda"], f["total_derecha"], f["diferencia_total"])
            for f in filas
        ], esperados)

    def test_cantidades_invalidas(self):
        for cantidad in (0, -2, 2.5, True, "8"):
            with self.subTest(cantidad=cantidad), self.assertRaises(ValueError):
                calcular_refinamientos(self.funcion, 0, 2, [cantidad])

    def test_constante_y_decreciente(self):
        self.assertEqual(comparar_sumas(lambda x: 3, self.particion)["diferencia_total"], 0)
        self.assertEqual(comparar_sumas(lambda x: 5 - x, self.particion)["diferencia_total"], -1)

    def test_bases_desalineadas_se_rechazan(self):
        modulo = sys.modules["src.matematica"]
        original = modulo.calcular_rectangulos

        def desalineados(funcion, particion, criterio):
            registros = original(funcion, particion, criterio)
            if criterio == "derecha":
                registros[0]["derecha"] = 0.75
            return registros

        with patch.object(modulo, "calcular_rectangulos", desalineados):
            with self.assertRaisesRegex(ValueError, "base"):
                comparar_sumas(self.funcion, self.particion)

    def test_cantidades_desalineadas_se_rechazan(self):
        modulo = sys.modules["src.matematica"]
        original = modulo.calcular_rectangulos

        def incompletos(funcion, particion, criterio):
            registros = original(funcion, particion, criterio)
            return registros[:-1] if criterio == "derecha" else registros

        with patch.object(modulo, "calcular_rectangulos", incompletos):
            with self.assertRaisesRegex(ValueError, "cantidad"):
                comparar_sumas(self.funcion, self.particion)


@unittest.skipUnless(importlib.util.find_spec("src.matematica"), "Daniel aún no agregó src.matematica")
class TestIntegracionModeloReal(unittest.TestCase):
    def test_ejemplo_con_modelo_real(self):
        from src.matematica import funcion_ejemplo

        resultado = comparar_sumas(funcion_ejemplo, [0, 0.5, 1, 1.5, 2])
        self.assertEqual((resultado["total_izquierda"], resultado["total_derecha"]), (3.75, 5.75))


if __name__ == "__main__":
    unittest.main()
