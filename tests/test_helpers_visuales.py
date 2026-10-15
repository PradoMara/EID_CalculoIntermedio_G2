"""Pruebas unitarias para helpers visuales de Manim (Tarea T-012 / T-028 a T-032).

Autor: Sebastian Pereda (Sublíder)
Comprueba configuración, rangos, lógica geométrica y creación de objetos
sin fallar si manim no está instalado en el entorno de pruebas ligeras.
"""

import sys
import unittest

try:
    import manim
    TIENE_MANIM = True
except ImportError:
    TIENE_MANIM = False


class TestHelpersVisuales(unittest.TestCase):
    def test_constantes_y_configuracion_escala(self):
        """Verifica que las constantes geométricas fijen la escala acordada."""
        from src.escenas.construcciones import (
            X_RANGE, Y_RANGE, X_LENGTH, Y_LENGTH,
            COLOR_IZQUIERDA, COLOR_DERECHA,
        )
        self.assertEqual(X_RANGE, [0, 2, 0.5])
        self.assertEqual(Y_RANGE, [0, 5, 1])
        self.assertEqual(X_LENGTH, 9.0)
        self.assertEqual(Y_LENGTH, 5.5)

        # Escala: 9/2 = 4.5 en X; 5.5/5 = 1.1 en Y
        self.assertEqual(COLOR_IZQUIERDA, "#56B4E9")
        self.assertEqual(COLOR_DERECHA, "#E69F00")

    @unittest.skipUnless(TIENE_MANIM, "Requiere Manim instalado en el entorno")
    def test_creacion_objetos_manim(self):
        from src.escenas.construcciones import (
            crear_ejes, crear_grafica, crear_marcas_particion,
            crear_rectangulo, crear_marcadores_muestra,
        )
        ejes = crear_ejes()
        f = lambda x: x**2 + 1
        particion = [0, 0.5, 1, 1.5, 2]

        grafica = crear_grafica(ejes, f)
        self.assertIsNotNone(grafica)

        marcas = crear_marcas_particion(ejes, particion)
        self.assertEqual(len(marcas), 5)

        dato = {
            "izquierda": 1.0,
            "derecha": 1.5,
            "muestra": 1.0,
            "altura": 2.0,
            "vertices_matematicos": [(1.0, 0.0), (1.5, 0.0), (1.5, 2.0), (1.0, 2.0)],
        }
        rect = crear_rectangulo(ejes, dato, "#56B4E9")
        self.assertIsNotNone(rect)

        marcadores = crear_marcadores_muestra(ejes, dato, "#56B4E9")
        self.assertEqual(len(marcadores), 3)


if __name__ == "__main__":
    unittest.main()
