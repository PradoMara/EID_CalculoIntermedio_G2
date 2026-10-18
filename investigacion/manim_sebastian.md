# T-010 — Manim: animar sumas de Riemann (investigación técnica)

**Autor:** Sebastian Pereda (@seba / Sublíder)  
**Fecha:** 10 de octubre de 2026 (consolidado al 14 de octubre de 2026)  
**Tema:** Representación visual de extremos izquierdos y derechos en Manim Community  
**Propósito:** Definir el sistema de coordenadas, escala, geometría de rectángulos, marcadores y accesibilidad visual.

---

## 1. Sistema de coordenadas y escala

Las coordenadas matemáticas $(x, y)$ son tus datos; Manim solo dibuja en unidades de escena, y `Axes.c2p` es el único puente entre ambos espacios.

### Tres espacios que no hay que mezclar

| Espacio | Qué representa | Ejemplo en este proyecto |
| :--- | :--- | :--- |
| **Matemático** | El plano cartesiano abstracto de la función, con $x \in [0, 2]$ e $y \in [0, 5]$. | El punto $(1{,}5; 3{,}25)$ sobre $f(x) = x^2 + 1$. |
| **Escena de Manim** | Unidades de escena: origen en el centro del cuadro, $x$ hacia la derecha, $y$ hacia arriba, $z = 0$. Un punto es un arreglo $[x, y, 0]$. | `Dot((2, 2, 0))` cae en esa posición de pantalla, sin importar dónde estén los ejes. |
| **Píxeles** | Solo existen al renderizar: `pixel_width × pixel_height` según la calidad elegida. | $1920 \times 1080$ con `-qh`; $854 \times 480$ con `-ql`. |

Por defecto el cuadro de Manim mide 8 unidades de alto y unas 14,22 de ancho (16:9), de modo que en 1080p una unidad de escena equivale a unos 135 px. **Nunca programes en píxeles**: cambiar la calidad de render no debe mover nada.

### Configurar `Axes` con escala fija

Parámetros utilizados (esquema ilustrativo, no firma ejecutable):
```python
Axes(x_range, y_range, x_length=12, y_length=6, axis_config, x_axis_config, y_axis_config, tips=True, **kwargs)
```

| Parámetro | Significado según la documentación | Valor propuesto |
| :--- | :--- | :--- |
| `x_range` | Valores `(x_min, x_max, x_step)` del eje x | `[0, 2, 0.5]` |
| `y_range` | Valores `(y_min, y_max, y_step)` del eje y | `[0, 5, 1]` |
| `x_length` | Longitud del eje x en unidades de escena (por defecto 12) | `9` |
| `y_length` | Longitud del eje y en unidades de escena (por defecto 6) | `5.5` |
| `tips` | Si se dibujan puntas de flecha en ambos ejes (por defecto `True`) | `False` |

La escala (unidades de escena por unidad matemática) sale de dividir la longitud entre el rango:
$$u_x = \frac{x\_\text{length}}{x_{\max} - x_{\min}} = \frac{9}{2} = 4{,}5 \qquad u_y = \frac{y\_\text{length}}{y_{\max} - y_{\min}} = \frac{5{,}5}{5} = 1{,}1$$

### Para que la escala sea idéntica en todas las escenas:
* Declara `x_range`, `y_range`, `x_length` e `y_length` una sola vez, en un módulo compartido, y crea los ejes siempre con la misma función. No dependas de los valores por defecto.
* Usa el mismo rango en la escena de la suma izquierda, la de la derecha y la comparativa, para que al superponer cuadros todo coincida.
* Construye cada Mobject con `ax.c2p`, después de colocar los ejes. Si mueves o escalas `ax` más tarde, los objetos ya creados no lo siguen, salvo que estén en el mismo `VGroup`.
* Con `tips=False` el extremo del eje coincide con el final del rango, así que $f(2) = 5$ queda en el borde superior sin puntas que lo tapen.

```python
# Módulo compartido de configuración de ejes
from manim import Axes

X_RANGE = [0, 2, 0.5]
Y_RANGE = [0, 5, 1]
X_LENGTH = 9
Y_LENGTH = 5.5

def make_axes():
    return Axes(
        x_range=X_RANGE,
        y_range=Y_RANGE,
        x_length=X_LENGTH,
        y_length=Y_LENGTH,
        tips=False,
        axis_config={'include_numbers': True},
    )
```

