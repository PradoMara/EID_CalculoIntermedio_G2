# Informe de Sebastian Pereda

Actualización: 17 de octubre de 2026. Revisión y cambios asistidos por Codex.
Este informe reemplaza las afirmaciones anteriores de cierre completo: los resultados aislados no acreditan integración ni revisión humana de la defensa.

## Trabajo propio realizado

| Tareas | Resultado | Límite de cierre |
| --- | --- | --- |
| T-005 | Corregida la generalización sobre funciones no constantes; se conserva el ejemplo correcto L=3.75, R=5.75, diferencia=2 e integral=14/3. | La consulta personal de bibliografía y su comprensión deben ser ratificadas por Sebastián; no se inventa una revisión cruzada. |
| T-010 | Documentada versión 0.22.0, procedencia de esta adaptación, referencias oficiales y procedimiento reproducible. | Los ejemplos didácticos del documento no equivalen a código ejecutado. |
| T-006 | Ajustadas las fases de los bloques propios; créditos especificados con 15 s dentro de 4:45; referencia del apunte corregida sin atribución institucional inventada. | Montaje, locución real y legibilidad final de créditos pendientes. |
| T-027 | Preparación geométrica verificada con cuatro pruebas aisladas. | Falta calcular_rectangulos de Daniel para integración real. |
| T-028–T-032 | Ejes rotulados, marcas para particiones irregulares, prevención de duplicados existentes; pruebas de curva, coordenadas, vértices y guías. | Verificado con Manim real; no sustituye revisión del montaje conjunto. |
| T-011 / T-033 | Muestra → altura → aporte → suma; 55 s por escena; panel de cálculos; total derivado de aportes. Eliminado respaldo silencioso con cifras manuales. | Escenas de producción esperan modelo real. Previsualización aislada disponible con aviso visible. |
| T-012 | Pruebas ampliadas y revisión de renders documentada abajo. | El resultado no implica que toda la suite del grupo pase. |
| T-013 / T-020 | No se declaran terminadas. | Video completo, voz propia, ensayo y validación humana pendientes. |

## Pruebas ejecutadas

Desde la raíz con el entorno existente:

```bash
.venv/bin/python -m unittest tests.test_datos_rectangulos tests.test_helpers_visuales -v
```

Resultado: **12 pruebas, 12 correctas**, sin omisiones, Manim Community 0.22.0.
Las cuatro de datos sustituyen src.matematica por un doble explícito. Las ocho de helpers incluyen objetos Manim reales y comprueban escala, rótulos, extremos de dos funciones distintas, marcas irregulares, duplicados, vértices, opacidad y posiciones de puntos/guías tras mover y escalar los ejes. También se comprueba que las dos escenas consumen los datos del proveedor y propagan errores, sin cifras de respaldo.

```bash
.venv/bin/python -m unittest discover -s tests -t . -v
```

Resultado: **29 pruebas: 28 correctas y 1 error**. El error es test_ejemplo_con_modelo_real de tests/test_comparacion.py: no existe calcular_rectangulos en src/matematica.py. No se modificaron los módulos ni las pruebas de Daniel/Rodrigo para ocultarlo.

## Revisión visual aislada

```bash
.venv/bin/python -m tests.render_construcciones_sebastian
```

El script utiliza el doble matemático de tests/test_datos_rectangulos.py exclusivamente para preparar datos de prueba. La animación es la misma que utilizarán las escenas de producción. Ambos videos incluyen «REVISIÓN AISLADA · datos de prueba · sin integración».

Archivos locales regenerables (media/ está ignorado por Git):
- media/revision_sebastian/videos/480p15/RevisionIzquierda.mp4
- media/revision_sebastian/videos/480p15/RevisionDerecha.mp4

Duración medida con PyAV: **55.0 segundos cada uno**, 854×480, 15 fps, sin audio.
Inspección de fotogramas en 6, 9, 12, 16, 36 y 54 segundos de ambas escenas: título, rótulos x/y y valores dentro del cuadro; panel separado de la gráfica; muestra antes de altura y aporte; bases alineadas, cuatro aportes y total legibles. Totales: 3.75 y 5.75. Esta inspección de fotogramas no es una prueba unitaria ni una revisión audiovisual humana completa.

Antes de entregar: render integrado con modelo real, calidad final y audio; comprobar sincronía con la toma de Sebastián. La locución del guion tiene 55 s asignados por construcción, pero no ha sido grabada ni medida.

## Asistencia de IA y validación personal

Codex ayudó a corregir fundamentos, documentación, helpers, animación y pruebas en esta revisión. Verificaciones realizadas por la herramienta: unitarias, render aislado, duración y fotogramas. No se afirma que Sebastián haya leído nuevas fuentes, dominado la guía, grabado voz o realizado un ensayo. Esos pasos personales permanecen pendientes de T-020. Este registro aporta los datos que necesita el responsable de consolidar declaracion_ia.md.
