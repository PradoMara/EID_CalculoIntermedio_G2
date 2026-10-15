# Cálculos de respaldo para el guion del video

**Autor:** Sebastian Pereda (Sublíder)  
**Fecha:** 10 de octubre de 2026 (consolidado al 14 de octubre de 2026)  
**Tema:** Extremos izquierdos vs. extremos derechos en Sumas de Riemann  
**Ejemplo:** $f(x) = x^2 + 1$ en $[0, 2]$, $n = 4$, $\Delta x = 0{,}5$, $P = \{0; 0{,}5; 1; 1{,}5; 2\}$.

---

## 1. Valores de $f(x) = x^2 + 1$ en los nodos

* $f(0) = 0^2 + 1 = 1$
* $f(0{,}5) = 0{,}25 + 1 = 1{,}25$
* $f(1) = 1 + 1 = 2$
* $f(1{,}5) = 2{,}25 + 1 = 3{,}25$
* $f(2) = 4 + 1 = 5$

---

## 2. Construcción izquierda ($L_4$)
* Subintervalo 1 $[0, 0{,}5]$: base $0{,}5$, muestra $0$, altura $f(0) = 1$, aporte $0{,}5 \times 1 = 0{,}5$.
* Subintervalo 2 $[0{,}5, 1]$: base $0{,}5$, muestra $0{,}5$, altura $f(0{,}5) = 1{,}25$, aporte $0{,}5 \times 1{,}25 = 0{,}625$.
* Subintervalo 3 $[1, 1{,}5]$: base $0{,}5$, muestra $1$, altura $f(1) = 2$, aporte $0{,}5 \times 2 = 1{,}0$.
* Subintervalo 4 $[1{,}5, 2]$: base $0{,}5$, muestra $1{,}5$, altura $f(1{,}5) = 3{,}25$, aporte $0{,}5 \times 3{,}25 = 1{,}625$.

**Total $L_4$:**
$$L_4 = 0{,}5 + 0{,}625 + 1{,}0 + 1{,}625 = 3{,}75$$
$$L_4 = 0{,}5 \cdot (1 + 1{,}25 + 2 + 3{,}25) = 0{,}5 \cdot 7{,}5 = 3{,}75$$

---

## 3. Construcción derecha ($R_4$)
* Subintervalo 1 $[0, 0{,}5]$: base $0{,}5$, muestra $0{,}5$, altura $f(0{,}5) = 1{,}25$, aporte $0{,}5 \times 1{,}25 = 0{,}625$.
* Subintervalo 2 $[0{,}5, 1]$: base $0{,}5$, muestra $1$, altura $f(1) = 2$, aporte $0{,}5 \times 2 = 1{,}0$.
* Subintervalo 3 $[1, 1{,}5]$: base $0{,}5$, muestra $1{,}5$, altura $f(1{,}5) = 3{,}25$, aporte $0{,}5 \times 3{,}25 = 1{,}625$.
* Subintervalo 4 $[1{,}5, 2]$: base $0{,}5$, muestra $2$, altura $f(2) = 5$, aporte $0{,}5 \times 5 = 2{,}5$.

**Total $R_4$:**
$$R_4 = 0{,}625 + 1{,}0 + 1{,}625 + 2{,}5 = 5{,}75$$
$$R_4 = 0{,}5 \cdot (1{,}25 + 2 + 3{,}25 + 5) = 0{,}5 \cdot 11{,}5 = 5{,}75$$

---

## 4. Tabla comparativa resumen para pantalla

| Subintervalo | Base $\Delta x$ | Muestra Izq. | Altura Izq. | Aporte Izq. | Muestra Der. | Altura Der. | Aporte Der. | Dif. Aporte |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $[0, 0{,}5]$ | $0{,}5$ | $0$ | $1$ | $0{,}5$ | $0{,}5$ | $1{,}25$ | $0{,}625$ | $+0{,}125$ |
| $[0{,}5, 1]$ | $0{,}5$ | $0{,}5$ | $1{,}25$ | $0{,}625$ | $1$ | $2$ | $1{,}0$ | $+0{,}375$ |
| $[1, 1{,}5]$ | $0{,}5$ | $1$ | $2$ | $1{,}0$ | $1{,}5$ | $3{,}25$ | $1{,}625$ | $+0{,}625$ |
| $[1{,}5, 2]$ | $0{,}5$ | $1{,}5$ | $3{,}25$ | $1{,}625$ | $2$ | $5$ | $2{,}5$ | $+0{,}875$ |
| **Total** | — | — | — | **$3{,}75$** | — | — | **$5{,}75$** | **$+2{,}0$** |

---

## 5. Notas didácticas para la locución de Sebastián
1. Enfatizar en el audio que las 4 bases son idénticas en ambas sumas ($\Delta x = 0{,}5$).
2. Tomar como caso explicativo el subintervalo $[1, 1{,}5]$: la base no se mueve de $[1, 1{,}5]$; lo que cambia es la altura, que sube de $2$ a $3{,}25$, aumentando el aporte de $1{,}0$ a $1{,}625$.
3. Explicar que la diferencia total $R_4 - L_4 = 2{,}0$ se comprueba con la fórmula telescópica: $\Delta x [f(b) - f(a)] = 0{,}5 \cdot (5 - 1) = 2{,}0$.
4. Valor de referencia de la integral exacta: $\int_0^2 (x^2 + 1) \, dx = \frac{14}{3} \approx 4{,}6667$, cumpliendo $3{,}75 < \frac{14}{3} < 5{,}75$.
