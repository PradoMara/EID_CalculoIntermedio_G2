"""Módulo de preparación de datos geométricos para Manim (Tarea T-027).

Autor: Sebastian Pereda (Sublíder)
Convierte los registros del modelo matemático en estructuras geométricas puras
(vértices matemáticos) para Manim, sin renderizar ni depender de píxeles.
"""


def preparar_datos_rectangulos(funcion, particion, criterio):
    """Consume `calcular_rectangulos` de `src.matematica` y prepara los vértices.

    Cada registro devuelto conserva los seis campos matemáticos originales:
    - izquierda, derecha, muestra, ancho, altura, aporte
    y añade:
    - vertices_matematicos: lista de 4 tuplas (x, y) en orden continuo cerrado:
      [(izquierda, 0), (derecha, 0), (derecha, altura), (izquierda, altura)]
    - criterio: 'izquierda' o 'derecha'

    No convierte unidades a píxeles ni mueve la base al punto muestra.
    """
    from src.matematica import calcular_rectangulos

    rectangulos_mat = calcular_rectangulos(funcion, particion, criterio)
    datos_geometricos = []

    for reg in rectangulos_mat:
        izq = reg["izquierda"]
        der = reg["derecha"]
        alt = reg["altura"]

        # Vértices geométricos del rectángulo con base sobre y=0
        # 1: abajo-izquierda, 2: abajo-derecha, 3: arriba-derecha, 4: arriba-izquierda
        vertices = [
            (izq, 0.0),
            (der, 0.0),
            (der, alt),
            (izq, alt),
        ]

        dato = reg.copy()
        dato["vertices_matematicos"] = vertices
        dato["criterio"] = criterio
        datos_geometricos.append(dato)

    return datos_geometricos
