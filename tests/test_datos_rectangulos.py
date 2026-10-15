"""Pruebas unitarias para preparar_datos_rectangulos (Tarea T-012 / T-027).

Autor: Sebastian Pereda (Sublíder)
Verifica que las bases sean idénticas entre izquierda y derecha, que las alturas
provengan de evaluar f en la muestra correcta, que no se traslade la base,
y que se mantengan los 6 campos matemáticos + vértices continuos.
"""

import sys
import types
import unittest
from unittest.mock import patch

from src.datos_rectangulos import preparar_datos_rectangulos


def modulo_matematica_mock():
    """Mock con el contrato acordado de src.matematica."""
    modulo = types.ModuleType("src.matematica")

    def funcion_ejemplo(x):
        return x**2 + 1

    def calcular_rectangulos(funcion, particion, criterio):
        registros = []
        for izq, der in zip(particion[:-1], particion[1:]):
            muestra = izq if criterio == "izquierda" else der
            ancho = der - izq
            altura = funcion(muestra)
            registros.append({
                "izquierda": izq,
                "derecha": der,
                "muestra": muestra,
                "ancho": ancho,
                "altura": altura,
                "aporte": altura * ancho,
            })
        return registros

    modulo.funcion_ejemplo = funcion_ejemplo
    modulo.calcular_rectangulos = calcular_rectangulos
    return modulo


class TestDatosRectangulos(unittest.TestCase):
    def setUp(self):
        self.mock_mat = modulo_matematica_mock()
        self.patcher = patch.dict(sys.modules, {"src.matematica": self.mock_mat})
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

        self.f = self.mock_mat.funcion_ejemplo
        self.particion = [0, 0.5, 1, 1.5, 2]

    def test_cantidad_y_bases_compartidas(self):
        """Izquierda y derecha deben tener 4 rectángulos y compartir exactamente las mismas bases."""
        izq = preparar_datos_rectangulos(self.f, self.particion, "izquierda")
        der = preparar_datos_rectangulos(self.f, self.particion, "derecha")

        self.assertEqual(len(izq), 4)
        self.assertEqual(len(der), 4)

        for r_izq, r_der in zip(izq, der):
            self.assertEqual(r_izq["izquierda"], r_der["izquierda"])
            self.assertEqual(r_izq["derecha"], r_der["derecha"])
            self.assertEqual(r_izq["ancho"], r_der["ancho"])
            self.assertAlmostEqual(r_izq["ancho"], 0.5)

    def test_muestras_y_alturas_ejemplo_oficial(self):
        """Verifica las 4 alturas y aportes teóricos de cada criterio."""
        izq = preparar_datos_rectangulos(self.f, self.particion, "izquierda")
        der = preparar_datos_rectangulos(self.f, self.particion, "derecha")

        alturas_izq_esperadas = [1.0, 1.25, 2.0, 3.25]
        aportes_izq_esperados = [0.5, 0.625, 1.0, 1.625]

        alturas_der_esperadas = [1.25, 2.0, 3.25, 5.0]
        aportes_der_esperados = [0.625, 1.0, 1.625, 2.5]

        for i in range(4):
            self.assertAlmostEqual(izq[i]["altura"], alturas_izq_esperadas[i])
            self.assertAlmostEqual(izq[i]["aporte"], aportes_izq_esperados[i])
            self.assertAlmostEqual(der[i]["altura"], alturas_der_esperadas[i])
            self.assertAlmostEqual(der[i]["aporte"], aportes_der_esperados[i])

    def test_subintervalo_critico_1_a_1_5(self):
        """En [1, 1.5], la base se mantiene en 0.5; solo cambia la altura (2 vs 3.25)."""
        izq = preparar_datos_rectangulos(self.f, self.particion, "izquierda")
        der = preparar_datos_rectangulos(self.f, self.particion, "derecha")

        sub_izq = izq[2]
        sub_der = der[2]

        self.assertEqual((sub_izq["izquierda"], sub_izq["derecha"]), (1.0, 1.5))
        self.assertEqual((sub_der["izquierda"], sub_der["derecha"]), (1.0, 1.5))

        self.assertEqual(sub_izq["muestra"], 1.0)
        self.assertEqual(sub_izq["altura"], 2.0)
        self.assertEqual(sub_izq["aporte"], 1.0)

        self.assertEqual(sub_der["muestra"], 1.5)
        self.assertEqual(sub_der["altura"], 3.25)
        self.assertEqual(sub_der["aporte"], 1.625)

    def test_vertices_geometricos_no_trasladan_base(self):
        """Los 4 vértices deben recorrer un rectángulo cerrado sobre [izq, der] con altura en y."""
        izq = preparar_datos_rectangulos(self.f, self.particion, "izquierda")
        sub = izq[0]  # [0, 0.5] con altura 1.0
        esperados = [(0.0, 0.0), (0.5, 0.0), (0.5, 1.0), (0.0, 1.0)]
        self.assertEqual(sub["vertices_matematicos"], esperados)


if __name__ == "__main__":
    unittest.main()
