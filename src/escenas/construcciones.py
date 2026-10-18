"""Helpers visuales y escenas de construcción para el EID (Grupo 2).

Autor: Sebastian Pereda (Sublíder)
Tareas:
- T-028: crear_ejes
- T-029: crear_grafica
- T-030: crear_marcas_particion
- T-031: crear_rectangulo
- T-032: crear_marcadores_muestra
- T-011: ConstruccionIzquierda (Scene)
- T-033: ConstruccionDerecha (Scene)

Usa la paleta Okabe-Ito accesible y escala uniforme compartida.
"""

# Constantes de configuración de escala compartida
X_RANGE = [0, 2, 0.5]
Y_RANGE = [0, 5, 1]
X_LENGTH = 9.0
Y_LENGTH = 5.5

# Paleta Okabe-Ito accesible y capas (z-index)
COLOR_IZQUIERDA = "#56B4E9"  # Azul cielo (Okabe-Ito)
COLOR_DERECHA = "#E69F00"    # Naranja (Okabe-Ito)
COLOR_CURVA = "#FFFFFF"
COLOR_EJES = "#BBBBBB"

OPACIDAD_RECTANGULO = 0.35
GROSOR_RECTANGULO = 2.0
GROSOR_CURVA = 4.0

Z_RECT = 1
Z_EJES = 2
Z_CURVA = 3
Z_LINEA_ALTURA = 4
Z_PUNTOS = 5
Z_ETIQUETAS = 6


def crear_ejes():
    """T-028: Devuelve ejes Manim con rangos x in [0, 2] e y in [0, 5].

    Define la escala base compartida antes de transformar la composición:
    ux = 9 / 2 = 4.5 unidades de escena por unidad x
    uy = 5.5 / 5 = 1.1 unidades de escena por unidad y
    """
    from manim import Axes, Text, VGroup, LEFT, RIGHT, UP

    ejes = Axes(
        x_range=X_RANGE,
        y_range=Y_RANGE,
        x_length=X_LENGTH,
        y_length=Y_LENGTH,
        tips=False,
        axis_config={
            "color": COLOR_EJES,
            "stroke_width": 2,
        },
    )
    rotulos = VGroup(
        Text("x", font_size=22).next_to(ejes.c2p(2, 0), RIGHT, buff=0.15),
        Text("y", font_size=22).next_to(ejes.c2p(0, 5), UP, buff=0.15),
    )
    for valor in range(1, 6):
        rotulos.add(Text(str(valor), font_size=20, color=COLOR_EJES)
                    .next_to(ejes.c2p(0, valor), LEFT, buff=0.15))
    ejes.add(rotulos)
    ejes.set_z_index(Z_EJES)
    return ejes


def crear_grafica(ejes, funcion):
    """T-029: Devuelve la curva de la función y su etiqueta sobre [0, 2]."""
    from manim import Text, VGroup, WHITE, LEFT

    curva = ejes.plot(
        funcion,
        x_range=[X_RANGE[0], X_RANGE[1]],
        color=COLOR_CURVA,
        stroke_width=GROSOR_CURVA,
    )
    curva.set_z_index(Z_CURVA)

    etiqueta = Text("f(x) = x² + 1", font_size=24, color=WHITE)
    pos_pantalla = ejes.c2p(1.5, 4.5)
    etiqueta.move_to(pos_pantalla).shift(LEFT * 0.5)
    etiqueta.set_z_index(Z_ETIQUETAS)

    return VGroup(curva, etiqueta)


def crear_marcas_particion(ejes, particion):
    """T-030: Devuelve marcas y etiquetas para cada límite de la partición."""
    from manim import Text, VGroup, DOWN, UP, Line
    import numpy as np

    grupo = VGroup()
    etiquetas_existentes = list(getattr(ejes.x_axis, "numbers", []))
    marcas_existentes = list(ejes.x_axis.ticks)
    for p in dict.fromkeys(particion):
        punto = ejes.c2p(p, 0)
        elementos = VGroup()
        if not any(np.allclose(m.get_center(), punto) for m in marcas_existentes):
            elementos.add(Line(punto + DOWN * 0.06, punto + UP * 0.06,
                               color=COLOR_EJES))
        if not any(np.isclose(t.get_value(), p) for t in etiquetas_existentes):
            elementos.add(Text(f"{p:g}", font_size=20, color=COLOR_EJES)
                           .next_to(punto, DOWN, buff=0.18))
        if len(elementos):
            grupo.add(elementos)
    return grupo.set_z_index(Z_ETIQUETAS)


