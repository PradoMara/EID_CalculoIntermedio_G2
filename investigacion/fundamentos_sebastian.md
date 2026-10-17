# T-005 — Fundamentos y verificación del ejemplo: Extremos izquierdos vs. derechos en Sumas de Riemann

**Autor:** Sebastian Pereda (@seba / Sublíder)  
**Fecha:** 10 de octubre de 2026 (consolidado al 14 de octubre de 2026)  
**Curso:** Cálculo Intermedio (MAT1188) — Grupo 2  
**Pregunta central:** ¿Por qué dos sumas construidas sobre la misma partición pueden entregar valores distintos?

---

## 1. Marco conceptual

Dos sumas de Riemann sobre la misma partición difieren porque la partición fija solo las bases; la altura depende de dónde se evalúa $f$ dentro de cada subintervalo.

### Intervalo y partición
Sea $f$ una función definida en el intervalo cerrado $[a, b]$. Una partición es un conjunto finito de puntos:
$$P = \{x_0, x_1, \dots, x_n\}, \qquad a = x_0 < x_1 < \dots < x_n = b$$

### Subintervalos y bases
$P$ divide $[a, b]$ en $n$ subintervalos $[x_{i-1}, x_i]$, con $i = 1, \dots, n$. La base (ancho) de cada uno es:
$$\Delta x_i = x_i - x_{i-1}$$
Si la partición es regular (uniforme), $\Delta x = \frac{b - a}{n}$ para todo $i$.

### Punto muestra, altura y aporte
En cada subintervalo se elige un punto muestra $x_i^* \in [x_{i-1}, x_i]$.
* **Altura:** $f(x_i^*)$
* **Aporte (área del rectángulo):** $f(x_i^*) \cdot \Delta x_i$

### Suma de Riemann
$$S(P) = \sum_{i=1}^{n} f(x_i^*) \, \Delta x_i$$

### Las dos elecciones clásicas (fórmulas para partición regular)
* **Suma Izquierda ($L_n$):** Punto muestra en el extremo izquierdo $x_i^* = x_{i-1}$.
  $$L_n = \Delta x \sum_{i=1}^{n} f(x_{i-1}), \quad i = 1, \dots, n$$
* **Suma Derecha ($R_n$):** Punto muestra en el extremo derecho $x_i^* = x_i$.
  $$R_n = \Delta x \sum_{i=1}^{n} f(x_i), \quad i = 1, \dots, n$$

### Principio clave
> **La partición $P$ solo fija las bases $\Delta x_i$.**  
> La altura la fija otra decisión: dónde se evalúa $f$ dentro de cada subintervalo. Dos sumas pueden compartir exactamente las mismas bases y evaluar $f$ en puntos distintos. Si los valores evaluados en ambos extremos son distintos, los aportes de ese tramo difieren. Una función no constante puede tener extremos iguales: por ejemplo, $f(x)=(x-1)^2$ en $[0,2]$. Además, diferencias locales pueden cancelarse al sumar. En nuestro ejemplo, la función es estrictamente creciente y todos los aportes derechos son mayores. Las bases se conservan.

---

## 2. Ejemplo oficial: $f(x) = x^2 + 1$ en $[0, 2]$, $n = 4$

Para $f(x) = x^2 + 1$ en $[0, 2]$ con $n = 4$, $L_4 = 3{,}75$ y $R_4 = 5{,}75$; difieren en $2$ y la integral exacta, $\frac{14}{3} \approx 4{,}6667$, queda entre ambas.

* **Datos:** $\Delta x = \frac{2 - 0}{4} = 0{,}5$ y $P = \{0; 0{,}5; 1; 1{,}5; 2\}$.
* **Valores de $f$ en los nodos (calculados y reutilizados):**
  * $f(0) = 0^2 + 1 = 1$
  * $f(0{,}5) = 0{,}25 + 1 = 1{,}25$
  * $f(1) = 1 + 1 = 2$
  * $f(1{,}5) = 2{,}25 + 1 = 3{,}25$
  * $f(2) = 4 + 1 = 5$

### Suma izquierda ($x_i^* = x_{i-1}$)
| $i$ | $[x_{i-1}, x_i]$ | Base $\Delta x$ | Punto muestra | Altura $f(x_i^*)$ | Aporte |
| :-: | :---: | :-: | :-: | :-: | :---: |
| 1 | $[0, 0{,}5]$ | $0{,}5$ | $0$ | $1$ | $0{,}5 \times 1 = 0{,}5$ |
| 2 | $[0{,}5, 1]$ | $0{,}5$ | $0{,}5$ | $1{,}25$ | $0{,}5 \times 1{,}25 = 0{,}625$ |
| 3 | $[1, 1{,}5]$ | $0{,}5$ | $1$ | $2$ | $0{,}5 \times 2 = 1$ |
| 4 | $[1{,}5, 2]$ | $0{,}5$ | $1{,}5$ | $3{,}25$ | $0{,}5 \times 3{,}25 = 1{,}625$ |