### Cómo funciona `c2p`
`axes.c2p(x, y)` es la abreviatura de `coords_to_point`: recibe coordenadas matemáticas y devuelve el punto de escena correspondiente como arreglo NumPy de tres componentes $[X, Y, 0]$. Equivale a `ax @ (x, y)`, y el método inverso es `point_to_coords` (`p2c`).

Para rangos que empiezan en 0:
$$(x, y) \longmapsto \mathbf{O} + x \cdot u_x \hat{\imath} + y \cdot u_y \hat{\jmath}$$
donde $\mathbf{O}$ es el origen de los ejes. Como $u_x = 4{,}5$ y $u_y = 1{,}1$, los rectángulos siguen teniendo ángulos rectos pero se adaptan a la proporción de los ejes.

**Errores típicos a evitar:**
* *Dibujar rectángulos con `Rectangle(width=0.5, height=2)`*: usa unidades de escena, no matemáticas, y desalinea la escala. Siempre usar vértices obtenidos con `c2p`.
* *Mezclar espacios*: `Dot((1.5, 3.25, 0))` es un punto en el centro de la pantalla, no el punto matemático $(1{,}5; 3{,}25)$.

---

## 2. Construcción geométrica de rectángulos y muestras

Calcula primero todos los números en Python puro y construye después los Mobjects con `c2p`: así los rectángulos salen exactos y puedes comprobar la matemática sin esperar un render.

### Por qué separar datos de objetos visuales
1. **Verificable:** Puedes comprobar con `assert` que $L_4 = 3{,}75$ y $R_4 = 5{,}75$ en milisegundos sin Manim.
2. **Una sola fuente de verdad:** La misma lista de datos alimenta rectángulos, puntos, etiquetas y tabla de aportes, evitando desincronizaciones.
3. **Reutilizable:** La suma izquierda y la derecha comparten la partición; solo cambia la regla del punto muestra.
4. **Aislado del estilo:** Cambiar colores, escala o animaciones no altera el cálculo.

```python
# riemann_data.py: Python puro, sin dependencias de Manim
def f(x):
    return x**2 + 1

def partition(a, b, n):
    dx = (b - a) / n
    return [a + i * dx for i in range(n + 1)]

def riemann_rows(f, P, rule):  # rule: 'left' o 'right'
    rows = []
    for i in range(1, len(P)):
        x_prev, x_i = P[i - 1], P[i]
        x_star = x_prev if rule == 'left' else x_i
        y_h = f(x_star)
        rows.append({
            'i': i,
            'x_prev': x_prev,
            'x_i': x_i,
            'x_star': x_star,
            'y_h': y_h,
            'area': y_h * (x_i - x_prev)
        })
    return rows
```

### El rectángulo como polígono de 4 vértices
Para el subintervalo $[x_{i-1}, x_i]$ con altura $y_h = f(x_i^*)$, los vértices matemáticos en orden de recorrido cerrado continuo son:

| Orden | Vértice matemático | Posición en el rectángulo |
| :-: | :--- | :--- |
| 1 | $(x_{i-1}, 0)$ | Abajo a la izquierda |
| 2 | $(x_i, 0)$ | Abajo a la derecha |
| 3 | $(x_i, y_h)$ | Arriba a la derecha |
| 4 | $(x_{i-1}, y_h)$ | Arriba a la izquierda |

```python
def make_rect(ax, x_prev, x_i, y_h, color):
    verts = [
        ax.c2p(x_prev, 0),
        ax.c2p(x_i, 0),
        ax.c2p(x_i, y_h),
        ax.c2p(x_prev, y_h),
    ]
    return Polygon(*verts, color=color, fill_opacity=0.35, stroke_width=2)
```

En el subintervalo $[1, 1{,}5]$: el ancho en pantalla es $\Delta x \cdot u_x = 0{,}5 \cdot 4{,}5 = 2{,}25$ unidades en ambas sumas, mientras que la altura pasa de $f(1) \cdot u_y = 2 \cdot 1{,}1 = 2{,}2$ unidades (izquierda) a $f(1{,}5) \cdot u_y = 3{,}25 \cdot 1{,}1 = 3{,}575$ unidades (derecha). La base no se mueve; solo cambia la altura.

### Marcadores: punto muestra, punto en la curva y altura

| Marcador | Coordenadas matemáticas | Mobject en Manim |
| :--- | :--- | :--- |
| **Punto muestra en eje X** | $(x_i^*, 0)$ | `Dot(ax.c2p(x_star, 0))` |
| **Punto sobre la curva** | $(x_i^*, f(x_i^*))$ | `Dot(ax.c2p(x_star, y_h))` |
| **Altura vertical** | Segmento de $(x_i^*, 0)$ a $(x_i^*, f(x_i^*))$ | `DashedLine(p_axis, p_curve)` |

