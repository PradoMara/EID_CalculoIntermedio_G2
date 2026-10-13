# Guía de estudio de Rodrigo: proyecto, integrales y código

Lee esta guía en orden. Los ejemplos son los del video: `f(x)=x²+1`, intervalo `[0,2]` y cuatro rectángulos. Puedes comprobar cada número con lápiz antes de ejecutar Python.

## 1. ¿Qué busca el proyecto?

La pregunta es: **¿por qué dos sumas sobre la misma partición pueden dar valores distintos?** El video muestra la gráfica, divide el intervalo en cuatro bases y compara qué ocurre al tomar la altura en el extremo izquierdo o derecho de cada base. Después muestra otra etapa: hacer las bases más angostas para conectar con la integral. La comparación principal mantiene la partición fija.

Los archivos se separan por responsabilidad:

| Archivo | Para qué sirve |
| --- | --- |
| `src/matematica.py` (Daniel, pendiente en esta revisión) | Define la función, crea/valida particiones, calcula cada rectángulo y suma los aportes. |
| `src/datos_rectangulos.py` (Sebastian, pendiente) | Prepara datos geométricos sin dibujar. |
| `src/comparacion.py` (Rodrigo) | Empareja las dos construcciones, calcula sus diferencias, extrae un intervalo y repite con distintas cantidades. |
| `src/escenas/construcciones.py` (Sebastian, pendiente) | Dibuja ejes, curva, marcas y rectángulos con Manim. |
| `src/escenas/comparacion.py` (Rodrigo) | Animaciones de detalle, comparación y cierre; falta comprobarlas con los módulos reales de sus compañeros. |
| `tests/test_comparacion.py` | Comprueba los números y los casos límite de Rodrigo. |

El flujo de datos previsto es `función + partición → rectángulos → sumas → comparación → escenas → video`. La matemática se calcula antes de dibujar; la pantalla solo representa esos resultados.

## 2. Vocabulario matemático mínimo

- **Función:** regla que asigna una altura a cada `x`. Aquí `f(1.5)=1.5²+1=3.25`.
- **Intervalo `[a,b]`:** tramo que estudiamos. Aquí empieza en 0 y termina en 2.
- **Partición `P`:** lista ordenada de límites. Aquí `P=[0,0.5,1,1.5,2]`; crea cuatro subintervalos.
- **`n`:** cantidad de subintervalos, no de puntos. Cinco límites producen cuatro intervalos.
- **Ancho `Δx_i`:** límite derecho menos izquierdo. En nuestro ejemplo todos valen `0.5`.
- **Punto muestra:** lugar de cada subintervalo donde se evalúa la función. Puede ser el extremo izquierdo, el derecho u otro punto.
- **Altura:** `f(punto muestra)`.
- **Aporte:** `altura × ancho`. Como nuestra función es positiva, coincide con el área del rectángulo.
- **Suma de Riemann:** suma de todos los aportes. Es una aproximación para una partición finita.

En general, para `a=x₀<x₁<...<xₙ=b`, el intervalo `i` va de `x_(i-1)` a `x_i`, tiene ancho `Δx_i=x_i-x_(i-1)` y aporta `f(x_i*)Δx_i`. La suma es `Σ f(x_i*)Δx_i`.

## 3. Cálculo completo a mano

Como `n=4`, cada ancho vale `(2-0)/4=0.5`. Los puntos son `0, 0.5, 1, 1.5, 2`.

| Base | Muestra izq. | Altura izq. | Aporte izq. | Muestra der. | Altura der. | Aporte der. | Cambio de aporte |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `[0,0.5]` | 0 | 1 | 0.5 | 0.5 | 1.25 | 0.625 | 0.125 |
| `[0.5,1]` | 0.5 | 1.25 | 0.625 | 1 | 2 | 1 | 0.375 |
| `[1,1.5]` | 1 | 2 | 1 | 1.5 | 3.25 | 1.625 | 0.625 |
| `[1.5,2]` | 1.5 | 3.25 | 1.625 | 2 | 5 | 2.5 | 0.875 |
| **Total** | | | **3.75** | | | **5.75** | **2** |

Por ejemplo, en `[1,1.5]` no se mueve la base. Izquierda: `f(1)×0.5=2×0.5=1`. Derecha: `f(1.5)×0.5=3.25×0.5=1.625`. Diferencia: `1.625-1=0.625`.

