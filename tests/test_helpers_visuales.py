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



@unittest.skipUnless(TIENE_MANIM, 'Requiere Manim')
class TestGeometriaVisual(unittest.TestCase):
    def setUp(self):
        import numpy as np
        from src.escenas import construcciones as c
        self.np, self.c = np, c
        self.ejes = c.crear_ejes()

    def test_ejes_escala_y_rotulos(self):
        e = self.ejes
        self.assertAlmostEqual(self.np.linalg.norm(e.c2p(1, 0)-e.c2p(0, 0)), 4.5)
        self.assertAlmostEqual(self.np.linalg.norm(e.c2p(0, 1)-e.c2p(0, 0)), 1.1)
        textos = [m.text for m in e.get_family() if isinstance(m, manim.Text)]
        for texto in ['x', 'y', '1', '2', '3', '4', '5']:
            self.assertIn(texto, textos)

    def test_grafica_funcion_recibida_y_extremos(self):
        for funcion in [lambda x: x*x+1, lambda x: 2*x]:
            curva = self.c.crear_grafica(self.ejes, funcion)[0]
            self.np.testing.assert_allclose(self.ejes.p2c(curva.get_start()), [0, funcion(0)], atol=1e-7)
            self.np.testing.assert_allclose(self.ejes.p2c(curva.get_end()), [2, funcion(2)], atol=1e-7)

    def test_particion_irregular_marcas_y_posicion(self):
        grupo = self.c.crear_marcas_particion(self.ejes, [0, 0.3, 1.2, 2])
        textos = [m for m in grupo.get_family() if isinstance(m, manim.Text)]
        self.assertEqual([t.text for t in textos], ['0', '0.3', '1.2', '2'])
        for txt, x in zip(textos, [0, 0.3, 1.2, 2]):
            self.assertAlmostEqual(txt.get_center()[0], self.ejes.c2p(x, 0)[0])
        lineas = [m for m in grupo.get_family() if isinstance(m, manim.Line)]
        for x in [0.3, 1.2]:
            self.assertTrue(any(self.np.allclose(m.get_center(), self.ejes.c2p(x, 0)) for m in lineas))

    def test_no_duplica_etiquetas_ni_marcas_existentes(self):
        class Numero(manim.Text):
            def get_value(self):
                return float(self.text)
        self.ejes.x_axis.numbers = manim.VGroup(Numero('0.5'))
        grupo = self.c.crear_marcas_particion(self.ejes, [0.5, 0.5])
        self.assertEqual(len(grupo), 0)

    def test_vertices_y_marcadores_con_ejes_transformados(self):
        e = self.ejes.scale(0.72).shift(manim.LEFT * 2)
        for muestra, altura in [(1, 2), (1.5, 3.25)]:
            dato = dict(izquierda=1, derecha=1.5, muestra=muestra, altura=altura)
            for con_vertices in [False, True]:
                vertices = [(1, 0), (1.5, 0), (1.5, altura), (1, altura)]
                if con_vertices:
                    dato['vertices_matematicos'] = vertices
                rect = self.c.crear_rectangulo(e, dato, self.c.COLOR_IZQUIERDA)
                self.np.testing.assert_allclose([e.p2c(p) for p in rect.get_vertices()], vertices, atol=1e-7)
                self.assertAlmostEqual(rect.get_fill_opacity(), 0.35)
            guia, base, cima = self.c.crear_marcadores_muestra(e, dato)
            for punto, esperado in [(base.get_center(), [muestra, 0]),
                                    (cima.get_center(), [muestra, altura]),
                                    (guia.get_start(), [muestra, 0]),
                                    (guia.get_end(), [muestra, altura])]:
                self.np.testing.assert_allclose(e.p2c(punto), esperado, atol=1e-7)

    def test_escenas_consumen_modelo_sin_respaldo_silencioso(self):
        from unittest.mock import patch
        for clase, criterio in [(self.c.ConstruccionIzquierda, 'izquierda'),
                                (self.c.ConstruccionDerecha, 'derecha')]:
            with patch.object(self.c, 'datos_construccion', return_value=['registro']) as cargar, \
                 patch.object(self.c, 'animar_construccion') as animar:
                escena = clase()
                escena.construct()
                cargar.assert_called_once_with(criterio)
                animar.assert_called_once_with(escena, ['registro'], criterio)
            with patch.object(self.c, 'datos_construccion', side_effect=ImportError('modelo pendiente')):
                with self.assertRaises(ImportError):
                    clase().construct()


if __name__ == "__main__":
    unittest.main()
