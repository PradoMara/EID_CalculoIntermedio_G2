# EID de Cálculo Intermedio — Grupo 2

Proyecto de la asignatura **MAT1188**, desarrollado con Manim Community.

## Integrantes

| Integrante | GitHub |
| --- | --- |
| Daniel Prado — líder | PradoMara |
| Sebastian Pereda | SPereda2005 |
| Rodrigo Pedraza | rpedrazav |

## Tema y pregunta central

**Extremos izquierdos y extremos derechos.**

¿Por qué dos sumas construidas sobre la misma partición pueden entregar valores distintos?

## Función elegida

Usaremos **f(x) = x² + 1** en el intervalo **[0, 2]**, con **cuatro subintervalos iguales**:

- Partición: P = {0, 0.5, 1, 1.5, 2}.
- Número de subintervalos: n = 4.
- Ancho de cada rectángulo: Δx = 0.5.

La función es continua, positiva y creciente en este intervalo. Compararemos dos sumas conservando la función, el intervalo, la partición y las bases de los rectángulos. Cambiaremos el punto muestra: extremo izquierdo o extremo derecho de cada subintervalo.

| Criterio | Puntos muestra | Alturas | Suma esperada |
| --- | --- | --- | ---: |
| Izquierdo | 0, 0.5, 1, 1.5 | 1, 1.25, 2, 3.25 | 3.75 |
| Derecho | 0.5, 1, 1.5, 2 | 1.25, 2, 3.25, 5 | 5.75 |

Cada suma se obtiene multiplicando las alturas por 0.5 y sumando los aportes. La diferencia esperada es **2**. En este ejemplo, los extremos derechos producen alturas mayores, porque la función es creciente; esa conclusión no se aplica a cualquier función.

El video explicará cómo cambiar el punto muestra modifica las alturas y los aportes, aunque las bases sean iguales. El cierre conectará esta comparación con la integral: al refinar las particiones, ambas sumas convergen a la misma integral, cuyo valor es **14/3 ≈ 4.6667**. El refinamiento se distinguirá de la comparación principal con partición fija.

## Organización del trabajo

Trabajaremos directamente en `main`, coordinando cambios en archivos compartidos. Todos deben desarrollar código, escribir pruebas unitarias, aportar su propia voz y subir un resumen de su trabajo. Daniel se encarga de la instalación y configuración inicial.

- [Análisis del proyecto](docs/context/analisis.md).
- [Tareas de Daniel Prado](tasks/dprado.md).
- [Tareas de Sebastian Pereda](tasks/spereda.md).
- [Tareas de Rodrigo Pedraza](tasks/rpedraza.md).

Se permite usar IA, declarando la herramienta, la finalidad, las partes apoyadas y las verificaciones humanas realizadas. Cada integrante debe comprender y poder explicar sus aportes.

## Estado y ejecución

La función y la partición principal ya están elegidas. La implementación de módulos, las pruebas del producto y el video están pendientes (T-002 en adelante). El entorno ya está configurado (T-001); detalles y decisiones en [investigacion/configuracion_daniel.md](investigacion/configuracion_daniel.md).

### Versiones verificadas

| Herramienta | Versión |
| --- | --- |
| Python | 3.13.7 (Windows; Manim exige >= 3.10) |
| Manim Community | 0.22.0 |
| ffmpeg | incluido vía PyAV; no hace falta instalarlo aparte |
| LaTeX | **No instalado**. Solo sería necesario para `MathTex`/`Tex`; usar `Text` o instalar MiKTeX (ver documento de configuración) |

### Preparar otro equipo (PowerShell)

```powershell
git clone https://github.com/PradoMara/EID_CalculoIntermedio_G2.git
cd EID_CalculoIntermedio_G2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

En Linux/macOS, activar con `source .venv/bin/activate`; Manim requiere además Cairo y Pango del sistema (ver [instalación oficial](https://docs.manim.community/en/stable/installation.html)).

### Pruebas

```powershell
python -m unittest discover -s tests -t . -v
```

Con el entorno activado. `tests/test_entorno.py` comprueba dependencias y `tests/test_matematica.py` valida `funcion_ejemplo` y los datos compartidos de T-022. Las pruebas de las demás funciones matemáticas, `test_datos_rectangulos.py` y `test_comparacion.py` siguen pendientes.

El ejemplo principal se define en `src/matematica.py`: `funcion_ejemplo`, `PARTICION_EJEMPLO`, `INTERVALO_EJEMPLO` y `N_SUBINTERVALOS_EJEMPLO`. Los módulos deben importar estos datos compartidos.

### Render

```powershell
python -m manim render src/escenas/prueba_render.py PruebaRender
```

Genera `media/videos/prueba_render/480p15/PruebaRender.mp4` (baja calidad por `manim.cfg`). Para el render final: `-qh` (1080p60). `media/` y `.venv/` no se suben.

### Estructura y rutas de módulos

| Ruta | Contenido | Tarea |
| --- | --- | --- |
| `src/matematica.py` | Cálculo de sumas, sin Manim | Daniel (T-002) |
| `src/datos_rectangulos.py` | Datos visuales a partir del modelo | Sebastian (T-011) |
| `src/comparacion.py` | Diferencias por aporte y refinamiento | Rodrigo |
| `src/escenas/` | Escenas Manim (`construcciones.py`, `comparacion.py`); `prueba_render.py` es solo de verificación | Sebastian / Rodrigo |
| `tests/` | Pruebas `unittest` por módulo | Cada autor |
| `manim.cfg` | Configuración de render | Daniel |

Se importan como `src.matematica`, `src.escenas.comparacion`, etc., siempre desde la raíz del repositorio. Los enlaces a fuentes consultadas y la declaración de IA se añadirán al cerrar el proyecto.