La suma derecha es mayor **en este ejemplo** porque `x²+1` crece entre 0 y 2. Para demostrarlo sin derivadas: si `0≤x<y≤2`, entonces `f(y)-f(x)=y²-x²=(y-x)(y+x)>0`. Para una función decreciente, la diferencia se invierte. Para una constante, ambas sumas coinciden. Para una función que sube y baja, algunos cambios pueden compensarse.

## 4. ¿Qué es la integral definida?

Una suma usa rectángulos de ancho finito y por eso suele aproximar el área. Al crear particiones cada vez más finas, cuyo **ancho máximo tiende a cero**, las sumas de una función continua en un intervalo cerrado se acercan a un mismo número: la integral definida `∫ₐᵇ f(x) dx`. `n→∞` describe un proceso de límite; jamás se ejecuta un bucle con infinitos rectángulos.

En nuestro caso `f` es continua y positiva. La integral es el área bajo su curva entre 0 y 2. Se puede comprobar exactamente con una **primitiva**: si `F'(x)=f(x)`, entonces `∫₀²f(x)dx=F(2)-F(0)`. Para `f(x)=x²+1`, `F(x)=x³/3+x` y el resultado es `8/3+2=14/3≈4.6667`.

La primitiva permite comprobar el resultado, pero la idea central del video es cómo la elección de muestras cambia una suma finita. Si `f` tomara valores negativos, la integral sería acumulación con signo; el área geométrica total requeriría tratar por separado las partes bajo el eje.

## 5. Refinamiento: qué queda fijo y qué cambia

En **cada fila** comparamos izquierda y derecha con una misma partición. **Entre filas** cambiamos `n` y, por tanto, la partición. La función y el intervalo siguen iguales.

| `n` | Ancho | Izquierda | Derecha | Derecha − izquierda |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 0.5 | 3.75 | 5.75 | 2 |
| 8 | 0.25 | 4.1875 | 5.1875 | 1 |
| 16 | 0.125 | 4.421875 | 4.921875 | 0.5 |

Con anchos iguales, `R_n-L_n=Δx[f(2)-f(0)]=(2/n)(5-1)=8/n`. Se debe a que los valores de los puntos interiores aparecen una vez en cada suma y se cancelan al restar. Esta fórmula especial no se usa para una partición no uniforme. Que las tres diferencias bajen ilustra la tendencia; la continuidad justifica el límite.

Si quieres comprobar la convergencia con álgebra, para esta función se obtiene `L_n=14/3−4/n+4/(3n²)` y `R_n=14/3+4/n+4/(3n²)`. Cuando `n` crece, los términos con `1/n` y `1/n²` tienden a cero. Ambas expresiones se acercan a `14/3`.

## 6. Cómo leer el código de Rodrigo

Abre `src/comparacion.py`. Contiene tres funciones sin dibujos:

1. `comparar_sumas(funcion, particion)` pide a Daniel los registros de rectángulos de ambos criterios. Primero comprueba que las listas tengan el mismo largo; luego compara los límites y el ancho de cada par. Después resta `aporte_derecho - aporte_izquierdo` y solicita los dos totales. El resultado es un diccionario con registros, totales y diferencias. El `zip` une pares por posición **solo después** de comprobar la cantidad.
2. `extraer_detalle_intervalo(comparacion, indice)` usa un índice que empieza en cero. Por eso `indice=2` corresponde al **tercer** intervalo, `[1,1.5]`. Rechaza índices inválidos y devuelve copias de los dos registros para que quien prepare la escena no cambie los datos originales por accidente.
3. `calcular_refinamientos(funcion, a, b, cantidades)` recorre, por ejemplo, `[4,8,16]`. Para cada `n` crea una partición uniforme y llama a `comparar_sumas`. Guarda una fila por `n`. No calcula la integral infinita: produce solo las filas solicitadas.

### Python necesario para entenderlo

