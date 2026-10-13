# Informe de Rodrigo Pedraza

Actualizado: 13 de octubre de 2026. Estado de trabajo, no informe final de entrega.

| Tarea | Avance verificable | Pendiente |
| --- | --- | --- |
| T-007, investigación | `investigacion/interpretacion_rodrigo.md`: fuente MIT, interpretación, cálculo independiente y texto para guion. | Sebastian debe confirmar que su fuente es distinta, compartir sus cálculos y recibir el texto. |
| T-014, IA y créditos | `declaracion_ia.md`: registro inicial honesto y lista de datos faltantes. | Obtener registros reales de Daniel, Sebastian y Rodrigo; identificar medios externos del video. |
| T-034, comparación | `src/comparacion.py`: totales, diferencias locales y verificación de bases/cantidades. | Prueba de integración con `src/matematica.py` real. |
| T-035, detalle | `src/comparacion.py`: selección por índice y copias de registros. | Consumo por escena Manim. |
| T-036, refinamientos | `src/comparacion.py`: una partición uniforme compartida por fila. | Prueba de integración con el constructor real de particiones. |
| T-016, pruebas | `tests/test_comparacion.py`: ejemplo, detalle, refinamientos, casos constante/decreciente y errores. Render de prueba de las tres escenas con dobles temporales. | Integración y render con los módulos reales. |
| T-015/T-037/T-038, escenas | `src/escenas/comparacion.py`: tres clases implementadas; render de prueba con dobles y capturas inspeccionadas. | Ajustes y render final tras recibir el módulo de Daniel y los helpers de Sebastian. |
| T-017, edición | Sin ensamblado aún. | Guion, clips, tres grabaciones reales, créditos y herramienta de edición acordada. |
| T-021, voz y defensa | Guía de estudio y preguntas de práctica preparadas. | Grabar voz propia, registrar escucha y ensayo personal. |

## Prueba ejecutada

Comandos: `python -m unittest tests.test_comparacion -v` y luego `python -m unittest discover -s tests -t . -v` desde la raíz del repositorio. La suite completa dio **11 pruebas, 10 correctas y 1 omitida**. La omitida es la integración con `src.matematica`, todavía ausente. Ocho pruebas matemáticas usan un doble de la interfaz acordada; dos comprueban el entorno. La primera ejecución de la suite completa reveló que faltaban archivos `__init__.py` para el descubrimiento en este entorno; se añadieron y se repitió con éxito.

Se ejecutó `python -m manim render -ql preview_rodrigo_temp.py DetalleIntervalo ComparacionSumas CierreIntegral` con un archivo temporal que simulaba `src.matematica`, `src.datos_rectangulos` y los helpers de Sebastian. Los tres MP4 de baja calidad se generaron en `media/` (ignorado por Git). Se inspeccionaron fotogramas; el texto causal de `ComparacionSumas` se recortaba, se dividió en dos líneas y el nuevo render ya no lo recorta. El archivo de simulación temporal se eliminó. Esta evidencia no sustituye el render de integración real.

Valores comprobados: `L₄=3.75`, `R₄=5.75`, diferencia `2`; aportes de `[1,1.5]`: `1` y `1.625`; refinamientos de `n=8` y `n=16` coinciden con la tabla del proyecto. Un caso constante da diferencia cero; `f(x)=5-x` en `[0,2]` da diferencia `-1` con esta partición.

## Créditos y fuente que se deben pasar al guion

Rodrigo consultó el apunte del curso y el texto en línea de Daniel Kleitman / MIT OpenCourseWare, *18.013A Calculus with Applications*, capítulo 20, secciones 20.2, 20.3 y 20.5 (curso MIT OCW 2005). Enlace y conclusión precisa en `investigacion/interpretacion_rodrigo.md`. No se incorporó música, imagen ni código externo a sus archivos. La redacción y el código se prepararon con ayuda de Codex; el alcance está en `declaracion_ia.md`.

## Evidencia que Rodrigo debe completar personalmente

1. Leer `src/comparacion.py` y explicar en voz alta por qué se comprueba la cantidad antes de `zip`.
2. Calcular en papel un aporte izquierdo, uno derecho y la diferencia de un intervalo.
3. Cuando aparezcan los módulos de compañeros, ejecutar toda la suite y registrar resultados reales.
4. Inspeccionar los tres renders en pantalla y anotar legibilidad, escalas y duración.
5. Grabar el audio de su sección con su propia voz; indicar archivo/toma usada y escuchar el resultado final.
6. Ensayar la defensa completa, incluida una variación de función o partición.

**Commit:** no se creó un commit en esta sesión; registrar el SHA cuando se guarden los cambios acordados por el grupo.
