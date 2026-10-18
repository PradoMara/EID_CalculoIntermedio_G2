"""Introducción de 65 s basada en Anatomía_de_las_Sumas_de_Riemann.pdf.

Render desde la raíz: .venv/Scripts/python -m manim render
    src/escenas/introduccion.py IntroduccionRiemann -r 1920,1080 --fps 30
No requiere LaTeX. Las figuras son objetos vectoriales animados de Manim.
"""
from manim import *
from src.matematica import funcion_ejemplo, PARTICION_EJEMPLO, calcular_rectangulos

BG = "#101B2B"
INK = "#F3F5F7"
BLUE = "#56B4E9"
ORANGE = "#E69F00"
MUTED = "#BCCADA"


def text(value, size=30, color=INK):
    return Text(value, font="Sans", font_size=size, color=color)


class IntroduccionRiemann(Scene):
    def header(self, title, number):
        return VGroup(text(title, 34).to_edge(UP, buff=.65),
                      text(f"{number} / 6", 20, MUTED).to_corner(UR, buff=.3))

    def until(self, seconds):
        self.wait(max(0, seconds - self.time))

    def clear_content(self):
        objects = [m for m in self.mobjects if m is not self.footer]
        self.play(*[FadeOut(m) for m in objects], run_time=.4)

    def graph(self, center=LEFT*2.8):
        axes = Axes(x_range=[0, 2.25, .5], y_range=[0, 5.5, 1],
                    x_length=5.8, y_length=3.6, tips=False,
                    axis_config={"color": MUTED, "include_ticks": True})
        axes.move_to(center + DOWN*.2)
        labels = VGroup(*[text(str(x).replace('.', ','), 21, MUTED).next_to(axes.c2p(x,0), DOWN, buff=.13)
                         for x in PARTICION_EJEMPLO],
                        text("x", 22).next_to(axes.x_axis, RIGHT, buff=.1),
                        text("y", 22).next_to(axes.y_axis, UP, buff=.1))
        curve = axes.plot(funcion_ejemplo, x_range=[0,2], color=INK, stroke_width=4)
        return axes, labels, curve

    def rectangles(self, axes, criterion, color):
        result = VGroup()
        for r in calcular_rectangulos(funcion_ejemplo, PARTICION_EJEMPLO, criterion):
            a,b,h = r['izquierda'],r['derecha'],r['altura']
            result.add(Polygon(axes.c2p(a,0), axes.c2p(b,0), axes.c2p(b,h), axes.c2p(a,h),
                               color=color, fill_color=color, fill_opacity=.35, stroke_width=2))
        return result

    def construct(self):
        self.camera.background_color = BG
        self.footer = VGroup(text("Narrador: Daniel Prado", 18, MUTED).to_corner(DL, buff=.3),
                             text("Grupo 2 · MAT1188 · Manim Community", 18, MUTED).to_corner(DR, buff=.3))
        self.add(self.footer)
        # 00:00–00:11: presentación y pregunta.
        title = text("Anatomía de las sumas de Riemann", 39).shift(UP*2.5)
        team = text("Daniel Prado · Sebastian Pereda · Rodrigo Pedraza", 25, MUTED).shift(UP*1.65)
        question = VGroup(text("¿Por qué dos sumas sobre la", 35),
                          text("misma partición", 43, BLUE),
                          text("pueden dar valores distintos?", 35)).arrange(DOWN, buff=.22).shift(DOWN*.15)
        self.play(FadeIn(title), FadeIn(team), run_time=1)
        self.play(LaggedStart(*[FadeIn(m, shift=UP*.15) for m in question], lag_ratio=.25), run_time=1.5)
        self.until(10.6)
        self.clear_content()
        # 00:11–00:20: hipótesis e interpretación geométrica.
        h = self.header("1. El escenario geométrico", 2)
        axes, labels, curve = self.graph()
        area = axes.get_area(curve, x_range=[0,2], color=BLUE, opacity=.2)
        notes = VGroup(text("Continua en [a, b]", 30), text("f(x) ≥ 0", 36, BLUE),
                       text("Aportes = áreas", 28), text("de los rectángulos", 28)).arrange(DOWN,buff=.32).move_to(RIGHT*3.35)
        self.play(FadeIn(h), Create(axes), FadeIn(labels), run_time=.8)
        self.play(Create(curve), FadeIn(area), FadeIn(notes), run_time=1.2)
        self.until(19.6)
        self.clear_content()
        # 00:20–00:32: partición y base genérica.
        h = self.header("2. La partición fija las bases", 3)
        formula = text("P = {x₀, x₁, …, xₙ}     a = x₀ < x₁ < … < xₙ = b", 29).shift(UP*1.7)
        line = Line(LEFT*5.5, RIGHT*5.5, color=MUTED).shift(DOWN*.1)
        ticks = VGroup()
        for x,label in [(-5,"x₀ = a"),(-3,"x₁"),(-1,"xᵢ₋₁"),(1,"xᵢ"),(3,"…"),(5,"xₙ = b")]:
            ticks.add(VGroup(Line([x,-.23,0],[x,.03,0], color=INK),text(label,25).move_to([x,-.55,0])))
        base = Line([-1,-.1,0],[1,-.1,0],color=BLUE,stroke_width=12)
        interval = text("[xᵢ₋₁, xᵢ]",34,BLUE).shift(UP*.65)
        width = text("Δxᵢ = xᵢ − xᵢ₋₁",38,BLUE).shift(DOWN*1.65)
        self.play(FadeIn(h), FadeIn(formula), Create(line), run_time=.8)
        self.play(LaggedStart(*[FadeIn(m) for m in ticks],lag_ratio=.15),run_time=1.2)
        self.play(Create(base), FadeIn(interval), FadeIn(width),run_time=1)
        self.until(31.6)
        self.clear_content()
        # 00:32–00:45: descomposición de la suma sin dependencia de LaTeX.
        h = self.header("3. Cada aporte es altura × base", 4)
        sigma = VGroup(text("n",24).move_to([-3.5,1.2,0]),text("Σ",85).move_to([-3.5,.35,0]),
                       text("i = 1",22).move_to([-3.5,-.5,0]))
        height = text("f(xᵢ*)",58,ORANGE).move_to([-.9,.35,0])
        times = text("·",50).move_to([1,.35,0])
        width = text("Δxᵢ",58,BLUE).move_to([2.7,.35,0])
        captions = VGroup(text("sumar n aportes",23).move_to([-3.5,-1.25,0]),
                          text("altura",27,ORANGE).move_to([-.9,-1.25,0]),
                          text("base",27,BLUE).move_to([2.7,-1.25,0]))
        sample = text("xᵢ* ∈ [xᵢ₋₁, xᵢ]  :  punto muestra",29,ORANGE).shift(DOWN*2.35)
        self.play(FadeIn(h), FadeIn(sigma), run_time=.7)
        self.play(FadeIn(height), FadeIn(times), FadeIn(width), FadeIn(captions), run_time=1.3)
        self.play(FadeIn(sample), Indicate(height, color=ORANGE),run_time=1)
        self.until(44.6)
        self.clear_content()
        # 00:45–00:58: misma geometría de bases, distintas alturas.
        h = self.header("4. Cambiar la muestra cambia la altura", 5)
        axes,labels,curve = self.graph()
        left = self.rectangles(axes,'izquierda',BLUE)
        right = self.rectangles(axes,'derecha',ORANGE)
        dots = VGroup(*[Dot(axes.c2p(x,funcion_ejemplo(x)),color=BLUE,radius=.07) for x in PARTICION_EJEMPLO[:-1]])
        targets = VGroup(*[Dot(axes.c2p(x,funcion_ejemplo(x)),color=ORANGE,radius=.07) for x in PARTICION_EJEMPLO[1:]])
        criterion = text("Izquierda: xᵢ* = xᵢ₋₁",29,BLUE).move_to([3.3,1.25,0])
        new_criterion = text("Derecha: xᵢ* = xᵢ",29,ORANGE).move_to(criterion)
        fixed = VGroup(text("Mismas bases",31,BLUE),text("Distintas alturas",31,ORANGE),
                       text("Distintos aportes",28)).arrange(DOWN,buff=.4).move_to([3.3,-.55,0])
        self.play(FadeIn(h),Create(axes),FadeIn(labels),Create(curve),run_time=.7)
        self.play(LaggedStart(*[FadeIn(r) for r in left],lag_ratio=.2),FadeIn(dots),FadeIn(criterion),run_time=1.3)
        self.until(50)
        self.play(Transform(left,right),Transform(dots,targets),Transform(criterion,new_criterion),run_time=2)
        self.play(FadeIn(fixed),run_time=.7)
        self.until(57.6)
        self.clear_content()
        # 00:58–01:05: enlace con el bloque de Sebastian.
        h = self.header("5. Nuestro ejemplo",6)
        cards = VGroup()
        for center,label,value,color in [((-3,1),"FUNCIÓN","f(x) = x² + 1",BLUE),((3,1),"INTERVALO","[0, 2]",ORANGE),
                                         ((-3,-1.1),"SUBINTERVALOS","n = 4",BLUE),((3,-1.1),"ANCHO","Δx = 0,5",ORANGE)]:
            box = RoundedRectangle(width=5.3,height=1.7,corner_radius=.15,color=color,fill_color=color,fill_opacity=.06)
            content=VGroup(text(label,21,MUTED),text(value,36)).arrange(DOWN,buff=.25)
            cards.add(VGroup(box,content).move_to([*center,0]))
        self.play(FadeIn(h),LaggedStart(*[FadeIn(c,shift=UP*.1) for c in cards],lag_ratio=.2),run_time=1.2)
        self.until(65)
