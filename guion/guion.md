# Guion Técnico del Video: Extremos Izquierdos vs. Derechos en Sumas de Riemann

**Asignatura:** Cálculo Intermedio (MAT1188) — Grupo 2  
**Tema:** Extremos izquierdos y extremos derechos  
**Pregunta central:** ¿Por qué dos sumas construidas sobre la misma partición pueden entregar valores distintos?  
**Duración estimada:** 4 minutos 45 segundos (Rango exigido: 4 a 6 minutos)  
**Formato de video:** MP4 1080p, 16:9, Manim Community.  

---

## Reparto de Voces y Roles

| Integrante | Rol | Bloque temático principal |
| :--- | :--- | :--- |
| **Daniel Prado** | Líder | Introducción, marco teórico, conceptos de partición, subintervalos y planteamiento de la pregunta central. |
| **Sebastian Pereda** | Sublíder | Construcción geométrica del ejemplo oficial ($f(x)=x^2+1$), suma izquierda ($L_4=3{,}75$), suma derecha ($R_4=5{,}75$) y cálculos paso a paso. |
| **Rodrigo Pedraza** | Integrante | Análisis causal en $[1, 1{,}5]$, respuesta a la pregunta central, refinamiento hacia la integral ($\int_0^2 f = 14/3$) y créditos. |

---

## Estructura de Escenas y Locución

### Bloque 1: Presentación y Fundamentos Teóricos (0:00 – 1:05)
* **Narrador:** Daniel Prado *(rótulo visible en pantalla: «Narrador: Daniel Prado»)*  
* **Visual / Escena Manim:** Título de la presentación, integrantes, pregunta central legible, definición formal de partición $P=\{x_0, \dots, x_n\}$, subintervalos $[x_{i-1}, x_i]$, ancho $\Delta x_i = x_i - x_{i-1}$, condición $f(x) \ge 0$ continua en $[a, b]$ y fórmula general de la suma de Riemann $\sum_{i=1}^n f(x_i^*)\,\Delta x_i$ destacando sus símbolos.  
* **Audio / Locución:**  
  > *"Hola, soy Daniel Prado y junto a Sebastian Pereda y Rodrigo Pedraza somos el Grupo 2 de Cálculo Intermedio. En este video responderemos nuestra pregunta central: ¿Por qué dos sumas de Riemann construidas sobre exactamente la misma partición pueden entregar valores distintos?  
  > Para entenderlo, consideremos una función continua y no negativa, $f(x) \ge 0$, en un intervalo cerrado $[a, b]$. Una partición $P = \{x_0, x_1, \dots, x_n\}$ divide el intervalo en $n$ subintervalos $[x_{i-1}, x_i]$, cada uno con base o ancho $\Delta x_i = x_i - x_{i-1}$.  
  > En la suma de Riemann, $\sum_{i=1}^n f(x_i^*)\,\Delta x_i$, el símbolo $\Sigma$ suma el área de $n$ rectángulos, donde la base es $\Delta x_i$ y la altura es la función evaluada en un punto muestra $x_i^*$. La clave es que la partición fija las bases sobre el eje horizontal, pero no fija por sí sola las alturas: elegir el extremo izquierdo $x_{i-1}$ da la suma izquierda $L_n$, y elegir el extremo derecho $x_i$ da la suma derecha $R_n$."*

---

### Bloque 2: Construcción de la Suma Izquierda ($L_4$) (1:05 – 2:00)
* **Narrador:** Sebastian Pereda *(rótulo visible en pantalla: «Narrador: Sebastian Pereda»)*  
* **Visual / Escena Manim (`ConstruccionIzquierda`):** Ejes coordenados fijos ($x \in [0, 2]$, $y \in [0, 5]$), gráfica de $f(x)=x^2+1$ en blanco, marcas de partición en $\{0; 0{,}5; 1; 1{,}5; 2\}$. Aparición progresiva de los 4 rectángulos en azul cielo (`#56B4E9`) con sus muestras en los extremos izquierdos, alturas punteadas y cálculo explícito de aportes (`0.5 × altura`).  
* **Audio / Locución:**  
  > *"Soy Sebastian Pereda. Desarrollaremos nuestro ejemplo propio con la función continua, positiva y creciente $f(x) = x^2 + 1$ en el intervalo $[0, 2]$, dividida en $n = 4$ subintervalos iguales de ancho $\Delta x = (2 - 0)/4 = 0{,}5$, con la partición $P = \{0; 0{,}5; 1; 1{,}5; 2\}$.  
  > Construyamos primero la suma izquierda $L_4$, evaluando $f$ en el extremo izquierdo de cada base y multiplicando altura por ancho:  
  > En $[0, 0{,}5]$, muestra $0$: altura $f(0) = 0^2 + 1 = 1$, y aporte $0{,}5 \times 1 = 0{,}5$.  
  > En $[0{,}5, 1]$, muestra $0{,}5$: altura $f(0{,}5) = 1{,}25$, aporte $0{,}5 \times 1{,}25 = 0{,}625$.  
  > En $[1, 1{,}5]$, muestra $1$: altura $f(1) = 2$, aporte $0{,}5 \times 2 = 1$.  
  > Y en $[1{,}5, 2]$, muestra $1{,}5$: altura $f(1{,}5) = 3{,}25$, aporte $0{,}5 \times 3{,}25 = 1{,}625$.  
  > Al sumar los cuatro aportes rectangulares, obtenemos la suma izquierda $L_4 = 3{,}75$."*

