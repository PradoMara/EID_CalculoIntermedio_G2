
# La partición es inmutable y define el intervalo y el número de subintervalos.
PARTICION_EJEMPLO = (0, 0.5, 1, 1.5, 2)
INTERVALO_EJEMPLO = (PARTICION_EJEMPLO[0], PARTICION_EJEMPLO[-1])
N_SUBINTERVALOS_EJEMPLO = len(PARTICION_EJEMPLO) - 1


def funcion_ejemplo(x):
    return x**2 + 1

import math
from collections.abc import Iterable, Mapping, Set
from decimal import Decimal
from numbers import Integral, Real


def validar_particion(particion):

    if (
        isinstance(particion, (str, bytes, bytearray, Mapping, Set))
        or not isinstance(particion, Iterable)
    ):
        raise ValueError("La partición debe ser una secuencia de números.")
    puntos = tuple(particion)
    if len(puntos) < 2:
        raise ValueError("La partición debe tener al menos dos puntos.")
    for p in puntos:
        if isinstance(p, bool) or not isinstance(p, (Real, Decimal)):
            raise ValueError(f"Valor no numérico en la partición: {p!r}.")
        try:
            finito = math.isfinite(p)
        except OverflowError:  # fracciones enormes: finitas pero sin float
            finito = True
        if not finito:
            raise ValueError(f"Valor no finito en la partición: {p!r}.")
    for anterior, actual in zip(puntos, puntos[1:]):
        if not anterior < actual:
            raise ValueError("Los puntos deben ser estrictamente crecientes.")
    return puntos

def crear_particion_uniforme(a, b, n):
    """Devuelve una tupla con los n+1 puntos equiespaciados entre a y b.

    Incluye ambos extremos (ancho (b-a)/n) y no redondea los puntos.
    Lanza ValueError si a<b no se cumple, los límites no son números
    finitos o n no es un entero positivo.
    """
    validar_particion((a, b))
    if isinstance(n, bool) or not isinstance(n, Integral) or n < 1:
        raise ValueError("n debe ser un entero positivo.")
    n = int(n)
    puntos = [a + (b - a) * i / n for i in range(n)]
    puntos.append(b)
    return validar_particion(puntos)

CRITERIOS_MUESTRA = ("izquierda", "derecha")


def seleccionar_muestra(izquierda, derecha, criterio):
    """Devuelve el punto de muestra de un subintervalo [izquierda, derecha].

    criterio admite dos valores: 'izquierda' (devuelve el límite izquierdo)
    o 'derecha' (devuelve el límite derecho). No evalúa ninguna función.
    Lanza ValueError si el criterio es desconocido o si
    izquierda >= derecha.
    """
    validar_particion((izquierda, derecha))
    if criterio == "izquierda":
        return izquierda
    if criterio == "derecha":
        return derecha
    raise ValueError(
        f"Criterio desconocido: {criterio!r}. Use 'izquierda' o 'derecha'."
    )
