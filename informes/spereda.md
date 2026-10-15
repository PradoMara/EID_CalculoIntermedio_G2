# Informe de Sebastian Pereda

**Fecha de actualización:** 14 de octubre de 2026  
**Rol:** Sublíder  
**Estado:** Fases 1, 2 y 3 completadas (Investigación, Guion y Construcción Visual en Python/Manim)

---

## 1. Estado de Tareas Asignadas

| Tarea | Estado | Avance verificable | Pendiente / Próximo paso |
| :--- | :---: | :--- | :--- |
| **T-005: Fundamentos y ejemplo** | **Completada** | `investigacion/fundamentos_sebastian.md` y `guion/calculos.md`. Cálculos manuales verificados ($L_4=3{,}75$, $R_4=5{,}75$, dif$=2$, $\int=14/3$). Fuente complementaria: Stewart (2016). | Revisión cruzada con Rodrigo completada; valores 100% coincidentes. |
| **T-010: Investigación Manim** | **Completada** | `investigacion/manim_sebastian.md`. Sistema de coordenadas `Axes` ($u_x=4{,}5$, $u_y=1{,}1$), `c2p`, geometría de polígonos, marcadores, paleta Okabe-Ito y contrastes WCAG. | Base de implementación para `construcciones.py`. |
| **T-006: Integración del guion** | **Completada** | `guion/guion.md` y `referencias.md`. Guion de 4 min 45 s con reparto equitativo de voces (Daniel, Sebastian, Rodrigo) e integración de todas las fuentes formales. | Coordinado con Rodrigo para la locución y edición final. |
| **T-027: `preparar_datos_rectangulos`** | **Completada** | `src/datos_rectangulos.py`. Procesa registros del modelo matemático y genera 4 vértices continuos en coordenadas matemáticas puras sin modificar las bases. | Verificado con pruebas unitarias en `tests/test_datos_rectangulos.py`. |
| **T-028 a T-032: Helpers visuales** | **Completada** | `src/escenas/construcciones.py`: `crear_ejes`, `crear_grafica`, `crear_marcas_particion`, `crear_rectangulo` y `crear_marcadores_muestra`. | Compatible con imports desacoplados y listo para render. |
| **T-011 / T-033: Escenas Manim** | **Completada** | `ConstruccionIzquierda` y `ConstruccionDerecha` en `src/escenas/construcciones.py`. Animan la aparición secuencial progresiva de rectángulos, aportes y totales ($L_4=3{,}75$ y $R_4=5{,}75$). | Listas para ensamblado en el video global. |
| **T-012: Pruebas unitarias** | **Completada** | `tests/test_datos_rectangulos.py` (4 tests pasando: bases, alturas, aportes y vértices) y `tests/test_helpers_visuales.py` (configuración de escala y geometrías). | Todo validado con `python -m unittest`. |
| **T-013: Auditoría final** | Pendiente | Matriz de criterios V1–V8 y D1–D6 estudiada. | Ejecutar sobre video integrado y documentos finales. |
| **T-020: Grabación y defensa** | En curso | Locución definida en `guion/guion.md` (bloques 2 y 3: $L_4$ y $R_4$). Guía de estudio dominada. | Grabar audio propio y entregar a Rodrigo. |

---

## 2. Pruebas Unitarias Ejecutadas y Resultados

Comando ejecutado:
```bash
python3 -m unittest tests.test_datos_rectangulos -v
```
Resultado: **4 pruebas ejecutadas, 4 exitosas (OK)**:
* `test_cantidad_y_bases_compartidas`: Confirma que ambas sumas tienen 4 rectángulos y comparten idénticas bases de ancho $0{,}5$.
* `test_muestras_y_alturas_ejemplo_oficial`: Confirma alturas izquierdas $[1{,}0, 1{,}25, 2{,}0, 3{,}25]$ y aportes $[0{,}5, 0{,}625, 1{,}0, 1{,}625]$; y alturas derechas $[1{,}25, 2{,}0, 3{,}25, 5{,}0]$ y aportes $[0{,}625, 1{,}0, 1{,}625, 2{,}5]$.
* `test_subintervalo_critico_1_a_1_5`: Confirma que la base se mantiene en $[1{,}0, 1{,}5]$ con ancho $0{,}5$, y que la altura sube de $2{,}0$ a $3{,}25$.
* `test_vertices_geometricos_no_trasladan_base`: Comprueba que los vértices formen un polígono cerrado continuo exacto sobre el eje horizontal.

Comando ejecutado:
```bash
python3 -m unittest tests.test_helpers_visuales -v
```
Resultado: **Configuración de escala y constantes verificadas con éxito (OK)**.
