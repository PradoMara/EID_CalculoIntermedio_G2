"""Comparación de sumas de Riemann; aquí no hay código de Manim.

Los registros matemáticos provienen de ``src.matematica``. Cada uno tiene
izquierda, derecha, muestra, ancho, altura y aporte.
"""


def comparar_sumas(funcion, particion):
    """Compara las muestras izquierda y derecha de LA MISMA partición.

    La diferencia se define siempre como derecha menos izquierda; por eso
    puede ser positiva, cero o negativa según la función y la partición.
    """
    from src.matematica import calcular_rectangulos, suma_riemann

    izquierdos = calcular_rectangulos(funcion, particion, "izquierda")
    derechos = calcular_rectangulos(funcion, particion, "derecha")

    if len(izquierdos) != len(derechos):
        raise ValueError("Las construcciones tienen distinta cantidad de rectángulos")

    diferencias = []
    for izquierdo, derecho in zip(izquierdos, derechos):
        # Comparar límites evita emparejar accidentalmente bases distintas.
        if (izquierdo["izquierda"], izquierdo["derecha"]) != (
            derecho["izquierda"], derecho["derecha"]
        ) or izquierdo["ancho"] != derecho["ancho"]:
            raise ValueError("Los rectángulos emparejados no comparten la base")
        diferencias.append(derecho["aporte"] - izquierdo["aporte"])

    total_izquierda = suma_riemann(funcion, particion, "izquierda")
    total_derecha = suma_riemann(funcion, particion, "derecha")
    return {
        "rectangulos_izquierda": izquierdos,
        "rectangulos_derecha": derechos,
        "total_izquierda": total_izquierda,
        "total_derecha": total_derecha,
        "diferencia_total": total_derecha - total_izquierda,
        "diferencias_aportes": diferencias,
    }


def extraer_detalle_intervalo(comparacion, indice):
    """Devuelve los dos rectángulos del intervalo ``indice`` (desde cero)."""
    izquierdos = comparacion["rectangulos_izquierda"]
    derechos = comparacion["rectangulos_derecha"]
    diferencias = comparacion["diferencias_aportes"]
    if not (len(izquierdos) == len(derechos) == len(diferencias)):
        raise ValueError("La comparación tiene cantidades incompatibles")
    if type(indice) is not int or not 0 <= indice < len(izquierdos):
        raise IndexError("Índice de intervalo fuera de rango")
    return {
        "izquierda": izquierdos[indice].copy(),
        "derecha": derechos[indice].copy(),
        "diferencia_aporte": diferencias[indice],
    }


def calcular_refinamientos(funcion, a, b, cantidades):
    """Calcula una fila por cantidad de subintervalos uniformes solicitada."""
    from src.matematica import crear_particion_uniforme

    filas = []
    for n in cantidades:
        if type(n) is not int or n <= 0:
            raise ValueError("Cada cantidad debe ser un entero positivo")
        particion = crear_particion_uniforme(a, b, n)
        comparacion = comparar_sumas(funcion, particion)
        filas.append({
            "n": n,
            "ancho": (b - a) / n,
            "total_izquierda": comparacion["total_izquierda"],
            "total_derecha": comparacion["total_derecha"],
            "diferencia_total": comparacion["diferencia_total"],
        })
    return filas
