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

    Garantiza escala fija en todas las escenas del grupo:
    ux = 9 / 2 = 4.5 unidades de escena por unidad x
    uy = 5.5 / 5 = 1.1 unidades de escena por unidad y
    """
    from manim import Axes

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
    from manim import Text, VGroup, DOWN

    grupo = VGroup()
    for p in particion:
        punto_eje = ejes.c2p(p, 0)
        etiqueta_texto = f"{p:g}" if isinstance(p, (int, float)) else str(p)
        txt = Text(etiqueta_texto, font_size=20, color=COLOR_EJES)
        txt.next_to(punto_eje, DOWN, buff=0.18)
        txt.set_z_index(Z_ETIQUETAS)
        grupo.add(txt)
    return grupo


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


try:
    from manim import Scene

    class ConstruccionIzquierda(Scene):
        """T-011: Escena Manim que anima la construcción de la suma izquierda (L_4 = 3.75)."""

        def construct(self):
            import sys
            from pathlib import Path
            raiz = Path(__file__).resolve().parent.parent.parent
            if str(raiz) not in sys.path:
                sys.path.insert(0, str(raiz))

            from manim import FadeIn, LaggedStart, Text, VGroup, DOWN, RIGHT, UP
            from src.matematica import funcion_ejemplo

            try:
                from src.matematica import crear_particion_uniforme, suma_riemann
                particion = crear_particion_uniforme(0, 2, 4)
                total_L4 = suma_riemann(funcion_ejemplo, particion, "izquierda")
            except (ImportError, AttributeError):
                particion = [0, 0.5, 1, 1.5, 2]
                total_L4 = 3.75

            from src.datos_rectangulos import preparar_datos_rectangulos

            try:
                datos = preparar_datos_rectangulos(funcion_ejemplo, particion, "izquierda")
            except (ImportError, AttributeError):
                # Fallback visual mientras Daniel termina T-026 en src.matematica
                datos = [
                    {"izquierda": 0.0, "derecha": 0.5, "muestra": 0.0, "altura": 1.0,
                     "vertices_matematicos": [(0, 0), (0.5, 0), (0.5, 1), (0, 1)]},
                    {"izquierda": 0.5, "derecha": 1.0, "muestra": 0.5, "altura": 1.25,
                     "vertices_matematicos": [(0.5, 0), (1, 0), (1, 1.25), (0.5, 1.25)]},
                    {"izquierda": 1.0, "derecha": 1.5, "muestra": 1.0, "altura": 2.0,
                     "vertices_matematicos": [(1, 0), (1.5, 0), (1.5, 2), (1, 2)]},
                    {"izquierda": 1.5, "derecha": 2.0, "muestra": 1.5, "altura": 3.25,
                     "vertices_matematicos": [(1.5, 0), (2, 0), (2, 3.25), (1.5, 3.25)]},
                ]

            titulo = Text("Suma de Riemann: Extremos Izquierdos", font_size=32).to_edge(UP)
            ejes = crear_ejes()
            grafica = crear_grafica(ejes, funcion_ejemplo)
            marcas = crear_marcas_particion(ejes, particion)

            escenario = VGroup(ejes, grafica, marcas)
            escenario.scale(0.85).shift(DOWN * 0.3)

            self.add(titulo)
            self.play(FadeIn(escenario))

            rectangulos_animados = []
            for dato in datos:
                rect = crear_rectangulo(ejes, dato, COLOR_IZQUIERDA)
                marcadores = crear_marcadores_muestra(ejes, dato, COLOR_IZQUIERDA)
                sub_grupo = VGroup(rect, marcadores)
                rectangulos_animados.append(sub_grupo)

            self.play(
                LaggedStart(
                    *(FadeIn(r) for r in rectangulos_animados),
                    lag_ratio=0.4,
                    run_time=3.0,
                )
            )

            texto_total = Text(f"L₄ = {total_L4:.2f}", font_size=30, color=COLOR_IZQUIERDA)
            texto_total.to_corner(UP + RIGHT, buff=0.8)
            self.play(FadeIn(texto_total))
            self.wait(1.5)

    class ConstruccionDerecha(Scene):
        """T-033: Escena Manim que anima la construcción de la suma derecha (R_4 = 5.75)."""

        def construct(self):
            import sys
            from pathlib import Path
            raiz = Path(__file__).resolve().parent.parent.parent
            if str(raiz) not in sys.path:
                sys.path.insert(0, str(raiz))

            from manim import FadeIn, LaggedStart, Text, VGroup, DOWN, RIGHT, UP
            from src.matematica import funcion_ejemplo

            try:
                from src.matematica import crear_particion_uniforme, suma_riemann
                particion = crear_particion_uniforme(0, 2, 4)
                total_R4 = suma_riemann(funcion_ejemplo, particion, "derecha")
            except (ImportError, AttributeError):
                particion = [0, 0.5, 1, 1.5, 2]
                total_R4 = 5.75

            from src.datos_rectangulos import preparar_datos_rectangulos

            try:
                datos = preparar_datos_rectangulos(funcion_ejemplo, particion, "derecha")
            except (ImportError, AttributeError):
                # Fallback visual mientras Daniel termina T-026 en src.matematica
                datos = [
                    {"izquierda": 0.0, "derecha": 0.5, "muestra": 0.5, "altura": 1.25,
                     "vertices_matematicos": [(0, 0), (0.5, 0), (0.5, 1.25), (0, 1.25)]},
                    {"izquierda": 0.5, "derecha": 1.0, "muestra": 1.0, "altura": 2.0,
                     "vertices_matematicos": [(0.5, 0), (1, 0), (1, 2), (0.5, 2)]},
                    {"izquierda": 1.0, "derecha": 1.5, "muestra": 1.5, "altura": 3.25,
                     "vertices_matematicos": [(1, 0), (1.5, 0), (1.5, 3.25), (1, 3.25)]},
                    {"izquierda": 1.5, "derecha": 2.0, "muestra": 2.0, "altura": 5.0,
                     "vertices_matematicos": [(1.5, 0), (2, 0), (2, 5), (1.5, 5)]},
                ]

            titulo = Text("Suma de Riemann: Extremos Derechos", font_size=32).to_edge(UP)
            ejes = crear_ejes()
            grafica = crear_grafica(ejes, funcion_ejemplo)
            marcas = crear_marcas_particion(ejes, particion)

            escenario = VGroup(ejes, grafica, marcas)
            escenario.scale(0.85).shift(DOWN * 0.3)

            self.add(titulo)
            self.play(FadeIn(escenario))

            rectangulos_animados = []
            for dato in datos:
                rect = crear_rectangulo(ejes, dato, COLOR_DERECHA)
                marcadores = crear_marcadores_muestra(ejes, dato, COLOR_DERECHA)
                sub_grupo = VGroup(rect, marcadores)
                rectangulos_animados.append(sub_grupo)

            self.play(
                LaggedStart(
                    *(FadeIn(r) for r in rectangulos_animados),
                    lag_ratio=0.4,
                    run_time=3.0,
                )
            )

            texto_total = Text(f"R₄ = {total_R4:.2f}", font_size=30, color=COLOR_DERECHA)
            texto_total.to_corner(UP + RIGHT, buff=0.8)
            self.play(FadeIn(texto_total))
            self.wait(1.5)

except ImportError:
    ConstruccionIzquierda = None
    ConstruccionDerecha = None
