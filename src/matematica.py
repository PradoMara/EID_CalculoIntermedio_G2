
# La partición es inmutable y define el intervalo y el número de subintervalos.
PARTICION_EJEMPLO = (0, 0.5, 1, 1.5, 2)
INTERVALO_EJEMPLO = (PARTICION_EJEMPLO[0], PARTICION_EJEMPLO[-1])
N_SUBINTERVALOS_EJEMPLO = len(PARTICION_EJEMPLO) - 1


def funcion_ejemplo(x):
    return x**2 + 1

import math
from collections.abc import Iterable, Mapping, Set
from decimal import Decimal
from numbers import Real


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
