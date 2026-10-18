"""Secuencia continua del guion, sin audio: 65 + 55 + 55 + 60 + 50 s."""
import math

from manim import BLACK, Scene, Text, VGroup, FadeIn, DOWN, UP, config
from src.escenas.introduccion import IntroduccionRiemann
from src.escenas.construcciones import ConstruccionIzquierda, ConstruccionDerecha
from src.escenas.comparacion import DetalleIntervalo, ComparacionSumas, CierreIntegral


# Orden y presupuestos del guion; detalle y comparación comparten 60 segundos.
BLOQUES = (
    ('Introducción · Daniel', 65),
    ('Suma izquierda · Sebastian', 55),
    ('Suma derecha · Sebastian', 55),
    ('Detalle del intervalo · Rodrigo', 30),
    ('Comparación · Rodrigo', 30),
    ('Integral · Rodrigo', 35),
    ('Créditos', 15),
)


class PresentacionGuion(IntroduccionRiemann, Scene):
    """Reutiliza las escenas reales y ajusta su ritmo al tiempo de locución."""
    factor_tiempo = 1.0
    narrador = None

    def clear(self):
        """Conserva la identificación al cambiar tarjetas dentro de un bloque."""
        super().clear()
        self.camera.background_color = BLACK
        if self.narrador:
            rotulo = Text(f"Narrador: {self.narrador}", font_size=20)
            rotulo.to_edge(UP, buff=0.12).set_z_index(100)
            self.add(rotulo)
        return self

    def identificar(self, nombre):
        self.narrador = nombre
        self.clear()

    def _duracion(self, segundos):
        # Redondear hacia abajo permite completar cada bloque al cuadro exacto.
        fps = config.frame_rate
        return max(1 / fps, math.floor(segundos * self.factor_tiempo * fps + 1e-7) / fps)

    def play(self, *animations, **kwargs):
        duracion = kwargs.get('run_time', max((getattr(a, 'run_time', 1) for a in animations), default=1))
        kwargs['run_time'] = self._duracion(duracion)
        return super().play(*animations, **kwargs)

    def wait(self, duration=1, **kwargs):
        segundos = self._duracion(duration)
        factor = self.factor_tiempo
        self.factor_tiempo = 1
        try:
            return super().wait(segundos, **kwargs)
        finally:
            self.factor_tiempo = factor

    def tarjeta(self, titulo, lineas, segundos):
        encabezado = Text(titulo, font_size=34).to_edge(UP, buff=0.65)
        contenido = VGroup(*(Text(t, font_size=28) for t in lineas))
        contenido.arrange(DOWN, buff=0.4)
        if contenido.width > 12.5:
            contenido.scale_to_fit_width(12.5)
        self.play(FadeIn(encabezado), FadeIn(contenido), run_time=1)
        self.wait(segundos - 1)
        self.clear()

    def introduccion(self):
        self.identificar(None)
        IntroduccionRiemann.construct(self)

    def creditos(self):
        self.tarjeta('Grupo 2 · Cálculo Intermedio (MAT1188)', [
            'Daniel Prado · Sebastian Pereda · Rodrigo Pedraza',
            'Animación: Manim Community 0.22.0',
            'Paleta: Okabe–Ito',
        ], 8)
        self.tarjeta('Fuentes y recursos', [
            'Introducción a la integral · Apunte del curso',
            'Stewart · Cálculo, 8.ª ed. · Secciones 5.1–5.2',
            'Kleitman · MIT OCW 18.013A · Capítulo 20',
            'IA: Codex · apoyo en código y guion',
            'Verificación: cálculos, pruebas unitarias y renders',
            'Detalle de fuentes, apoyos y verificaciones: repositorio',
        ], 7)

    def ejecutar_bloque(self, construir, duracion, factor=1):
        inicio = self.renderer.time
        self.factor_tiempo = factor
        construir()
        self.factor_tiempo = 1
        restante = duracion - (self.renderer.time - inicio)
        if restante < -1 / config.frame_rate:
            raise ValueError('La escena excede el tiempo asignado en el guion')
        if restante > 0.5 / config.frame_rate:
            self.wait(restante)
        self.clear()

    def bloque_introduccion(self):
        self.ejecutar_bloque(self.introduccion, 65)

    def bloque_desarrollo(self):
        self.identificar('Sebastian Pereda')
        self.ejecutar_bloque(lambda: ConstruccionIzquierda.construct(self), 55)
        self.ejecutar_bloque(lambda: ConstruccionDerecha.construct(self), 55)

    def bloque_cierre(self):
        self.identificar('Rodrigo Pedraza')
        self.ejecutar_bloque(lambda: DetalleIntervalo.construct(self), 30, 30 / 7)
        self.ejecutar_bloque(lambda: ComparacionSumas.construct(self), 20, 20 / 7)
        self.ejecutar_bloque(lambda: self.tarjeta('¿Por qué cambian las sumas?', [
            'Partición uniforme: Rₙ − Lₙ = Δx · [f(b) − f(a)]',
            'En este ejemplo: 0.5 × (5 − 1) = 2',
            'La partición fija las bases.',
            'La regla de selección determina las alturas.',
        ], 10), 10)
        self.ejecutar_bloque(lambda: CierreIntegral.construct(self), 35, 35 / 10.95)
        self.identificar(None)
        self.ejecutar_bloque(self.creditos, 15)

    def construct(self):
        self.bloque_introduccion()
        self.bloque_desarrollo()
        self.bloque_cierre()


class DesarrolloGuion(PresentacionGuion):
    """Bloque de desarrollo (Sebastian Pereda): suma izquierda y suma derecha."""

    def construct(self):
        self.bloque_desarrollo()


class CierreGuion(PresentacionGuion):
    """Bloque de cierre (Rodrigo Pedraza): detalle, comparación, integral y créditos."""

    def construct(self):
        self.bloque_cierre()