```python
def make_markers(ax, x_star, y_h, color):
    p_axis = ax.c2p(x_star, 0)     # (x*, 0) en eje X
    p_curve = ax.c2p(x_star, y_h)   # (x*, f(x*)) en curva
    dot_axis = Dot(p_axis, radius=0.08, color=color)
    dot_curve = Dot(p_curve, radius=0.08, color=color)
    height_line = DashedLine(p_axis, p_curve, dash_length=0.1, stroke_width=3, color=color)
    return VGroup(height_line, dot_axis, dot_curve)
```

*Nota sobre la API:* `ax.get_riemann_rectangles` existe en Manim, pero ensancha artificialmente cada base (`width_scale_factor=1.001`) y tiene opacidad $1$ por defecto. Construir los rectángulos con `Polygon` propio otorga control geométrico exacto e independiente para cada subintervalo y sus marcadores.

---

## 3. Diseño visual y accesibilidad

Se utiliza el par azul–naranja de la paleta **Okabe–Ito** (Okabe & Ito, 2008), elegida para favorecer la distinción de categorías; no garantiza por sí sola accesibilidad para todas las personas ni en escala de grises. Se evita explícitamente el par conflictivo rojo–verde.

### Paleta y contrastes (WCAG 2.1)

| Elemento | Fondo oscuro (Manim por defecto) | Fondo claro | Nota |
| :--- | :--- | :--- | :--- |
| **Suma izquierda $L$** | `#56B4E9` (azul cielo) | `#0072B2` (azul) | Contraste aprox. 9:1 sobre negro, 5:1 sobre blanco |
| **Suma derecha $R$** | `#E69F00` (naranja) | `#D55E00` (bermellón) | Contraste aprox. 9:1 sobre negro, 4:1 sobre blanco |
| **Curva $f(x)$** | `#FFFFFF` | `#000000` | Trazo grueso, contraste máximo |
| **Ejes** | `#BBBBBB` | `#555555` | Discretos, no compiten con los datos |
| **Referencia ($\int = 14/3$)** | `#009E73` (verde azulado) | `#009E73` | Para el cierre de refinamiento |

Los valores anteriores describen colores opacos. El relleno con opacidad 0.35 tiene otro contraste efectivo: no se declara conformidad WCAG del render completo. Los contornos, textos y posiciones aportan señales adicionales.

**Señales redundantes (no depender solo del color):**
* Rotular siempre con texto explícito: «Suma izquierda $L_4 = 3{,}75$» y «Suma derecha $R_4 = 5{,}75$».
* Posición espacial redundante: el marcador izquierdo está en el borde izquierdo del subintervalo y el derecho en el borde derecho.

### Opacidad, bordes y orden de capas (`z_index`)

| Capa | `z_index` | Mobject | Motivo |
| :-: | :-: | :--- | :--- |
| 1 | 1 | Rectángulos (`Polygon`) | Relleno `fill_opacity=0.35`, contorno `stroke_width=2`. Permite ver ejes y curva detrás. |
| 2 | 2 | Ejes (`Axes`) | Base de referencia visible. |
| 3 | 3 | Curva $f(x)$ (`ax.plot`) | Trazo `stroke_width=4` dominante. |
| 4 | 4 | Líneas de altura (`DashedLine`) | Trazo `stroke_width=3` para guiar la mirada. |
| 5 | 5 | Puntos (`Dot`) | Radio `0.08`, bien contrastados. |
| 6 | 6 | Etiquetas (`Text`/`MathTex`) | Tamaño $\ge 28$, legibles sin tapar elementos clave. |

---

## 4. Ejemplo mínimo de código didáctico

```python
# riemann_min.py
from manim import *

class RiemannRectangle(Scene):
    def construct(self):
        f = lambda x: x**2 + 1
        
        ax = Axes(
            x_range=[0, 2, 0.5],
            y_range=[0, 5, 1],
            x_length=9,
            y_length=5.5,
            tips=False,
            axis_config={'include_numbers': True},
        )
        curve = ax.plot(f, x_range=[0, 2], color=WHITE, stroke_width=4)
        
        # Subintervalo [1, 1.5] con suma izquierda
        x_prev, x_i = 1.0, 1.5
        y_h = f(x_prev)  # f(1) = 2.0
        
        rect = Polygon(
            ax.c2p(x_prev, 0),
            ax.c2p(x_i, 0),
            ax.c2p(x_i, y_h),
            ax.c2p(x_prev, y_h),
            color='#56B4E9',
            fill_opacity=0.35,
            stroke_width=2,
        )
        
        self.add(ax, rect, curve)
```
*Comando de render:* `manim -pql riemann_min.py RiemannRectangle` (para previsualización rápida a 480p) o `-qh` (para 1080p final).

