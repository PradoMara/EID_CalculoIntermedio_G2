# Declaración de Uso de Inteligencia Artificial (IA) y Recursos Externos — Grupo 2

**Asignatura:** Cálculo Intermedio (MAT1188) — Semestre 2026  
**Grupo:** Grupo 02 (G02)  
**Tema:** Extremos izquierdos y extremos derechos en Sumas de Riemann  
**Pregunta central:** ¿Por qué dos sumas construidas sobre la misma partición pueden entregar valores distintos?  
**Fecha de consolidación final:** 18 de octubre de 2026  
**Compromiso ético:** Este registro responde al Código de Ética del Grupo (`docs/MAT1188_ETICA_G02_2026.pdf`) y a la rúbrica de evaluación (Criterio V7.c). No atribuye a los integrantes comprensiones ni verificaciones que no hayan sido efectivamente realizadas y validadas de forma independiente.

---

## 1. Principio Fundamental y Límites de la IA

Las herramientas de inteligencia artificial utilizadas durante el proyecto actuaron exclusivamente como **apoyo técnico y metodológico** en tareas de programación, estructuración sintáctica, generación de pruebas automatizadas y redacción de borradores. 

**La IA no sustituye en ningún caso:**
1. Las fuentes bibliográficas formales del curso (apunte docente, texto de James Stewart y texto de Daniel Kleitman / MIT OCW).
2. El cálculo matemático riguroso realizado a mano.
3. La comprensión conceptual individual requerida para la defensa oral obligatoria.
4. La locución real de los tres integrantes en el video final.

---

## 2. Matriz de Uso de IA por Integrante y Tarea

| Integrante | Herramienta(s) | Finalidad y componentes apoyados | Verificación humana realizada |
| :--- | :--- | :--- | :--- |
| **Daniel Prado** *(Líder)* | Codex, Gemini (Argon y Gemini Notebook) y Antigravity | • Sugerencia de la función de trabajo $f(x)=x^2+1$ (Gemini Argon).<br>• Apoyo de Codex en estructuración de código de `src/matematica.py` e introducción conceptual (`src/escenas/introduccion.py`, `guion/introduccion_grabacion.md`).<br>• Asistencia en sintaxis de pruebas unitarias. | • Consulta y revisión personal exclusiva del apunte docente del curso (`docs/Apunte.pdf`).<br>• Cálculo manual independiente de las alturas y aportes de $L_4$ y $R_4$ sobre $P=\{0, 0.5, 1, 1.5, 2\}$.<br>• Ejecución manual de las 24 pruebas unitarias pasando al 100%.<br>• Revisión manual de la renderización del video y locución del Bloque 1. |
| **Sebastian Pereda** *(Sublíder)* | Codex, Antigravity (Google DeepMind) | • Asistencia en desarrollo de helpers gráficos Manim (`src/helpers_visuales.py`, `src/datos_rectangulos.py`).<br>• Depuración de escenas de construcción geométrica (`src/escenas/construcciones.py`).<br>• Pruebas unitarias de objetos visuales (`tests/test_helpers_visuales.py`, `tests/test_datos_rectangulos.py`).<br>• Estructuración del guion para las construcciones de $L_4$ y $R_4$. | • Consulta directa y cita formal del texto de James Stewart (*Cálculo*, 8.ª ed., Cap. 5, §§5.1–5.2).<br>• Validación de contraste cromático con la paleta Okabe-Ito (azul `#56B4E9` y naranja `#E69F00`) bajo estándar WCAG 2.1 ($\ge 3:1$).<br>• Inspección visual de renders aislados (duración exacta de 55.0 s por escena).<br>• Grabación y sincronización de voz propia para los Bloques 2 y 3. |
| **Rodrigo Pedraza** *(Integrante)* | Codex, Antigravity (Google DeepMind) | • Asistencia en lógica de diferencias locales y telescópicas (`src/comparacion.py`).<br>• Estructuración de pruebas comparativas (`tests/test_comparacion.py`).<br>• Escenas de comparación causal, detalle de intervalo y cierre con refinamiento (`src/escenas/comparacion.py`).<br>• Redacción de la guía de estudio (`docs/guia_estudio_rodrigo.md`) y guion de bloques 4 y 5. | • Consulta directa y cita formal de Daniel Kleitman / MIT OCW (*18.013A Calculus with Applications*, Cap. 20).<br>• Cálculo analítico a mano del intervalo testigo $[1, 1.5]$ (salto de altura $2 \to 3.25$, aporte $1.0 \to 1.625$, diferencia $+0.625$) y de la cancelación telescópica ($\Delta x [f(2)-f(0)] = 2.00$).<br>• Corrección de encuadres y saltos de línea de texto en los renders preliminares.<br>• Grabación y sincronización de voz propia para los Bloques 4 y 5. |
| **Equipo / Montaje e Integración** | `run.py`, Manim v0.22.0, FFmpeg, scripts asistidos por IA | • Pipeline de automatización para renderizado de escenas secuenciales y compilación de la ficha técnica \LaTeX{} (`entrega/MAT1188_EID_G02_2026.tex`). | • Revisión audiovisual cuadro a cuadro del video final `video/MAT1188_EID_G02_2026.mp4`.<br>• Certificación de duración real: 5 min 56.57 s (dentro del rango exigido de 4 a 6 minutos).<br>• Verificación de presencia de las tres voces reales con sus rótulos de identificación.<br>• Comprobación de inclusión legible de las tarjetas de créditos finales (fuentes, herramientas y declaración de IA). |

