
# La partición es inmutable y define el intervalo y el número de subintervalos.
PARTICION_EJEMPLO = (0, 0.5, 1, 1.5, 2)
INTERVALO_EJEMPLO = (PARTICION_EJEMPLO[0], PARTICION_EJEMPLO[-1])
N_SUBINTERVALOS_EJEMPLO = len(PARTICION_EJEMPLO) - 1


def funcion_ejemplo(x):
    return x**2 + 1
