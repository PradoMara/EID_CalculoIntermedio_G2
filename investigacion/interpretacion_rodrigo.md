# T-007 — Interpretación de las dos sumas

**Autor del aporte:** Rodrigo Pedraza. **Fecha de preparación:** 13 de octubre de 2026.

## Fuentes consultadas

1. Apunte del curso, *Introducción a la integral*, secciones 2–6 (`docs/Apunte.pdf`): partición, punto muestra, suma de Riemann y paso al límite.
2. Daniel Kleitman / MIT OpenCourseWare, *18.013A Calculus with Applications*, texto en línea, capítulo 20, secciones [20.2, definición precisa y sumas](https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter20/section02.html), [20.3, funciones integrables](https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter20/section03.html) y [20.5, sumas especiales](https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter20/section05.html). Curso publicado por MIT OCW en 2005. Esta es mi fuente matemática complementaria propuesta; Sebastian debe escoger otra fuente distinta y registrar cuál usó.

MIT distingue explícitamente suma izquierda, derecha, superior e inferior. En una función creciente, derecha coincide con superior e izquierda con inferior; en una función decreciente ocurre al revés. También explica que una función continua es integrable y que para particiones generales debe tender a cero el **máximo ancho**, no basta contar muchos intervalos.

## Respuesta a nuestra pregunta

La partición fija las bases `[x_(i-1), x_i]` y sus anchos. Elegir el extremo izquierdo o derecho cambia el punto donde evaluamos `f`. Esa elección puede cambiar la altura `f(muestra)`, el aporte `altura × ancho` y finalmente la suma. No obliga a que los totales difieran: una función constante da la misma suma y los cambios positivos y negativos pueden compensarse.

Para cualquier partición:

`R(P) - L(P) = Σ [f(x_i) - f(x_(i-1))] × (x_i - x_(i-1))`.

Por eso el signo depende de la función en cada subintervalo. Si `f` crece, cada corchete es no negativo; si decrece, es no positivo. Para una función que sube y baja no hay una regla universal. Izquierda y derecha tampoco son siempre sinónimos de suma inferior y superior.

## Comprobación del ejemplo de este grupo

Con `f(x)=x²+1`, `[0,2]` y `P={0,0.5,1,1.5,2}`, la función crece porque para `0≤x<y≤2`, `y²-x²=(y-x)(y+x)>0`. Las alturas izquierdas son `1, 1.25, 2, 3.25` y las derechas `1.25, 2, 3.25, 5`. Los aportes respectivos son `0.5, 0.625, 1, 1.625` y `0.625, 1, 1.625, 2.5`. Por suma independiente: `L₄=3.75`, `R₄=5.75`, `R₄-L₄=2`. Las diferencias por intervalo son `0.125, 0.375, 0.625, 0.875`; suman `2`.

Sobre `[1,1.5]`, la base sigue siendo `0.5`. Izquierda: muestra `1`, altura `2`, aporte `1`. Derecha: muestra `1.5`, altura `3.25`, aporte `1.625`. La diferencia local es `0.625`.

Para anchos **iguales** `d`, los términos interiores se cancelan: `R_n-L_n=d[f(2)-f(0)] = (2/n)(5-1)=8/n`. Esta simplificación no vale sin más para particiones de anchos distintos.

## Refinamiento e integral

Al pasar de `n=4` a `8` y `16` se cambia la partición **entre filas**. Dentro de cada fila, izquierda y derecha usan la misma partición. Los pares de sumas son `3.75/5.75`, `4.1875/5.1875` y `4.421875/4.921875`. Las diferencias son `2`, `1` y `0.5`. Tres filas muestran una tendencia, pero no demuestran por sí solas una convergencia.

La justificación general es que `f` es continua en el intervalo cerrado. MIT 20.3 explica que su variación dentro de cada subintervalo puede hacerse pequeña cuando el máximo ancho tiende a cero. Así, cualquier elección de muestras llega a la misma integral. Para nuestras particiones uniformes `d=2/n→0` cuando `n→∞` (es un límite, no una sustitución de `n` por un número infinito).

La integral exacta se comprueba con la primitiva `F(x)=x³/3+x`: `F(2)-F(0)=14/3≈4.6667`. Es un valor entre las sumas izquierda y derecha del ejemplo porque aquí la función es creciente. La integral definida representa área geométrica porque `f≥0` en `[0,2]`; para valores negativos se interpreta como acumulación con signo.

## Material para el guion de Sebastian

Texto sugerido de Rodrigo: “Los cuatro intervalos y sus bases permanecen iguales. En cada uno movemos el punto muestra del extremo izquierdo al derecho. Como `x²+1` crece entre 0 y 2, sube la altura y aumenta el aporte. La suma pasa de 3.75 a 5.75. En otra función el signo puede cambiar. Cuando hacemos cada base más estrecha, ahora sí cambiamos la partición; las dos sumas se acercan a la integral `14/3` por continuidad.”

**Coordinación pendiente:** verificar el documento de cálculos de Sebastian cuando exista y comunicarle esta fuente y el párrafo para el guion. No se ha registrado todavía una revisión cruzada efectuada por Sebastian.