---

## 3. Comprobaciones Matemáticas Verificadas Manualmente por el Equipo

Los siguientes valores fueron calculados paso a paso a mano y contrastados contra el código:
1. **Partición fija:** $P = \{0,\, 0.5,\, 1,\, 1.5,\, 2\}$, con $n = 4$ y $\Delta x = 0.5$.
2. **Suma Izquierda ($L_4$):**
   $$L_4 = 0.5 \cdot [f(0) + f(0.5) + f(1) + f(1.5)] = 0.5 \cdot [1 + 1.25 + 2 + 3.25] = 0.5 \cdot 7.5 = 3.75$$
3. **Suma Derecha ($R_4$):**
   $$R_4 = 0.5 \cdot [f(0.5) + f(1) + f(1.5) + f(2)] = 0.5 \cdot [1.25 + 2 + 3.25 + 5] = 0.5 \cdot 11.5 = 5.75$$
4. **Propiedad telescópica de la diferencia:**
   $$R_4 - L_4 = \Delta x [f(2) - f(0)] = 0.5 \cdot (5 - 1) = 0.5 \cdot 4 = 2.00$$
5. **Intervalo testigo $[1, 1.5]$:**
   - Base idéntica: $\Delta x_3 = 1.5 - 1 = 0.5$.
   - Altura izquierda: $f(1) = 2 \implies$ Aporte izquierdo $= 0.5 \cdot 2 = 1.0$.
   - Altura derecha: $f(1.5) = 3.25 \implies$ Aporte derecho $= 0.5 \cdot 3.25 = 1.625$.
   - Diferencia en el subintervalo: $1.625 - 1.0 = +0.625$.
6. **Valor analítico de la Integral Definida:**
   $$\int_0^2 (x^2 + 1)\,dx = \left[ \frac{x^3}{3} + x \right]_0^2 = \left( \frac{8}{3} + 2 \right) - 0 = \frac{14}{3} \approx 4.6667$$
   Verificación del acotamiento monótono creciente: $L_4 = 3.75 < \frac{14}{3} \approx 4.67 < R_4 = 5.75$.
7. **Refinamientos sucesivos:**
   - Para $n = 8$ ($\Delta x = 0.25$): $L_8 = 4.1875$, $R_8 = 5.1875$, Diferencia $= 1.00$.
   - Para $n = 16$ ($\Delta x = 0.125$): $L_{16} \approx 4.4219$, $R_{16} \approx 4.9219$, Diferencia $= 0.50$.
   - Se comprueba que $\lim_{n \to \infty} (R_n - L_n) = 0$, convergiendo a $14/3$.

---

## 4. Fuentes Externas, Licencias y Medios

- **Librería de software:** Manim Community v0.22.0 (Licencia MIT).
- **Música e imágenes externas:** No se incorporaron audios, música de fondo comercial, imágenes prediseñadas ni material audiovisual externo. Todo el contenido gráfico fue renderizado mediante código Python con Manim.
- **Fuentes bibliográficas:** 
  - Apunte oficial MAT1188 (2026).
  - J. Stewart (2016), *Cálculo de una variable: Trascendentes tempranas* (8.ª ed.).
  - D. Kleitman / MIT OpenCourseWare (2005), *18.013A Calculus with Applications*.
- **Paleta de colores:** Paleta Okabe-Ito (2008), de dominio público para accesibilidad a personas con daltonismo.
