"""Tres escenas de Rodrigo para la comparación y el cierre.

Se ejecutan cuando estén disponibles los módulos de Daniel y Sebastian.
Texto simple de Manim: no requiere instalación de LaTeX.
"""

from manim import (
    BLUE, ORANGE, WHITE, Create, FadeIn, FadeOut, ReplacementTransform,
    Scene, Text, Transform, VGroup, DOWN, LEFT, RIGHT, UP,
)

from src.comparacion import comparar_sumas, extraer_detalle_intervalo, calcular_refinamientos


def _grupo(objetos):
    """Admite tanto un objeto Manim como varios objetos devueltos juntos."""
    if isinstance(objetos, (tuple, list)):
        return VGroup(*objetos)
    return objetos


def _datos_y_ayudas():
    """Carga las piezas compartidas cuando se construye una escena."""
    from src.matematica import crear_particion_uniforme, funcion_ejemplo
    from src.datos_rectangulos import preparar_datos_rectangulos
    from src.escenas.construcciones import (
        crear_ejes, crear_grafica, crear_marcas_particion,
        crear_rectangulo, crear_marcadores_muestra,
    )
    return (crear_particion_uniforme, funcion_ejemplo,
            preparar_datos_rectangulos, crear_ejes, crear_grafica,
            crear_marcas_particion, crear_rectangulo, crear_marcadores_muestra)


def _escenario(ejes, funcion, particion, crear_grafica, crear_marcas_particion):
    """Muestra una sola escala y las mismas marcas para los dos criterios."""
    curva = _grupo(crear_grafica(ejes, funcion))
    marcas = _grupo(crear_marcas_particion(ejes, particion))
    return VGroup(ejes, curva, marcas)


def _rectangulos(ejes, datos, color, crear_rectangulo):
    return VGroup(*(crear_rectangulo(ejes, dato, color) for dato in datos))