---

### Bloque 3: Construcción de la Suma Derecha ($R_4$) (2:00 – 2:55)
* **Narrador:** Sebastian Pereda *(rótulo visible en pantalla: «Narrador: Sebastian Pereda»)*  
* **Visual / Escena Manim (`ConstruccionDerecha`):** Los mismos ejes, escala y marcas. Los 4 rectángulos se construyen ahora con muestras en los extremos derechos, representados en color naranja (`#E69F00`), mostrando las nuevas alturas y el cálculo de cada aporte.  
* **Audio / Locución:**  
  > *"Ahora, sobre exactamente la misma función, intervalo y conservando idénticas las cuatro bases de ancho $0{,}5$, construimos la suma por extremos derechos $R_4$, evaluando en el límite derecho de cada subintervalo:  
  > En $[0, 0{,}5]$, la muestra es $0{,}5$: altura $1{,}25$, y aporte $0{,}5 \times 1{,}25 = 0{,}625$.  
  > En $[0{,}5, 1]$, la muestra es $1$: altura $2$, aporte $0{,}5 \times 2 = 1$.  
  > En $[1, 1{,}5]$, la muestra es $1{,}5$: altura $3{,}25$, aporte $0{,}5 \times 3{,}25 = 1{,}625$.  
  > Y en $[1{,}5, 2]$, la muestra es $2$: altura $f(2) = 2^2 + 1 = 5$, aporte $0{,}5 \times 5 = 2{,}5$.  
  > Sumando estos cuatro aportes, la suma derecha es $R_4 = 5{,}75$. Aunque las bases fueron exactamente iguales, cambiar el punto muestra aumentó la suma en 2 unidades completas."*

---

### Bloque 4: Comparación Causal y Respuesta Central (2:55 – 3:55)
* **Narrador:** Rodrigo Pedraza *(rótulo visible en pantalla: «Narrador: Rodrigo Pedraza»)*  
* **Visual / Escena Manim (`DetalleIntervalo` y `ComparacionSumas`):** Primer plano en el subintervalo $[1, 1{,}5]$. Se resalta la base fija de $0{,}5$ y cómo la altura pasa de $2$ a $3{,}25$, elevando el aporte de $1{,}0$ a $1{,}625$ (diferencia $+0{,}625$). Luego vista comparativa con la diferencia total $R_4 - L_4 = 2$.  
* **Audio / Locución:**  
  > *"Soy Rodrigo Pedraza. Para justificar nuestra respuesta a la pregunta central, observemos en detalle el tercer subintervalo, $[1, 1{,}5]$.  
  > Al pasar de extremos izquierdos a derechos, la base no se desplaza: permanece fija entre $1$ y $1{,}5$ con ancho $0{,}5$. Sin embargo, cambiar el punto muestra de $1$ a $1{,}5$ evalúa la función en otro punto: la altura sube de $2$ a $3{,}25$ y el aporte aumenta de $1$ a $1{,}625$, sumando $0{,}625$ extra.  
  > En este ejemplo la suma derecha sobreestima y la izquierda subestima porque $f(x)=x^2+1$ es estrictamente creciente en $[0, 2]$; en una función decreciente ocurriría al revés, y en una constante ambas sumas serían iguales.  
  > Al sumar las diferencias de los cuatro tramos con ancho uniforme, los puntos interiores se cancelan telescópicamente: $R_4 - L_4 = \Delta x [f(2) - f(0)] = 0{,}5 \times (5 - 1) = 2$.  
  > Respondemos así la pregunta central: dos sumas sobre la misma partición pueden diferir porque la partición fija únicamente las bases, mientras que la elección del punto muestra determina las alturas evaluadas y sus aportes."*

---