def crear_rectangulo(ejes, dato, color):
    """T-031: Convierte vértices matemáticos de `dato` en un Polygon Manim."""
    from manim import Polygon

    if "vertices_matematicos" in dato:
        verts_mat = dato["vertices_matematicos"]
    else:
        izq, der, alt = dato["izquierda"], dato["derecha"], dato["altura"]
        verts_mat = [(izq, 0.0), (der, 0.0), (der, alt), (izq, alt)]

    verts_pantalla = [ejes.c2p(vx, vy) for vx, vy in verts_mat]
    rect = Polygon(
        *verts_pantalla,
        color=color,
        fill_opacity=OPACIDAD_RECTANGULO,
        stroke_width=GROSOR_RECTANGULO,
    )
    rect.set_z_index(Z_RECT)
    return rect


def crear_marcadores_muestra(ejes, dato, color=None):
    """T-032: Devuelve marcador en (muestra, 0), punto en (muestra, altura) y guía."""
    from manim import DashedLine, Dot, VGroup, WHITE

    muestra = dato["muestra"]
    altura = dato["altura"]
    col = color if color is not None else WHITE

    p_eje = ejes.c2p(muestra, 0.0)
    p_curva = ejes.c2p(muestra, altura)

    punto_eje = Dot(p_eje, radius=0.07, color=col)
    punto_curva = Dot(p_curva, radius=0.07, color=col)
    punto_eje.set_z_index(Z_PUNTOS)
    punto_curva.set_z_index(Z_PUNTOS)

    linea_guia = DashedLine(
        p_eje,
        p_curva,
        dash_length=0.08,
        dashed_ratio=0.5,
        stroke_width=2.5,
        color=col,
    )
    linea_guia.set_z_index(Z_LINEA_ALTURA)

    return VGroup(linea_guia, punto_eje, punto_curva)


def datos_construccion(criterio):
    """Carga exclusivamente el modelo real; nunca sustituye errores por cifras."""
    from src.matematica import funcion_ejemplo, PARTICION_EJEMPLO
    from src.datos_rectangulos import preparar_datos_rectangulos
    return preparar_datos_rectangulos(funcion_ejemplo, PARTICION_EJEMPLO, criterio)


def animar_construccion(escena, datos, criterio):
    """Presentación de 55 s; datos inyectables para revisión visual aislada."""
    from manim import Text, VGroup, FadeIn, UP, DOWN, LEFT
    from src.matematica import funcion_ejemplo, PARTICION_EJEMPLO

    color = COLOR_IZQUIERDA if criterio == "izquierda" else COLOR_DERECHA
    simbolo = "L₄" if criterio == "izquierda" else "R₄"
    titulo = Text(f"Suma {criterio}: mismas bases, nuevas alturas", font_size=30).to_edge(UP)
    ejes = crear_ejes()
    escenario = VGroup(ejes, crear_grafica(ejes, funcion_ejemplo),
                       crear_marcas_particion(ejes, PARTICION_EJEMPLO))
    escenario.scale(0.72).to_edge(LEFT, buff=0.4).shift(DOWN * 0.45)
    escena.add(titulo)
    escena.play(FadeIn(escenario), run_time=1)
    escena.wait(6)
    for i, dato in enumerate(datos):
        marcadores = crear_marcadores_muestra(ejes, dato, color)
        rect = crear_rectangulo(ejes, dato, color)
        y = 1.7 - i * 0.95
        muestra = Text(f"[{dato['izquierda']:g}, {dato['derecha']:g}]   muestra: {dato['muestra']:g}",
                       font_size=21).move_to([3.9, y, 0])
        altura = Text(f"altura: {dato['altura']:g}", font_size=21).move_to([3.9, y-0.28, 0])
        aporte = Text(f"aporte: {dato['ancho']:g} × {dato['altura']:g} = {dato['aporte']:g}",
                      font_size=21, color=color).move_to([3.9, y-0.56, 0])
        escena.play(FadeIn(marcadores[1]), FadeIn(muestra), run_time=1)
        escena.wait(2)
        escena.play(FadeIn(marcadores[0]), FadeIn(marcadores[2]), FadeIn(altura), run_time=1)
        escena.wait(2)
        escena.play(FadeIn(rect), FadeIn(aporte), run_time=1)
        escena.wait(3)
    total = sum(d['aporte'] for d in datos)
    texto_total = Text(f"{simbolo} = {total:g}", font_size=32, color=color).move_to([3.9, -2.8, 0])
    escena.play(FadeIn(texto_total), run_time=1)
    escena.wait(7)


try:
    from manim import Scene
except ImportError:
    ConstruccionIzquierda = None
    ConstruccionDerecha = None
else:
    class ConstruccionIzquierda(Scene):
        def construct(self):
            animar_construccion(self, datos_construccion("izquierda"), "izquierda")

    class ConstruccionDerecha(Scene):
        def construct(self):
            animar_construccion(self, datos_construccion("derecha"), "derecha")