class DetalleIntervalo(Scene):
    """La base [1, 1.5] permanece fija; cambia la altura."""

    def construct(self):
        (crear_particion_uniforme, funcion, preparar_datos, crear_ejes,
         crear_grafica, crear_marcas, crear_rectangulo, crear_marcadores) = _datos_y_ayudas()
        particion = crear_particion_uniforme(0, 2, 4)
        detalle = extraer_detalle_intervalo(comparar_sumas(funcion, particion), 2)
        datos_izq = preparar_datos(funcion, particion, "izquierda")
        datos_der = preparar_datos(funcion, particion, "derecha")

        titulo = Text("Misma base [1, 1.5]", font_size=34).to_edge(UP)
        ejes = crear_ejes()
        escenario = _escenario(ejes, funcion, particion, crear_grafica, crear_marcas)
        escenario.scale(0.72).to_edge(LEFT, buff=0.4).shift(DOWN * 0.45)
        rect_izq = crear_rectangulo(ejes, datos_izq[2], BLUE)
        rect_der = crear_rectangulo(ejes, datos_der[2], ORANGE)
        marca_izq = _grupo(crear_marcadores(ejes, datos_izq[2]))
        marca_der = _grupo(crear_marcadores(ejes, datos_der[2]))

        explicacion_izq = VGroup(
            Text("Muestra: 1", font_size=27),
            Text("Ancho: 0.5", font_size=27),
            Text("Altura: 2", font_size=27),
            Text("Aporte: 1", font_size=27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(RIGHT, buff=0.5)
        explicacion_der = VGroup(
            Text("Muestra: 1.5", font_size=27),
            Text("Ancho: 0.5", font_size=27),
            Text("Altura: 3.25", font_size=27),
            Text("Aporte: 1.625", font_size=27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(explicacion_izq)
        diferencia = Text(
            f"Aumento del aporte: {detalle['diferencia_aporte']:g}",
            font_size=26, color=ORANGE,
        ).to_edge(DOWN)

        self.play(FadeIn(titulo), Create(escenario))
        self.play(FadeIn(rect_izq), FadeIn(marca_izq), FadeIn(explicacion_izq))
        self.wait(1)
        self.play(ReplacementTransform(rect_izq, rect_der),
                  ReplacementTransform(marca_izq, marca_der),
                  Transform(explicacion_izq, explicacion_der))
        self.play(FadeIn(diferencia))
        self.wait(2)


class ComparacionSumas(Scene):
    """Compara L y R con una única función y una única partición."""

    def construct(self):
        (crear_particion_uniforme, funcion, preparar_datos, crear_ejes,
         crear_grafica, crear_marcas, crear_rectangulo, crear_marcadores) = _datos_y_ayudas()
        particion = crear_particion_uniforme(0, 2, 4)
        resultado = comparar_sumas(funcion, particion)
        datos_izq = preparar_datos(funcion, particion, "izquierda")
        datos_der = preparar_datos(funcion, particion, "derecha")

        titulo = Text("Misma funcion, intervalo y bases", font_size=32).to_edge(UP)
        ejes = crear_ejes()
        escenario = _escenario(ejes, funcion, particion, crear_grafica, crear_marcas)
        escenario.scale(0.72).to_edge(LEFT, buff=0.4).shift(DOWN * 0.45)
        izquierdos = _rectangulos(ejes, datos_izq, BLUE, crear_rectangulo)
        derechos = _rectangulos(ejes, datos_der, ORANGE, crear_rectangulo)
        texto_izq = Text(
            f"Izquierda = {resultado['total_izquierda']:g}", font_size=27, color=BLUE
        ).to_edge(RIGHT, buff=0.45)
        texto_der = Text(
            f"Derecha = {resultado['total_derecha']:g}", font_size=27, color=ORANGE
        ).move_to(texto_izq)
        diferencia = Text(
            f"Derecha - izquierda = {resultado['diferencia_total']:g}",
            font_size=25, color=WHITE,
        ).to_edge(DOWN)
        causa = Text("Aqui f(x) crece:\nsuben las alturas", font_size=25)
        causa.next_to(texto_der, DOWN, buff=0.35)
        causa.to_edge(RIGHT, buff=0.5)

        self.play(FadeIn(titulo), Create(escenario))
        self.play(FadeIn(izquierdos), FadeIn(texto_izq))
        self.wait(1)
        self.play(ReplacementTransform(izquierdos, derechos),
                  ReplacementTransform(texto_izq, texto_der))
        self.play(FadeIn(causa), FadeIn(diferencia))
        self.wait(2)


class CierreIntegral(Scene):
    """Al refinar cambia la partición; ambas sumas se acercan a 14/3."""

    def construct(self):
        (crear_particion_uniforme, funcion, preparar_datos, crear_ejes,
         crear_grafica, crear_marcas, crear_rectangulo, crear_marcadores) = _datos_y_ayudas()
        filas = calcular_refinamientos(funcion, 0, 2, [4, 8, 16])
        titulo = Text("Refinamos la particion", font_size=33).to_edge(UP)
        ejes = crear_ejes()
        # Las bases de los rectángulos indican la partición de cada fila.
        # No dejamos marcas fijas de n=4 cuando pasamos a n=8 y n=16.
        escenario = VGroup(ejes, _grupo(crear_grafica(ejes, funcion)))
        escenario.scale(0.68).to_edge(LEFT, buff=0.4).shift(DOWN * 0.35)

        self.play(FadeIn(titulo), Create(escenario))
        rectangulos_anteriores = None
        texto_anterior = None
        for fila in filas:
            particion = crear_particion_uniforme(0, 2, fila["n"])
            datos = preparar_datos(funcion, particion, "izquierda")
            rectangulos = _rectangulos(ejes, datos, BLUE, crear_rectangulo)
            texto = VGroup(
                Text(f"n = {fila['n']}, ancho = {fila['ancho']:g}", font_size=25),
                Text(f"L = {fila['total_izquierda']:g}", font_size=25, color=BLUE),
                Text(f"R = {fila['total_derecha']:g}", font_size=25, color=ORANGE),
                Text(f"Diferencia = {fila['diferencia_total']:g}", font_size=25),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.45)
            if rectangulos_anteriores is None:
                self.play(FadeIn(rectangulos), FadeIn(texto))
            else:
                self.play(FadeOut(rectangulos_anteriores), FadeOut(texto_anterior))
                self.play(FadeIn(rectangulos), FadeIn(texto))
            self.wait(0.65)
            rectangulos_anteriores = rectangulos
            texto_anterior = texto

        conclusion = VGroup(
            Text("Cambia la muestra, altura y aporte", font_size=27),
            Text("Misma particion: pueden cambiar las sumas", font_size=26),
            Text("Al refinar: ambas se acercan a 14/3", font_size=26),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN)
        self.play(FadeOut(rectangulos_anteriores), FadeOut(texto_anterior),
                  FadeOut(escenario), FadeOut(titulo), FadeIn(conclusion))
        self.wait(2)
