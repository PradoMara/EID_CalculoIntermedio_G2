"""Secuencia continua del guion, sin audio: 65 + 55 + 55 + 60 + 50 s."""
import math

from manim import Scene, Text, VGroup, FadeIn, DOWN, UP, config
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


class PresentacionGuion(Scene):
    """Reutiliza las escenas reales y ajusta su ritmo al tiempo de locución."""
    factor_tiempo = 1.0

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
        self.tarjeta('Grupo 2 · Cálculo Intermedio', [
            'Extremos izquierdos y extremos derechos',
            '¿Por qué dos sumas sobre la misma partición',
            'pueden entregar valores distintos?',
            'Daniel Prado · Sebastian Pereda · Rodrigo Pedraza',
        ], 15)
        self.tarjeta('La partición fija las bases', [
            'Función continua f en un intervalo [a, b]',
            'P = {x₀, x₁, …, xₙ}',
            'Subintervalo: [xᵢ₋₁, xᵢ]',
            'Ancho: Δxᵢ = xᵢ − xᵢ₋₁',
        ], 25)
        self.tarjeta('La muestra determina la altura', [
            'Elegimos x* dentro de cada subintervalo',
            'Altura: f(x*)     Aporte: f(x*) × Δxᵢ',
            'Izquierda: x* = xᵢ₋₁     Derecha: x* = xᵢ',
            'Misma partición y mismas bases; pueden cambiar las alturas',
        ], 25)

    def creditos(self):
        self.tarjeta('Grupo 2 · Cálculo Intermedio', [
            'Daniel Prado · Sebastian Pereda · Rodrigo Pedraza',
            'Animación: Manim Community 0.22.0',
        ], 8)
        self.tarjeta('Fuentes y recursos', [
            'Introducción a la integral · Apunte del curso',
            'Stewart · Cálculo, 8.ª ed. · Secciones 5.1–5.2',
            'MIT OpenCourseWare · 18.013A · Capítulo 20',
            'Referencias completas y uso de IA: repositorio del proyecto',
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

    def construct(self):
        self.ejecutar_bloque(self.introduccion, 65)
        self.ejecutar_bloque(lambda: ConstruccionIzquierda.construct(self), 55)
        self.ejecutar_bloque(lambda: ConstruccionDerecha.construct(self), 55)
        self.ejecutar_bloque(lambda: DetalleIntervalo.construct(self), 30, 30 / 7)
        self.ejecutar_bloque(lambda: ComparacionSumas.construct(self), 20, 20 / 7)
        self.ejecutar_bloque(lambda: self.tarjeta('¿Por qué cambian las sumas?', [
            'Partición uniforme: Rₙ − Lₙ = Δx · [f(b) − f(a)]',
            'En este ejemplo: 0.5 × (5 − 1) = 2',
            'La partición fija las bases.',
            'La regla de selección determina las alturas.',
        ], 10), 10)
        self.ejecutar_bloque(lambda: CierreIntegral.construct(self), 35, 35 / 10.95)
        self.ejecutar_bloque(self.creditos, 15)