$$L_4 = 0{,}5 + 0{,}625 + 1 + 1{,}625 = 3{,}75$$

### Suma derecha ($x_i^* = x_i$)
| $i$ | $[x_{i-1}, x_i]$ | Base $\Delta x$ | Punto muestra | Altura $f(x_i^*)$ | Aporte |
| :-: | :---: | :-: | :-: | :-: | :---: |
| 1 | $[0, 0{,}5]$ | $0{,}5$ | $0{,}5$ | $1{,}25$ | $0{,}5 \times 1{,}25 = 0{,}625$ |
| 2 | $[0{,}5, 1]$ | $0{,}5$ | $1$ | $2$ | $0{,}5 \times 2 = 1$ |
| 3 | $[1, 1{,}5]$ | $0{,}5$ | $1{,}5$ | $3{,}25$ | $0{,}5 \times 3{,}25 = 1{,}625$ |
| 4 | $[1{,}5, 2]$ | $0{,}5$ | $2$ | $5$ | $0{,}5 \times 5 = 2{,}5$ |

$$R_4 = 0{,}625 + 1 + 1{,}625 + 2{,}5 = 5{,}75$$

### Tabla comparativa conjunta
| $i$ | Subintervalo | $\Delta x$ | $f(x_{i-1})$ | $f(x_i)$ | Aporte izq. | Aporte der. | Diferencia |
| :-: | :---: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | $[0, 0{,}5]$ | $0{,}5$ | $1$ | $1{,}25$ | $0{,}5$ | $0{,}625$ | $0{,}125$ |
| 2 | $[0{,}5, 1]$ | $0{,}5$ | $1{,}25$ | $2$ | $0{,}625$ | $1$ | $0{,}375$ |
| 3 | $[1, 1{,}5]$ | $0{,}5$ | $2$ | $3{,}25$ | $1$ | $1{,}625$ | $0{,}625$ |
| 4 | $[1{,}5, 2]$ | $0{,}5$ | $3{,}25$ | $5$ | $1{,}625$ | $2{,}5$ | $0{,}875$ |
| **Total** | — | — | — | — | **$L_4 = 3{,}75$** | **$R_4 = 5{,}75$** | **$2$** |

Las diferencias suman: $0{,}125 + 0{,}375 + 0{,}625 + 0{,}875 = 2$, es decir, $R_4 - L_4 = 5{,}75 - 3{,}75 = 2$.

---

## 3. Análisis detallado del subintervalo $[1, 1{,}5]$

* La base es $\Delta x = 1{,}5 - 1 = 0{,}5$ en ambas sumas: **el ancho del rectángulo no cambia**.
* Con extremo izquierdo, la altura es $f(1) = 2$ y el rectángulo mide $0{,}5 \times 2 = 1$.
* Con extremo derecho, la altura es $f(1{,}5) = 3{,}25$ y el rectángulo mide $0{,}5 \times 3{,}25 = 1{,}625$.
* La diferencia local es $0{,}5 \times (3{,}25 - 2) = 0{,}625$, que corresponde exactamente al $\Delta x$ por el cambio de $f$ en ese tramo.
* **Conclusión visual:** Los dos rectángulos están sobre el mismo tramo del eje $x$ y solo difieren en la altura. La diferencia entre las sumas aparece porque $f$ evaluada en un extremo es distinta de $f$ evaluada en el otro.

---

## 4. Por qué $R_4 > L_4$: monotonía y suma telescópica

* **Monotonía:** $f'(x) = 2x \ge 0$ en $[0, 2]$, así que $f$ es creciente. En cada subintervalo, $f(x_{i-1}) \le f(x_i)$. Como $\Delta x > 0$, cada aporte derecho es mayor o igual que el izquierdo y, sumando, $R_n \ge L_n$. Aquí la desigualdad es estricta porque $f$ es estrictamente creciente en $[0, 2]$.
* **Fórmula telescópica:**
  $$R_n - L_n = \Delta x \sum_{i=1}^{n} \left[ f(x_i) - f(x_{i-1}) \right] = \Delta x \left[ f(x_n) - f(x_0) \right] = \Delta x \left[ f(b) - f(a) \right]$$
  Todos los términos intermedios se cancelan:
  $$\left(f(x_1) - f(x_0)\right) + \left(f(x_2) - f(x_1)\right) + \dots + \left(f(x_n) - f(x_{n-1})\right) = f(x_n) - f(x_0)$$
  *Verificación:* $0{,}5 \cdot [f(2) - f(0)] = 0{,}5 \cdot (5 - 1) = 2$ ✓.
* **Límite:** Como $\Delta x = \frac{b - a}{n}$, la diferencia es $\frac{(b - a)[f(b) - f(a)]}{n}$, que tiende a $0$ cuando $n \to \infty$. Por eso ambas sumas convergen al mismo valor: la integral.

