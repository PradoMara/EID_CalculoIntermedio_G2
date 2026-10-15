# Referencias Bibliográficas y Fuentes del Proyecto

**Evaluación Integrada de Desempeño (EID) — Cálculo Intermedio (MAT1188)**  
**Grupo 2:** Extremos izquierdos y extremos derechos en Sumas de Riemann  

---

## 1. Material del Curso
* **Equipo Docente MAT1188 (2026).**  
  *Introducción a la integral: Sumas de Riemann, particiones y paso al límite* (`docs/Apunte.pdf`).  
  Pontificia Universidad Católica de Chile / Universidad de procedencia. Secciones 2 a 6.

---

## 2. Fuentes Matemáticas Complementarias Independientes
El equipo consultó dos fuentes complementarias distintas y formalmente identificables:

1. **James Stewart (2016).**  
   *Cálculo de una variable: Trascendentes tempranas* (8.ª ed.). Cengage Learning.  
   Capítulo 5 (*Integrales*), Sección 5.1 (*Áreas y distancias*) y Sección 5.2 (*La integral definida*), pp. 364–385.  
   *Aporte específico:* Distinción formal entre $L_n$ y $R_n$, definición rigurosa de puntos muestra arbitrarios $x_i^*$ y demostración de que la partición determina exclusivamente las bases mientras la regla determina las alturas evaluadas. (Consultado por Sebastian Pereda).

2. **Daniel Kleitman / MIT OpenCourseWare (2005).**  
   *18.013A Calculus with Applications*, texto en línea del Massachusetts Institute of Technology.  
   Capítulo 20: Sección 20.2 (*Definición precisa y sumas*), Sección 20.3 (*Funciones integrables*) y Sección 20.5 (*Sumas especiales*).  
   Enlace web: [https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter20/section02.html](https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter20/section02.html).  
   *Aporte específico:* Propiedades de funciones continuas e integrabilidad de Riemann, coincidencia de sumas laterales con sumas superiores/inferiores para funciones crecientes y condición de norma de partición tendiendo a cero. (Consultado por Rodrigo Pedraza).

3. **Referencias complementarias de apoyo pedagógico:**  
   * Thomas, G. B., Weir, M. D. y Hass, J. (2015). *Cálculo: una variable* (13.ª ed.). Pearson Educación. Cap. 5.1 y 5.3.  
   * Larson, R. y Edwards, B. H. (2010). *Cálculo 1 de una variable* (9.ª ed.). McGraw-Hill. Cap. 4.2.

---

## 3. Herramientas de Animación y Software
* **Manim Community Developers (2024–2026).**  
  *Manim Community: A community-maintained Python library for creating mathematical animations* (v0.18+ / v0.21+).  
  Documentación oficial consultada en línea: [https://docs.manim.community/](https://docs.manim.community/).  
  *Módulos utilizados:*
  - `manim.mobject.graphing.coordinate_systems.Axes` (manejo de escalas fijas y método `coords_to_point` / `c2p`).
  - `manim.mobject.geometry.polygram.Polygon` (construcción de rectángulos cerrados sin distorsión).
  - `manim.mobject.geometry.line.DashedLine` (guías verticales de alturas evaluadas).
  - `manim.mobject.geometry.arc.Dot` (marcadores de puntos muestra en eje y curva).
  - `manim.animation.composition.LaggedStart` (aparición secuencial didáctica).

---

## 4. Estándares Visuales y Accesibilidad
* **Masataka Okabe & Kei Ito (2008).**  
  *Color Universal Design (CUD): How to make figures and presentations that are friendly to Colorblind people.*  
  Paleta Okabe-Ito utilizada para alto contraste y distinción frente al daltonismo: Azul cielo (`#56B4E9`) para la suma izquierda y Naranja (`#E69F00`) para la suma derecha.
* **W3C (2018).**  
  *Web Content Accessibility Guidelines (WCAG) 2.1.* Criterio 1.4.11 (Contraste no textual $\ge 3:1$ superado en todos los componentes visuales).
