"""Escena mínima de verificación del entorno (sin MathTex, no requiere LaTeX)."""
from manim import Scene, Square, Create, BLUE


class PruebaRender(Scene):
    """Dibuja un cuadrado; sirve solo para comprobar que Manim renderiza."""

    def construct(self):
        cuadrado = Square(color=BLUE)
        self.play(Create(cuadrado))
        self.wait(0.5)
