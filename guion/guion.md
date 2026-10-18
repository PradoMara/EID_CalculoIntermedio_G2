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
* **Narrador:** Daniel Prado  
* **Visual / Escena Manim:** Título de la presentación, pregunta central legible, definición formal de partición $P=\{x_0, \dots, x_n\}$, subintervalos $[x_{i-1}, x_i]$ y ancho $\Delta x_i$.  
* **Audio / Locución:**  
  > *"Hola, somos el Grupo 2 de Cálculo Intermedio. En este video abordaremos una pregunta fundamental: ¿Por qué dos sumas de Riemann construidas sobre exactamente la misma partición pueden entregar valores distintos?  
  > Para responderlo, consideremos una función continua $f$ en un intervalo cerrado $[a, b]$. Una partición $P$ subdivide este intervalo en $n$ subintervalos de la forma $[x_{i-1}, x_i]$, donde cada uno tiene una base o ancho $\Delta x_i = x_i - x_{i-1}$.  
  > La clave está en que la partición define de manera fija las bases sobre el eje horizontal, pero no fija por sí sola las alturas. La altura depende de qué punto muestra $x_i^*$ elijamos dentro de cada subintervalo para evaluar la función: si elegimos el extremo izquierdo $x_{i-1}$, obtenemos la suma izquierda; si elegimos el extremo derecho $x_i$, obtenemos la suma derecha."*

---

### Bloque 2: Construcción de la Suma Izquierda ($L_4$) (1:05 – 2:00)
* **Narrador:** Sebastian Pereda  
* **Visual / Escena Manim (`ConstruccionIzquierda`):** Ejes coordenados fijos ($x \in [0, 2]$, $y \in [0, 5]$), gráfica de $f(x)=x^2+1$ en blanco, marcas de partición en $\{0; 0{,}5; 1; 1{,}5; 2\}$. Aparición progresiva de los 4 rectángulos en azul cielo (`#56B4E9`) con sus muestras en los extremos izquierdos, alturas punteadas y aportes numéricos.  
* **Audio / Locución:**  
  > *"Soy Sebastian Pereda. Analicemos nuestro ejemplo oficial con la función $f(x) = x^2 + 1$ en el intervalo $[0, 2]$, dividida en cuatro subintervalos iguales de ancho $\Delta x = 0{,}5$, con la partición $\{0; 0{,}5; 1; 1{,}5; 2\}$.  
  > Construyamos primero la suma por extremos izquierdos. En cada subintervalo, evaluamos la función en su límite izquierdo:  
  > En $[0, 0{,}5]$, evaluamos en 0: altura 1, aporte $0{,}5$.  
  > En $[0{,}5, 1]$, evaluamos en $0{,}5$: altura $1{,}25$, aporte $0{,}625$.  
  > En $[1, 1{,}5]$, evaluamos en 1: altura 2, aporte 1.  
  > Y en $[1{,}5, 2]$, evaluamos en $1{,}5$: altura $3{,}25$, aporte $1{,}625$.  
  > Sumando los cuatro rectángulos, obtenemos una suma izquierda $L_4$ de exactamente $3{,}75$."*

---

### Bloque 3: Construcción de la Suma Derecha ($R_4$) (2:00 – 2:55)
* **Narrador:** Sebastian Pereda  
* **Visual / Escena Manim (`ConstruccionDerecha`):** Los mismos ejes, escala y marcas. Los 4 rectángulos se construyen ahora con muestras en los extremos derechos, representados en color naranja (`#E69F00`), mostrando las nuevas alturas y aportes.  
* **Audio / Locución:**  
  > *"Ahora, sobre exactamente la misma gráfica y conservando idénticas las cuatro bases de ancho $0{,}5$, construimos la suma por extremos derechos. Evaluamos la función en el extremo derecho de cada subintervalo:  
  > En $[0, 0{,}5]$, la muestra es $0{,}5$: altura $1{,}25$, aporte $0{,}625$.  
  > En $[0{,}5, 1]$, la muestra es 1: altura 2, aporte 1.  
  > En $[1, 1{,}5]$, la muestra es $1{,}5$: altura $3{,}25$, aporte $1{,}625$.  
  > En $[1{,}5, 2]$, la muestra es 2: altura 5, aporte $2{,}5$.  
  > Al sumar estos aportes, la suma derecha $R_4$ resulta ser $5{,}75$. Las bases fueron idénticas, pero el resultado final aumentó en 2 unidades completas."*

---

