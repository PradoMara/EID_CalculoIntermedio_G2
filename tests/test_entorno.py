"""Pruebas de entorno: comprueban que las dependencias están instaladas.

No validan la matemática del producto; esas pruebas viven en
tests/test_matematica.py, tests/test_datos_rectangulos.py y
tests/test_comparacion.py (tareas posteriores).
"""
import importlib
import unittest

import manim


class TestEntorno(unittest.TestCase):
    def test_version_manim_fijada(self):
        self.assertEqual(manim.__version__, "0.22.0")

    def test_escena_de_prueba_importable(self):
        modulo = importlib.import_module("src.escenas.prueba_render")
        self.assertTrue(issubclass(modulo.PruebaRender, manim.Scene))


if __name__ == "__main__":
    unittest.main()