---

## 5. Verificación exacta por antiderivada

Una antiderivada de $x^2 + 1$ es $F(x) = \frac{x^3}{3} + x$. Por el Teorema Fundamental del Cálculo:
$$\int_0^2 (x^2 + 1) \, dx = F(2) - F(0) = \left( \frac{8}{3} + 2 \right) - 0 = \frac{14}{3} \approx 4{,}6667$$

Entonces $3{,}75 < \frac{14}{3} < 5{,}75$, es decir, $L_4 < \int < R_4$. Para una función creciente, la suma izquierda subestima el área y la derecha la sobreestima. Los errores son:
* Error izquierda: $\frac{14}{3} - 3{,}75 \approx 0{,}9167$
* Error derecha: $5{,}75 - \frac{14}{3} \approx 1{,}0833$
* Suma de errores: $0{,}9167 + 1{,}0833 = 2$, exactamente igual que $R_4 - L_4$.

---

## 6. Fuentes bibliográficas consultadas

1. **Stewart, J. (2016).** *Cálculo de una variable: trascendentes tempranas* (8.ª ed.). Cengage Learning.  
   Capítulo 5, secciones 5.1 («Áreas y distancias») y 5.2 («La integral definida»): suma de Riemann con puntos muestra arbitrarios y sumas por extremo izquierdo y derecho.
2. **Thomas, G. B., Weir, M. D. y Hass, J. (2015).** *Cálculo: una variable* (13.ª ed.). Pearson Educación.  
   Capítulo 5, secciones 5.1 («Área y su estimación mediante sumas finitas») y 5.3 («La integral definida»).
3. **Larson, R. y Edwards, B. H. (2010).** *Cálculo 1 de una variable* (9.ª ed.). McGraw-Hill.  
   Capítulo 4, sección 4.2 («Área»): tratamiento de las sumas inferior y superior.

---

## 7. Guía de estudio para la defensa

* **Pregunta 1: «Si usaron la misma partición, ¿por qué las sumas son distintas?»**  
  *Respuesta:* «La partición solo determina las bases de los rectángulos. Las alturas dependen del punto muestra donde se evalúa $f$. Con el extremo izquierdo se evalúa en $x_{i-1}$ y con el derecho en $x_i$, y como $f$ es creciente esos valores son distintos. En $[1, 1{,}5]$, por ejemplo, la base es $0{,}5$ en ambos casos, pero la altura pasa de $f(1) = 2$ a $f(1{,}5) = 3{,}25$. Por eso $L_4 = 3{,}75$ y $R_4 = 5{,}75$.»
* **Pregunta 2: «¿Cómo sabían de antemano que $R_4$ sería mayor que $L_4$, y por cuánto?»**  
  *Respuesta:* «Porque $f(x) = x^2 + 1$ es estrictamente creciente en $[0, 2]$, ya que $f'(x) = 2x \ge 0$. Eso hace que $f(x_i) > f(x_{i-1})$ en cada subintervalo. Además, la diferencia se calcula exactamente: al restar las sumas queda una suma telescópica, $R_n - L_n = \Delta x [f(b) - f(a)] = 0{,}5 \cdot (5 - 1) = 2$. Solo importan los valores de $f$ en los extremos del intervalo.»
* **Pregunta 3: «¿Cuál de las dos sumas es la correcta? ¿Qué relación tienen con la integral?»**  
  *Respuesta:* «Ninguna es la correcta: son aproximaciones del área bajo la curva. La integral exacta es $\frac{14}{3} \approx 4{,}6667$ y se cumple $3{,}75 < \frac{14}{3} < 5{,}75$: la izquierda subestima y la derecha sobreestima porque $f$ es creciente. Al aumentar $n$, la diferencia $R_n - L_n = \frac{(b - a)[f(b) - f(a)]}{n}$ tiende a 0, así que ambas convergen a la integral. Esa convergencia es la definición de integrabilidad por Riemann.»
* **Preguntas de seguimiento posibles:**  
  * *¿Y si $f$ fuera decreciente?* Se invierten los roles: $L > \int > R$, y $R_n - L_n$ sería negativa.  
  * *¿Y si $f$ no fuera monótona?* No se puede asegurar cuál suma es mayor. La fórmula telescópica sigue valiendo, pero no determina el signo de cada aporte.  
  * *¿Qué pasa con el punto medio?* Suele aproximar mejor que los extremos porque los errores por exceso y por defecto se compensan dentro del subintervalo.
* **Consejo para la defensa:** Memoriza las cinco alturas ($1; 1{,}25; 2; 3{,}25; 5$) y los totales ($3{,}75; 5{,}75; 2; \frac{14}{3}$). Si te pierdes en el cálculo, vuelve al subintervalo $[1, 1{,}5]$, que resume toda la idea: misma base, distinta altura.