### Bloque 4: Comparación Causal y Respuesta Central (2:55 – 3:55)
* **Narrador:** Rodrigo Pedraza  
* **Visual / Escena Manim (`DetalleIntervalo` y `ComparacionSumas`):** Primer plano en el subintervalo $[1, 1{,}5]$. Se resalta la base fija de $0{,}5$ y cómo la altura pasa de $2$ a $3{,}25$, elevando el aporte de $1{,}0$ a $1{,}625$. Luego comparación sucesiva sobre los mismos ejes, conservando la escala, con la diferencia $R_4 - L_4 = 2$.
* **Audio / Locución:**  
  > *"Soy Rodrigo Pedraza. Para responder a nuestra pregunta central, miremos con lupa el tercer subintervalo, entre 1 y $1{,}5$.  
  > Los cuatro intervalos y sus bases permanecen iguales. En cada uno movemos el punto muestra del extremo izquierdo al derecho. La base no se traslada en absoluto; sigue midiendo $0{,}5$. Pero como $f(x)=x^2+1$ es una función estrictamente creciente en este intervalo, evaluar en el extremo derecho produce una altura mayor: sube de 2 a $3{,}25$, y el aporte local pasa de 1 a $1{,}625$.  
  > Al sumar las diferencias de todos los tramos, los términos intermedios se cancelan en una suma telescópica: la diferencia total es $\Delta x [f(2) - f(0)] = 0{,}5 \times (5 - 1) = 2$.  
  > Por eso dos sumas sobre la misma partición pueden dar valores distintos: la partición fija las bases, pero la regla de selección fija las alturas evaluadas."*

---

### Bloque 5: Refinamiento, Integral y Cierre (3:55 – 4:45)
* **Narrador:** Rodrigo Pedraza  
* **Visual / Escena Manim (`CierreIntegral`):** Tabla de refinamiento con $n=4, 8, 16$. Se muestra cómo las áreas escalonadas se pegan a la curva y convergen al valor exacto de la integral $\frac{14}{3} \approx 4{,}6667$. Pantalla final con créditos completos y fuentes.  
* **Audio / Locución:**  
  > *"¿Qué ocurre si refinamos la partición? Al aumentar $n$ a 8 y luego a 16 subintervalos, ahora sí estamos cambiando la partición: las bases se hacen cada vez más estrechas ($\Delta x \to 0$).  
  > La suma izquierda sube hacia $4{,}42$ y la suma derecha baja hacia $4{,}92$. Como la función es continua, ambas aproximaciones quedan acotadas y convergen al mismo valor: el área exacta bajo la curva, dada por la integral definida $\int_0^2 (x^2+1)dx = 14/3$, aproximadamente $4{,}67$.  
  > Concluimos así que sobre una partición fija las sumas difieren por la elección de alturas, pero al llevar el ancho de las bases al límite cero, la discrepancia desaparece y ambas revelan la misma integral de Riemann."*

---

## Resumen de Tiempos y Cobertura

| Sección | Tiempo | Narrador | Minutos acumulados |
| :--- | :---: | :---: | :---: |
| Conceptos teóricos y pregunta | 65 s | Daniel Prado | 0:00 – 1:05 |
| Construcción izquierda ($L_4$) | 55 s | Sebastian Pereda | 1:05 – 2:00 |
| Construcción derecha ($R_4$) | 55 s | Sebastian Pereda | 2:00 – 2:55 |
| Comparación causal $[1, 1{,}5]$ | 60 s | Rodrigo Pedraza | 2:55 – 3:55 |
| Refinamiento, integral y créditos | 50 s | Rodrigo Pedraza | 3:55 – 4:45 |
| **Total video** | **285 s** | **Equilibrio 3 voces** | **4 min 45 s** |


## Ajuste técnico de las construcciones y créditos — 17 de octubre de 2026

Cada construcción dura 55 segundos sin audio: 0–7 s presentación de ejes y criterio; 7–17, 17–27, 27–37 y 37–47 s, un subintervalo por bloque. En cada bloque aparecen muestra (3 s), altura (3 s) y rectángulo con aporte (4 s). De 47–55 s aparece y permanece el total calculado a partir de los aportes. El panel derecho conserva los cuatro cálculos para leerlos juntos. Las pausas deben sincronizarse con la grabación de Sebastián; todavía no hay toma de voz validada.

Los archivos de revisión aislada utilizan datos de prueba explícitos. Las escenas de producción ya consumen el modelo real integrado de Daniel.

Créditos dentro del bloque final, sin ampliar los 285 segundos previstos:
- 3:55–4:30: explicación del refinamiento y conclusión (35 s).
- 4:30–4:38: tarjeta 1 (8 s): «Grupo 2 · Cálculo Intermedio / Daniel Prado · Sebastian Pereda · Rodrigo Pedraza / Animación: Manim Community 0.22.0».
- 4:38–4:45: tarjeta 2 (7 s): «Fuentes: Introducción a la integral (apunte del curso) / Stewart, Cálculo, 8.ª ed., §§5.1–5.2 / MIT OCW, 18.013A, cap. 20 / Referencias completas y uso de IA: repositorio del proyecto».

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
