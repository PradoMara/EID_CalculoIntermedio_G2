# Informe de Sebastian Pereda

**Fecha de actualización:** 14 de octubre de 2026  
**Rol:** Sublíder  
**Estado:** Avance de Fase 1 (Investigación, verificación matemática y diseño Manim)

---

## 1. Estado de Tareas Asignadas

| Tarea | Estado | Avance verificable | Pendiente / Próximo paso |
| :--- | :---: | :--- | :--- |
| **T-005: Fundamentos y ejemplo** | **Completada** | `investigacion/fundamentos_sebastian.md` y `guion/calculos.md`. Cálculos manuales verificados ($L_4=3{,}75$, $R_4=5{,}75$, dif$=2$, $\int=14/3$). Fuente complementaria: Stewart (2016). | Revisión cruzada con Rodrigo completada; valores 100% coincidentes. |
| **T-010: Investigación Manim** | **Completada** | `investigacion/manim_sebastian.md`. Sistema de coordenadas `Axes` ($u_x=4{,}5$, $u_y=1{,}1$), `c2p`, geometría de polígonos, marcadores, paleta Okabe-Ito y contrastes WCAG. | Implementar en `src/datos_rectangulos.py` y `src/escenas/construcciones.py`. |
| **T-006: Integración del guion** | En preparación | Respaldos numéricos y material visual listos. Recibido texto propuesto por Rodrigo para el guion. | Redactar `guion/guion.md` y `referencias.md` integrando las 3 secciones y reparto de voces. |
| **T-027: `preparar_datos_rectangulos`** | Pendiente | Diseño geométrico documentado en `investigacion/manim_sebastian.md`. | Requiere `src/matematica.py` de Daniel. |
| **T-028 a T-032: Helpers visuales** | Pendiente | Especificaciones de ejes, marcas, gráfica, rectángulos y marcadores documentadas. | Programar en `src/escenas/construcciones.py`. |
| **T-011 / T-033: Escenas Manim** | Pendiente | Lógica de animación secuencial por subintervalo diseñada. | Programar `ConstruccionIzquierda` y `ConstruccionDerecha`. |
| **T-012: Pruebas unitarias** | Pendiente | Casos de prueba previstos para geometrías y coordenadas. | Crear `tests/test_datos_rectangulos.py` y `tests/test_helpers_visuales.py`. |
| **T-013: Auditoría final** | Pendiente | Matriz de criterios V1–V8 y D1–D6 estudiada. | Ejecutar sobre video integrado y documentos finales. |
| **T-020: Grabación y defensa** | Pendiente | Guía de estudio y preguntas típicas dominadas. | Grabar locución de las sumas y entregar audio a Rodrigo; ensayo final. |

---

## 2. Coordinación y Revisión Cruzada con Rodrigo Pedraza (T-007)

* **Fuentes complementarias:**
  * Rodrigo utilizó MIT OpenCourseWare 18.013A (Daniel Kleitman, 2005).
  * Sebastián seleccionó y documentó como fuente independiente: **James Stewart (2016), *Cálculo de una variable: Trascendentes tempranas*, 8.ª ed., Cap. 5**.
  * Se satisface el requisito de dos fuentes matemáticas complementarias distintas para el grupo.
* **Consistencia matemática comprobada:**
  * Se revisó `investigacion/interpretacion_rodrigo.md`. Los valores de $L_4=3{,}75$, $R_4=5{,}75$, diferencia $2$, aportes en $[1, 1{,}5]$ ($1{,}0$ vs $1{,}625$) y la integral de referencia $14/3$ coinciden con exactitud matemática en ambos documentos.
* **Texto de Rodrigo para el guion:**
  * Se acusó recibo del texto propuesto por Rodrigo (sección causal y paso al límite). Se integrará formalmente en la redacción de `guion/guion.md` asignándole su locución correspondiente.
