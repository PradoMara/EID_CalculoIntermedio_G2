# Informe de Daniel Prado

## T-003 — Pruebas unitarias del modelo matemático

- **Qué:** `tests/test_matematica.py` con clases separadas para `funcion_ejemplo`, `validar_particion`, `crear_particion_uniforme`, `seleccionar_muestra`, `calcular_rectangulos` y `suma_riemann`.
- **Por qué:** detectar errores del cálculo antes de que lleguen a las escenas.
- **Comando:** `python -m unittest tests.test_matematica`
- **Resultado real:** `Ran 24 tests ... OK`.
- **Commit verificado (código y pruebas):** `4ab898e` (T-002), sobre `ed9d426`, `c89b0f9` y `667230b`.

### Casos cubiertos
- Aportes y totales del ejemplo acordado (partición `[0, 0.5, 1, 1.5, 2]`): izquierda = 3.75 (aportes 0.5, 0.625, 1, 1.625) y derecha = 5.75 (aportes 0.625, 1, 1.625, 2.5), comparados con valores calculados a mano.
- Funciones constante, creciente y decreciente.
- Partición no uniforme `(0, 1, 3)`: anchos propios 1 y 2, totales 5 (izquierda) y 22 (derecha), sin fórmula telescópica uniforme.
- Rechazo de entradas inválidas (`ValueError`): criterio desconocido, intervalo con `izquierda>=derecha`, `n` inválido, límites no finitos o no numéricos, partición vacía, de un punto, duplicada o desordenada.
- Ausencia de mutación de la partición recibida.

## Declaración de uso de IA

Utilicé inteligencia artificial como apoyo para generar código y para obtener la función de ejemplo con la que trabajé. Codex me ayudó a generar código y Argon de Gemini me sugirió dicha función. Las pruebas unitarias y la revisión de la renderización las realicé manualmente.

## Fuente consultada y verificación humana

La fuente consultada fueron los apuntes de la asignatura proporcionados por la profesora(Apuntes.pdf). Revisé personalmente esos apuntes y los utilicé como referencia para el trabajo. No añadí otras fuentes externas.