### Bloque 5: Refinamiento, Integral y Cierre (3:55 – 4:45)
* **Narrador:** Rodrigo Pedraza *(rótulo visible en pantalla: «Narrador: Rodrigo Pedraza»)*  
* **Visual / Escena Manim (`CierreIntegral`):** Tabla de refinamiento con $n=4, 8, 16$. Se muestra cómo al estrechar las bases las áreas escalonadas convergen al valor exacto de la integral $\frac{14}{3} \approx 4{,}67$. Pantalla final con las dos tarjetas de créditos completas (fuentes y verificación de IA).  
* **Audio / Locución:**  
  > *"Finalmente, ¿cómo se conecta esto con la integral definida? Si refinamos la partición aumentando $n$ de 4 a 8 y a 16 subintervalos, ahora sí cambiamos la partición entre etapas, haciendo que el ancho $\Delta x$ tienda a cero.  
  > Con ello, la suma izquierda sube de $3{,}75$ a $4{,}42$, la derecha baja de $5{,}75$ a $4{,}92$, y la diferencia se reduce de $2$ a $0{,}5$. Como $f(x)=x^2+1$ es continua en $[0, 2]$, al tender el ancho máximo a cero la discrepancia entre extremos desaparece y ambas aproximaciones convergen al mismo límite: el área exacta bajo la curva, dada por la integral definida $\int_0^2 (x^2+1)\,dx = 14/3 \approx 4{,}67$."*

---

## Resumen de Tiempos y Cobertura

| Sección | Tiempo | Narrador | Minutos acumulados | Criterios Rúbrica (`EID_calculo_intermedio (4).pdf`) |
| :--- | :---: | :---: | :---: | :---: |
| Conceptos teóricos y pregunta | 65 s | Daniel Prado | 0:00 – 1:05 | V1 (7 pts), V5, V6 |
| Construcción izquierda ($L_4$) | 55 s | Sebastian Pereda | 1:05 – 2:00 | V2 (7 pts), V4, V5, V6 |
| Construcción derecha ($R_4$) | 55 s | Sebastian Pereda | 2:00 – 2:55 | V2 (7 pts), V4, V5, V6 |
| Comparación causal $[1, 1{,}5]$ | 60 s | Rodrigo Pedraza | 2:55 – 3:55 | V1.c/e, V3.a–d (5 pts), V4, V5, V6 |
| Refinamiento, integral y créditos | 50 s | Rodrigo Pedraza | 3:55 – 4:45 | V3.e (1 pt), V6, V7 (3 pts) |
| **Total video** | **285 s** | **Equilibrio 3 voces** | **4 min 45 s** | **Total Video: 40 / 40 pts** |


## Ajuste técnico de las construcciones y créditos — 18 de octubre de 2026

Cada construcción dura 55 segundos sin audio: 0–7 s presentación de ejes y criterio; 7–17, 17–27, 27–37 y 37–47 s, un subintervalo por bloque. En cada bloque aparecen muestra (3 s), altura (3 s) y rectángulo con aporte (4 s). De 47–55 s aparece y permanece el total calculado a partir de los aportes. El panel derecho conserva los cuatro cálculos para leerlos juntos. Las pausas deben sincronizarse con la grabación de Sebastián; todavía no hay toma de voz validada.

Los archivos de revisión aislada utilizan datos de prueba explícitos. Las escenas de producción consumen el modelo real (`src/matematica.py`).

Créditos dentro del bloque final, sin ampliar los 285 segundos previstos (cumpliendo **V7.a, V7.b y V7.c**):
- 3:55–4:30: explicación del refinamiento y conclusión (35 s).
- 4:30–4:38: tarjeta 1 (8 s): «Grupo 2 · Cálculo Intermedio (MAT1188) / Daniel Prado · Sebastian Pereda · Rodrigo Pedraza / Animación: Manim Community 0.22.0 · Paleta accesible Okabe-Ito».
- 4:38–4:45: tarjeta 2 (7 s): «Fuentes: Apunte del curso "Introducción a la integral" · Stewart, Cálculo 8.ª ed. (§§5.1–5.2) · Kleitman, MIT OCW 18.013A (cap. 20) / Uso de IA (Codex): apoyo en código y guion, verificado con cálculo manual, pruebas unitarias e inspección de renders (detalle en repositorio)».

Las tarjetas usarán texto blanco sobre negro, al menos 28 puntos en Manim y margen de 0.5 unidades; deben verificarse en el montaje final. Esta es una especificación editorial para el responsable del montaje, no una afirmación de que los créditos ya estén renderizados. La locución del cierre debe ensayarse para comprobar que cabe en los 35 segundos disponibles.



## Ejecución continua para ensayo — 18 de octubre de 2026

`python run.py` genera PresentacionGuion como un solo video, sin voz grabada.
La introducción se divide en pregunta/presentación (0:00–0:15), partición
(0:15–0:40) y muestra/altura/aporte (0:40–1:05). Se reutilizan ambas
construcciones de 55 s. El bloque causal se divide en DetalleIntervalo
(2:55–3:25), ComparacionSumas (3:25–3:45) y respuesta con fórmula telescópica
(3:45–3:55). CierreIntegral ocupa 3:55–4:30 y las tarjetas de créditos
4:30–4:38 y 4:38–4:45.

La comparación cambia de izquierda a derecha en los mismos ejes; no es una
vista de dos gráficas simultáneas. Las animaciones de comparación y cierre
se ralentizan para acompañar la explicación. Los controles del reproductor
permiten pausar o volver atrás para estudiar. El reloj del video sirve como
referencia de ensayo; no certifica sincronización con una toma de voz.
