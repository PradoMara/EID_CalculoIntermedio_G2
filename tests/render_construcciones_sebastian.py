"""Revisión aislada: python -m tests.render_construcciones_sebastian.

Usa el doble de pruebas existente, NO acredita integración con Daniel.
Los videos se identifican como revisión aislada en pantalla y en su ruta.
"""
from unittest.mock import patch
from manim import Scene, Text, DOWN, tempconfig
from tests.test_datos_rectangulos import modulo_matematica_mock
from src.matematica import funcion_ejemplo, PARTICION_EJEMPLO
from src.datos_rectangulos import preparar_datos_rectangulos
from src.escenas.construcciones import animar_construccion


class RevisionIzquierda(Scene):
    criterio = 'izquierda'

    def construct(self):
        with patch.dict('sys.modules', {'src.matematica': modulo_matematica_mock()}):
            datos = preparar_datos_rectangulos(funcion_ejemplo, PARTICION_EJEMPLO, self.criterio)
        self.add(Text('REVISIÓN AISLADA · datos de prueba · sin integración',
                      font_size=16).to_edge(DOWN, buff=0.12))
        animar_construccion(self, datos, self.criterio)


class RevisionDerecha(RevisionIzquierda):
    criterio = 'derecha'


if __name__ == '__main__':
    with tempconfig({'quality': 'low_quality', 'media_dir': 'media/revision_sebastian',
                     'disable_caching': True}):
        RevisionIzquierda().render()
        RevisionDerecha().render()