---

## 5. Referencias oficiales de Manim Community consultadas

| Tema | Módulo / Clase | Qué respalda |
| :--- | :--- | :--- |
| **Ejes** | `manim.mobject.graphing.coordinate_systems.Axes` | Parámetros `x_range`, `y_range`, `x_length`, `y_length`, `axis_config`, `tips`; métodos `coords_to_point` y `point_to_coords`. |
| **Sistema base** | `manim.mobject.graphing.coordinate_systems.CoordinateSystem` | `c2p`, `p2c`, `plot`, `get_riemann_rectangles`, `get_vertical_line`, `get_area`. |
| **Polígono** | `manim.mobject.geometry.polygram.Polygon` | `Polygon(*vertices, **kwargs)`: lazo cerrado continuo de vértices en coordenadas de escena. |
| **Línea de altura** | `manim.mobject.geometry.line.DashedLine` | `DashedLine(*args, dash_length, dashed_ratio)`. |
| **Marcadores** | `manim.mobject.geometry.arc.Dot` | `Dot(point, radius, color)`. |
| **Grupos** | `manim.mobject.types.vectorized_mobject.VGroup` | Agrupación de rectángulo y marcadores para animación por subintervalo. |
| **Animación en cascada** | `manim.animation.composition.LaggedStart` | Aparición secuencial de rectángulos en la escena. |
| **Orden y capas** | `manim.mobject.mobject.Mobject` | Propiedad `set_z_index` para control de superposición visual. |
| **Configuración** | Guía de configuración oficial de Manim | Medidas de cuadro de escena (8 de alto, 14.22 de ancho en 16:9). |


## 6. Implementación y revisión reproducible — 17 de octubre de 2026

Versión ejecutada: Manim Community 0.22.0, coincidente con requirements.txt.
Consulta de esta revisión (asistida por Codex):
- [Axes: rangos, dimensiones y conversión de coordenadas](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html).
- [Polygon: construcción a partir de vértices](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Polygon.html).

Procedencia: los ejemplos anteriores son desarrollos didácticos del proyecto basados en estas APIs; no se presentan como ejemplos oficiales copiados ni como código ejecutado. La implementación ejecutada es src/escenas/construcciones.py. La revisión del 17 de octubre añadió con asistencia de Codex etiquetas Text, marcas, pruebas geométricas y animación por fases. Se usa Text para evitar depender de LaTeX; los ejemplos antiguos con include_numbers=True pueden requerir LaTeX y no son el comando de ejecución recomendado.

La escala base sigue siendo 4.5 horizontal y 1.1 vertical. Las dos construcciones aplican 0.72, como ComparacionSumas: escala efectiva 3.24 horizontal y 0.792 vertical. CierreIntegral tiene otra composición (0.68); no se modificó el módulo de Rodrigo. Los rótulos se agrupan con los ejes para conservar su posición al transformarlos.

Procedimiento:
1. Ejecutar `.venv/bin/python -m unittest tests.test_datos_rectangulos tests.test_helpers_visuales -v`.
2. Ejecutar `.venv/bin/python -m tests.render_construcciones_sebastian` para una revisión aislada, rotulada como tal, con el doble matemático de pruebas. No acredita integración.
3. Inspeccionar cuadros iniciales, muestra, altura, aporte y cierre de ambos videos: rótulos dentro del cuadro, bases iguales, panel separado de la curva, totales correctos y guía alineada.
4. Medir duración de cada archivo: 55 segundos previstos. Revisar posteriormente sincronía con la voz real y legibilidad en la resolución de entrega.
5. Cuando esté disponible calcular_rectangulos, ejecutar las escenas de producción con `python -m manim render -ql src/escenas/construcciones.py ConstruccionIzquierda ConstruccionDerecha`. Ya no sustituyen importaciones fallidas por datos manuales.

Resultados y límites de la revisión: informes/spereda.md. El audio y la validación humana de la defensa siguen pendientes.