- `def nombre(...):` define una función. Los parámetros son valores que recibe.
- `return` entrega el resultado al código que la llamó.
- Una **lista** como `[0,0.5,1]` mantiene el orden. Una lista de registros tiene un elemento por subintervalo.
- Un **diccionario** como `{"ancho": 0.5}` asocia una clave legible con un valor. `registro["ancho"]` consulta ese valor.
- `for n in cantidades:` repite el bloque una vez por cada `n`.
- `zip(lista_a, lista_b)` produce pares correspondientes; como corta en la lista más corta, antes verificamos que tengan igual longitud.
- `raise ValueError(...)` indica datos incompatibles. `IndexError` indica un índice fuera de rango.
- `type(n) is int` evita aceptar `True` como 1: en Python un booleano también se comporta como entero en muchos contextos.
- `.copy()` crea una copia superficial de un registro plano; basta aquí porque sus seis campos son números.
- `import` dentro de una función carga el módulo de Daniel al llamar la función. Esto permite probar la lógica de Rodrigo mientras se completa esa dependencia.

## 7. Ejecutar y estudiar las pruebas

Desde la raíz del repositorio, ejecuta:

```powershell
python -m unittest tests.test_comparacion -v
```

Las pruebas de Rodrigo comparan con números calculados a mano, prueban una función constante y otra decreciente, verifican el índice 2 y comprueban que se rechacen bases desalineadas. Mientras falte `src/matematica.py`, usan un pequeño **doble de prueba** con la misma interfaz acordada. La prueba de integración real aparece como `skipped` hasta que Daniel agregue el módulo. Cuando eso ocurra, vuelve a ejecutar toda la suite:

```powershell
python -m unittest discover -s tests -t . -v
```

Lee una prueba como “preparo datos → llamo la función → comparo con un resultado que ya conozco”. Una prueba aprobada del doble confirma la lógica de Rodrigo; no confirma todavía que todos los módulos reales encajen ni que las escenas se vean bien. El render de Manim se revisará por separado.

## 8. Manim y las escenas previstas

Manim convierte números matemáticos en objetos de pantalla. Los ejes definen la escala; `ejes.c2p(x,y)` convierte un punto matemático al lugar correspondiente de la pantalla. Un rectángulo sobre `[1,1.5]` siempre tiene esquinas horizontales `1` y `1.5`; mover la muestra cambia su altura, no su base. La gráfica debe conservar ejes y escala entre izquierda y derecha.

En `src/escenas/comparacion.py`, `DetalleIntervalo` toma el índice `2` y transforma un rectángulo azul en otro naranja sobre la misma base. `ComparacionSumas` transforma los cuatro rectángulos y muestra los totales calculados. `CierreIntegral` recorre las filas `n=4,8,16` y muestra la respuesta central. `_datos_y_ayudas()` carga las funciones de los compañeros al construir la escena; `_escenario()` reúne ejes, curva y marcas, y `_rectangulos()` convierte la lista de datos visuales en objetos de Manim. `self.play(...)` inicia cada animación y `self.wait(...)` deja tiempo para leer.

Se hizo un render de prueba usando dobles temporales de las interfaces de los compañeros. La verificación final del render con sus implementaciones reales sigue pendiente. Para ejecutarla, cuando estén ambos módulos, usa:

```powershell
python -m manim render -ql src/escenas/comparacion.py DetalleIntervalo ComparacionSumas CierreIntegral
```

## 9. Preguntas para practicar la defensa

1. ¿Por qué hay cinco puntos de partición y solo cuatro rectángulos?
2. ¿Qué se mantiene y qué cambia al pasar de extremos izquierdos a derechos?
3. Calcula sin mirar la tabla los dos aportes de `[1,1.5]`.
4. ¿Por qué `R₄-L₄=2`? ¿Sería siempre positivo?
5. ¿Qué ocurre con `f(x)=3`? ¿Y con `f(x)=5-x`?
6. ¿Qué cambia al pasar de `n=4` a `n=8`? ¿Se cambió la función?
7. ¿Por qué tres valores numéricos no son una prueba de convergencia?
8. ¿Qué significa `14/3` y por qué está entre 3.75 y 5.75 aquí?
9. ¿Dónde se calculan los números y dónde solo se dibujan?
10. Si cambias la función, ¿qué valores y qué afirmaciones debes volver a verificar?

## 10. Plan corto de estudio

**Primera sesión:** reconstruye la tabla sin código. **Segunda:** ejecuta y lee una función y una prueba a la vez. **Tercera:** explica en voz alta la diferencia entre comparación fija y refinamiento. **Cuarta:** cuando estén las escenas, detén el video en cada cambio y explica qué objeto matemático representa. Finalmente, pide a un compañero una variación sencilla y resuélvela con papel antes de editar código.
