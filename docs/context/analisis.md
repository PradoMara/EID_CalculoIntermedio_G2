# Análisis y plan de trabajo del EID — Grupo 2

Fecha del análisis: 9 de octubre de 2026. Asignatura: Cálculo Intermedio, MAT1188.

Este documento reúne los requisitos encontrados en el repositorio y propone cómo cumplirlos. **Los requisitos provienen de la pauta y la rúbrica; el ejemplo, el guion, la estructura de carpetas y la distribución técnica sugeridos aquí son propuestas de trabajo, todavía no acuerdos del grupo.** No acredita entregas en Blackboard ni reemplaza las instrucciones del equipo docente.

## 1. Archivos revisados y estado actual

| Archivo | Qué aporta |
| --- | --- |
| [Pauta del EID](docs/Evaluacion%20Integrada%20De%20Desempe%C3%B1o.pdf) | Organización, video, repositorio, fuentes, ética, defensa y entrega. Cuatro páginas. |
| [Rúbrica](docs/EID_calculo_intermedio%20(4).pdf) | Ocho criterios del video (40 pts) y cuatro de la defensa (70 pts, porcentaje de conservación). Dos páginas. |
| [Temas](docs/temas.pdf) | Tema del grupo 2, pregunta central y alcance específico, página 2. |
| [Apunte](docs/Apunte.pdf) | Base conceptual: partición, punto muestra, suma de Riemann e integral. Siete páginas. |
| [Código de ética del grupo](docs/MAT1188_ETICA_G02_2026.pdf) | Integrantes, coordinación, compromisos y calendario interno. Tres páginas. |
| [README](README.md) | Actualmente solo identifica el repositorio; falta completar la documentación exigida. |
| LICENSE y .gitignore | Archivos generales del repositorio; revisar su adecuación al incorporar código y recursos. |

En los archivos de trabajo revisados no hay todavía escenas Python, dependencias, guion, cálculos propios, audios, video ni ficha final. Los PDF existen localmente, pero `git status` muestra `docs/` como carpeta sin seguimiento: **su existencia local no demuestra que estén publicados en GitHub**. Tampoco se ha comprobado desde aquí que el repositorio sea público o que los documentos ya se hayan entregado.

### Integrantes identificados en el acuerdo

| Integrante | Usuario GitHub | Rol de coordinación registrado |
| --- | --- | --- |
| Daniel Prado | PradoMara | Líder |
| Sebastian Pereda | SPereda2005 | Sublíder |
| Rodrigo Pedraza | rpedrazav | Integrante |

El acuerdo describe las tres responsabilidades técnicas, pero **no asigna explícitamente una persona a cada una**. Hay que completar esa asignación. Todos deben comprender el proyecto completo y explicar matemáticas con su propia voz.

## 2. Qué debe demostrar el grupo 2

**Tema:** extremos izquierdos y extremos derechos.

**Pregunta central:** ¿Por qué dos sumas construidas sobre la misma partición pueden entregar valores distintos?

Debemos construir dos sumas de Riemann sobre **la misma función y exactamente la misma partición**, usando extremos izquierdos en una y derechos en la otra. El video debe conectar:

1. Elección del punto muestra.
2. Evaluación de la función en ese punto.
3. Altura del rectángulo.
4. Aporte de cada rectángulo y valor de la suma.

La idea que debe quedar explícita es: **tener las mismas bases no obliga a tener las mismas alturas. La partición determina los subintervalos, pero no determina por sí sola los puntos muestra.**

| Elemento | ¿Permanece fijo en la comparación principal? |
| --- | --- |
| Función y gráfica | Sí |
| Intervalo de trabajo | Sí |
| Puntos de la partición | Sí |
| Número de subintervalos | Sí |
| Anchos y bases de los rectángulos | Sí |
| Extremo elegido como punto muestra | No: izquierdo o derecho |
| Altura de cada rectángulo | Puede cambiar al evaluar en el otro extremo |
| Aportes y suma total | Pueden cambiar como consecuencia |

No basta con mostrar dos dibujos ni leer dos resultados. Hay que explicar la causa matemática de la diferencia. El refinamiento puede aparecer brevemente en el cierre para conectar con la integral, pero no debe desplazar la comparación con partición fija.

## 3. Requisitos obligatorios y entregables

### Video

- MP4 de **4 a 6 minutos**, incluyendo presentación, cierre y créditos.
- Presentar integrantes, tema y pregunta central.
- Explicar conceptos, símbolos y condiciones para compañeros que todavía no estudian técnicas de integración.
- Desarrollar un ejemplo propio distinto de los desarrollados en el apunte: datos, procedimiento, resultados e interpretación.
- Incorporar animaciones de **Manim Community** que expliquen el ejemplo y estén sincronizadas con la narración.
- Responder explícitamente la pregunta central y conectar el tema con la integral.
- Incluir fuentes y recursos externos en créditos legibles.
- Cada integrante debe intervenir con su **propia voz en una explicación matemática sustantiva**, identificado por nombre. Saludar o leer créditos no satisface este requisito.
- No es obligatorio aparecer en cámara.

### Repositorio público de GitHub

- README con curso, integrantes y cuentas, tema y pregunta central.
- Versiones efectivamente utilizadas de Python y Manim, dependencias y pasos para ejecutar cada escena.
- Archivos `.py` y recursos necesarios para reconstruir las escenas del video.
- Guion con notas y cálculos que respalden el ejemplo: la rúbrica lo considera evidencia y exige que la ficha permita localizarlo.
- Referencias y declaración de IA en el README o en archivos enlazados desde él.
- Código correspondiente al video; la ficha debe identificar el **SHA del commit final**. Cambiar esa versión después de entregarla requiere autorización docente.

### Ficha final PDF

Debe contener curso, integrantes, tema, pregunta central, duración real del video, enlace de GitHub, SHA final, referencias y declaración de IA. Puede remitir a los registros completos identificados en el repositorio.

### Código de ética PDF independiente

Debe estar entregado en la actividad específica de Blackboard, con identificación, fecha y aceptación firmada de todos. Debe cubrir roles, tareas, plazos, comunicación, compromisos mínimos, aviso de dificultades, incumplimientos reiterados, recuperación, escalamiento docente, autoría, fuentes, IA y preparación de la defensa.

Ya existe un PDF del grupo. Debemos verificar su entrega y aceptación, resolver la discrepancia de fechas y asignar responsables técnicos. El texto extraído incluye nombres en el espacio de firmas; **eso no permite certificar que la aceptación firmada sea válida para la docente**. No hay que volver a cargarlo si ya está entregado y vigente; cualquier actualización debe tener fecha y aceptación de los integrantes habilitados.

### Nombres de entrega para este grupo

Con MAT1188 identificado en el documento de temas y en el acuerdo:

- `MAT1188_EID_G02_2026.mp4`
- `MAT1188_EID_G02_2026.pdf`
- `MAT1188_ETICA_G02_2026.pdf`

El MP4 y la ficha se cargan por separado. Si el video excede el tamaño permitido, utilizar únicamente la alternativa autorizada en Blackboard.

## 4. Fechas y pendientes administrativos

| Hito | Fecha documentada | Acción |
| --- | --- | --- |
| Inscripción por Educa | 6 de octubre, 23:59, según pauta | Confirmar inscripción con curso, grupo, nombres, cuentas y tema. |
| Código de ética en Blackboard | 6 de octubre, 23:59, según pauta | Confirmar entrega y aceptación. |
| Ejemplo y guion | 10 de octubre, acuerdo interno | Terminar selección, cálculos y tiempos por escena. |
| Código funcional y reproducible | 14 de octubre, acuerdo interno | Tener escenas verificadas. |
| Audios y primer ensamblado | 16 de octubre, acuerdo interno | Grabar a los tres integrantes e integrar el video. |
| Entrega final | Domingo 18 de octubre, 23:59, según pauta | Enviar MP4 y ficha, comprobar permisos y archivos. |
| Defensa | Miércoles 21 de octubre, mediante inscripción | Confirmar horario y modalidad en Blackboard. |

**Discrepancia concreta:** el acuerdo del grupo indica el **7 de octubre** para ética e inscripción, mientras que la pauta dice **6 de octubre**. Al 9 de octubre ambas fechas ya pasaron. Revisar anuncios y comprobantes; no asumir que la fecha interna modificó la oficial. Si hubo una ampliación docente, conservar el antecedente. El calendario del curso y las reglas sobre atrasos o problemas técnicos se comunican por Blackboard.

## 5. Base matemática que debemos dominar

Para una partición

\[
P=\{x_0,x_1,\ldots,x_n\},\qquad a=x_0<x_1<\cdots<x_n=b,
\]

el subintervalo número \(i\) es \([x_{i-1},x_i]\), con ancho \(\Delta x_i=x_i-x_{i-1}\). Elegir un punto muestra \(x_i^*\) dentro de ese subintervalo permite formar

\[
S(P)=\sum_{i=1}^{n}f(x_i^*)\Delta x_i.
\]

En nuestro tema:

\[
L(P)=\sum_{i=1}^{n}f(x_{i-1})\Delta x_i,
\qquad
R(P)=\sum_{i=1}^{n}f(x_i)\Delta x_i.
\]

Para una partición uniforme, todos los anchos son iguales:

\[
\Delta x=\frac{b-a}{n},\qquad x_i=a+i\Delta x.
\]

La diferencia se explica término a término:

\[
R(P)-L(P)=\sum_{i=1}^{n}\bigl[f(x_i)-f(x_{i-1})\bigr]\Delta x_i.
\]

**Condiciones y límites de las afirmaciones:**

- Usaremos una función continua y no negativa para representar los aportes como áreas de rectángulos sobre el eje horizontal.
- Si la función es creciente, el extremo derecho da alturas mayores o iguales: la suma izquierda subestima el área y la derecha la sobreestima.
- Si es decreciente, se invierte la comparación.
- Para funciones no monótonas, izquierda no significa necesariamente suma inferior ni derecha suma superior.
- Dos elecciones diferentes **pueden** dar valores distintos; no necesariamente lo hacen. Una función constante produce sumas iguales. También puede haber compensaciones entre aportes.
- Con anchos iguales, la diferencia se simplifica por cancelación telescópica a \(R_n-L_n=\Delta x[f(b)-f(a)]\). No usar esa simplificación para una partición no uniforme.
- Para una función continua, al refinar particiones de modo que su ancho máximo tienda a cero, ambas sumas convergen a la misma integral. En particiones uniformes esto ocurre al hacer \(n\to\infty\). No se sustituye \(n\) por el número infinito.

## 6. Ejemplo principal propuesto y verificado

**Propuesta:** \(f(x)=x^2+1\), intervalo \([0,2]\), cuatro subintervalos iguales:

\[
P=\{0,0.5,1,1.5,2\},\qquad n=4,\qquad \Delta x=0.5.
\]

Es continua, positiva y creciente en este intervalo. Las cuatro bases tienen el mismo ancho y todas las alturas son visibles, incluyendo la primera. El apunte revisado presenta teoría y situaciones generales, pero no desarrolla este ejemplo numérico.

| Subintervalo | Muestra izquierda | Altura izquierda | Aporte izquierdo | Muestra derecha | Altura derecha | Aporte derecho |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [0, 0.5] | 0 | 1 | 0.5 | 0.5 | 1.25 | 0.625 |
| [0.5, 1] | 0.5 | 1.25 | 0.625 | 1 | 2 | 1 |
| [1, 1.5] | 1 | 2 | 1 | 1.5 | 3.25 | 1.625 |
| [1.5, 2] | 1.5 | 3.25 | 1.625 | 2 | 5 | 2.5 |
| **Total** | | | **3.75** | | | **5.75** |

\[
L_4=0.5(1+1.25+2+3.25)=3.75,
\]

\[
R_4=0.5(1.25+2+3.25+5)=5.75.
\]

La diferencia es \(R_4-L_4=2\), consistente con \(0.5[f(2)-f(0)]=0.5(5-1)=2\).

### Rectángulo que conviene explicar en detalle

En \([1,1.5]\), la base permanece en 0.5. La muestra izquierda es 1, la altura es \(f(1)=2\) y el aporte vale 1. Al elegir la muestra derecha 1.5, la altura pasa a \(f(1.5)=3.25\), y el aporte a 1.625. **La base no se desplaza: cambia la altura evaluada sobre ella.**

### Comprobación adicional para el equipo

El área exacta es

\[
\int_0^2(x^2+1)\,dx=\left[\frac{x^3}{3}+x\right]_0^2=\frac{14}{3}\approx4.6667,
\]

y cumple \(3.75<14/3<5.75\). Este cálculo con antiderivada sirve para verificar el ejemplo; no debe convertirse en el contenido principal del video ni exigir conocimientos de integración que la audiencia aún no tiene.

Para una breve conexión final, con la misma función e intervalo y particiones uniformes refinadas:

| n | Ancho | Suma izquierda | Suma derecha | Diferencia |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 0.5 | 3.75 | 5.75 | 2 |
| 8 | 0.25 | 4.1875 | 5.1875 | 1 |
| 16 | 0.125 | 4.421875 | 4.921875 | 0.5 |

Cada fila compara izquierda y derecha **sobre una misma partición**; entre filas sí cambia la partición. Explicitar esa distinción si se utiliza la tabla. Estos valores ilustran el acercamiento; la conclusión general se apoya en la continuidad y el límite.

## 7. Guion y escenas sugeridas: video de 5 minutos

| Tiempo | Contenido | Qué debe verse |
| --- | --- | --- |
| 0:00–0:20 | Integrantes, tema y pregunta central | Título y pregunta legible. |
| 0:20–1:00 | Función, intervalo, partición y punto muestra | Gráfica de \(x^2+1\), marcas 0, 0.5, 1, 1.5, 2 y ancho 0.5. |
| 1:00–1:50 | Construcción izquierda | Muestras izquierdas, alturas y aparición progresiva de cuatro rectángulos; suma 3.75. |
| 1:50–2:40 | Construcción derecha | Las mismas bases, muestras derechas y nuevas alturas; suma 5.75. |
| 2:40–3:45 | Comparación causal | Detalle del subintervalo [1, 1.5], base fija y transformación de altura; comparación de totales y diferencia 2. |
| 3:45–4:35 | Interpretación y respuesta central | Lista breve de elementos fijos y variable; subestimación y sobreestimación justificadas por crecimiento. |
| 4:35–4:50 | Conexión con la integral | Acercamiento de ambas aproximaciones al refinar, con mención explícita del cambio de partición. |
| 4:50–5:00 | Créditos | Fuentes, Manim y apoyos; ajustar tiempo si no resultan legibles. |

Distribución de voces propuesta: integrante A explica conceptos y construcción izquierda; B explica construcción derecha y cálculos; C interpreta la comparación, responde la pregunta y conecta con la integral. Asignar los nombres en el guion y mostrar el nombre de quien habla. Los tres deben tener contenido matemático sustantivo.

### Criterios de implementación visual

- Mantener el mismo encuadre, escala, gráfica y marcas de partición en las dos construcciones.
- Usar colores consistentes y etiquetas «izquierda» y «derecha»; no depender únicamente del color.
- Marcar cada muestra en el eje horizontal y su altura sobre la curva.
- Hacer que los rectángulos ocupen el subintervalo correspondiente, aunque la altura venga de uno de sus extremos.
- Mostrar la sustitución de valores antes del total, sin llenar la pantalla con toda la tabla.
- Si se usan dos paneles, deben tener escalas iguales. También puede usarse una transformación sobre los mismos ejes.
- No llamar «área exacta» a 3.75 ni a 5.75.
- Separar visualmente el cierre con refinamiento de la comparación principal.
- Verificar que pausas, narración, fórmulas y animaciones permitan seguir el razonamiento.

**Respuesta que el cierre debe expresar, con palabras propias:** las dos sumas pueden diferir porque en cada subintervalo se evalúa la misma función en puntos distintos. Las bases permanecen iguales, pero las alturas y los aportes pueden cambiar. En nuestro ejemplo creciente, las alturas derechas son mayores y la suma pasa de 3.75 a 5.75. Al refinar la partición, ambas aproximaciones convergen a la misma integral porque la función es continua.

## 8. Organización técnica propuesta

```text
README.md
analisis.md
requirements.txt
src/
  riemann_g02.py
guion/
  guion.md
  calculos.md
referencias.md
declaracion_ia.md
recursos/
  audio/
docs/
  [documentos actuales]
entrega/
  MAT1188_EID_G02_2026.mp4
  MAT1188_EID_G02_2026.pdf
```

Esta estructura es orientativa. Los archivos y carpetas propuestos todavía no existen, salvo los ya indicados en la revisión inicial. El código de ética puede mantenerse en `docs/`; su entrega en Blackboard es independiente.

### Trabajo técnico pendiente

1. Elegir el entorno de Python y Manim Community, instalar y registrar sus versiones reales. No inventar versiones en el README.
2. Declarar las dependencias Python y las herramientas externas que el flujo de renderizado necesite, incluida LaTeX si las escenas la requieren.
3. Centralizar función, intervalo, partición y criterios de muestra para evitar inconsistencias entre cálculos y escenas.
4. Implementar las escenas y documentar sus nombres y comandos reales de ejecución.
5. Probar primero una salida de revisión; corregir etiquetas, encuadres y alturas antes del render final.
6. Comprobar manualmente y con el cálculo utilizado por el código los cuatro aportes y ambos totales.
7. Grabar y editar las voces; verificar sincronización y duración total.
8. Probar la reconstrucción de las escenas siguiendo el README en un entorno limpio o por otro integrante.
9. Revisar `.gitignore` para excluir cachés, entornos y renders temporales, sin omitir recursos necesarios. Revisar las licencias y permisos de recursos externos.
10. Incorporar los archivos necesarios a GitHub, comprobar acceso público y fijar el commit que corresponde al video. Registrar su SHA completo en la ficha.

El repositorio debe reconstruir las escenas; conservar los audios y documentar la edición también ayuda a explicar cómo se obtuvo el MP4 final.

## 9. Fuentes y declaración de IA

Debemos consultar y registrar **el apunte base, al menos dos fuentes matemáticas complementarias de autoría identificable y la documentación oficial de Manim**. El apunte y la IA no sustituyen las dos fuentes adicionales.

El apunte orienta hacia Stewart, Thomas/Weir/Hass y Larson/Edwards. Podemos seleccionar dos fuentes de esa bibliografía u otras adecuadas. Antes de citarlas, hay que consultar efectivamente el contenido y registrar autor o institución, título, año disponible, enlace y sección pertinente. **Este análisis no acredita que ya se hayan consultado esas fuentes externas ni la documentación de Manim.**

Para cada fuente, registrar qué afirmación respalda: elección de muestras, fórmulas, comportamiento en funciones monótonas o convergencia. Identificar también código, música, imágenes u otros recursos adaptados, su procedencia y permisos aplicables.

Como este documento se preparó con ayuda de IA, debe registrarse ese uso si se incorpora al proyecto: herramienta Codex, finalidad de analizar requisitos y proponer organización y ejemplo, y partes apoyadas. Después se deben documentar las verificaciones humanas realmente realizadas: contraste con PDF, revisión de fórmulas, comprobación de valores, inspección de escenas y comprensión por los tres integrantes. No declarar revisiones como realizadas si todavía están pendientes. Ampliar la declaración si se usa IA para programación, guion u otras partes. No se requieren conversaciones completas.

## 10. Cómo cumplir la rúbrica (`docs/EID_calculo_intermedio (4).pdf`)

El video se evalúa sobre un máximo de **40 puntos** ($P_V$), obteniendo así una nota inicial ($N_V$). Durante la defensa oral (máximo **70 puntos**, $P_D$), el estudiante seleccionado al azar no repite una presentación del video, sino que responde las **cuatro preguntas** formuladas por la comisión (M1, M2, M3 y C1). El porcentaje de nota conservado es $C = (P_D + 30)\%$ (entre el $30\%$ y el $100\%$ de $N_V$), de modo que $N_f = N_V \times \frac{P_D + 30}{100}$. La defensa permite aclarar o corregir oralmente un error, pero **no modifica el puntaje ya asignado al video**.

| Video (40 pts) | Puntaje | Evidencia e indicadores observables que debemos asegurar |
| --- | :---: | --- |
| **V1. Fundamentos matemáticos** | **7 pts** | a) define el concepto central (1 pt); b) explica los símbolos $\sum, f(x_i^*), \Delta x_i$ (1 pt); c) indica condiciones de aplicación: continuidad, $f(x)\ge 0$, monotonía (1 pt); d) relaciona los conceptos (2 pts); e) presenta afirmaciones matemáticas correctas (2 pts). |
| **V2. Ejemplo y procedimiento** | **7 pts** | a) usa un ejemplo distinto al apunte (1 pt); b) define función, intervalo y datos (1 pt); c) desarrolla los pasos principales (2 pts); d) obtiene resultados correctos: $L_4=3.75, R_4=5.75$ (2 pts); e) explica los cálculos en el video (1 pt). |
| **V3. Interpretación y pregunta central** | **6 pts** | a) interpreta el resultado (1 pt); b) relaciona el ejemplo y la teoría (1 pt); c) responde la pregunta central (1 pt); d) justifica su respuesta en $[1, 1.5]$ y diferencia total $2$ (2 pts); e) conecta su conclusión con la integral $14/3$ al refinar (1 pt). |
| **V4. Visualización matemática con Manim** | **5 pts** | a) utiliza escenas pertinentes de Manim; b) representa bien funciones y objetos; c) usa ejes y etiquetas coherentes; d) anima cambios que facilitan la comprensión; e) coordina parámetros, cálculos y visualización. |
| **V5. Integración de explicación y animación** | **5 pts** | a) sincroniza narración y escenas; b) explica lo representado; c) ordena la exposición progresivamente; d) usa lenguaje comprensible; e) articula presentación, desarrollo y cierre. |
| **V6. Comunicación y participación en el video** | **5 pts** | a) cumple la duración total de 4 a 6 minutos; b) todos los integrantes explican matemáticas con su voz; c) identifica cada intervención por nombre; d) tiene audio comprensible; e) tiene expresiones y gráficos legibles. |
| **V7. Fuentes, recursos externos e IA** | **3 pts** | a) cita el apunte y dos fuentes matemáticas adicionales (1 pt); b) identifica Manim y recursos adaptados, con créditos localizables (1 pt); c) declara el uso o no uso de IA y su verificación (1 pt). |
| **V8. Entrega y documentación** | **2 pts** | a) entrega MP4 y ficha PDF identificados y accesibles (1 pt); b) facilita el repositorio con código del video, versión final y README (1 pt). |

| Defensa oral (70 pts) | Puntaje | Qué debe poder responder cualquiera de los tres |
| --- | :---: | --- |
| **M1. Comprensión del contenido matemático** | **20 pts** | Explica un concepto, relación o afirmación que utilizó en su video y lo vincula con el tema asignado. |
| **M2. Justificación del desarrollo** | **20 pts** | Explica por qué realizó un paso o eligió un procedimiento, y qué significado tiene en su ejemplo. |
| **M3. Interpretación matemática** | **10 pts** | Interpreta un resultado, gráfica o animación y lo relaciona con la explicación del proyecto. |
| **C1. Comprensión del código utilizado** | **20 pts** | Explica qué representa o modifica un fragmento o parámetro relevante del código y cómo afecta a la visualización (sin exigir memorizar sintaxis de Manim). |

Los documentos respaldan el video, pero no sustituyen explicaciones ausentes en él. La ética y el repositorio son requisitos; no constituyen una tercera ponderación. La cantidad de commits o la sofisticación audiovisual no dan bonificaciones por sí solas.

## 11. Preparación de la defensa

La defensa es obligatoria, dura **máximo 10 minutos por grupo** y se selecciona al azar a un integrante presente para responder las **cuatro preguntas** formuladas por el equipo evaluador (M1, M2, M3 y C1; no se debe repetir una presentación del video). Todos declaran conocer el proyecto completo. No se cambia de representante por dificultades al responder. Solo habla el seleccionado o quien reciba expresamente la palabra del evaluador para la pregunta indicada.

Cada integrante debe practicar estas preguntas sin ayuda:

1. ¿Qué distingue una partición de una elección de puntos muestra?
2. ¿Qué está fijo y qué cambia entre nuestras dos sumas?
3. ¿Por qué el ancho es 0.5 y hay cuatro rectángulos?
4. ¿Cómo se calcula el aporte sobre [1, 1.5] por cada extremo?
5. ¿Cómo obtenemos 3.75 y 5.75, y por qué difieren en 2?
6. ¿Por qué la suma derecha es mayor en este ejemplo? ¿Ocurre siempre?
7. ¿Qué pasa con una función constante o decreciente?
8. ¿Pueden coincidir las sumas de una función no constante? Sí: por ejemplo, en una partición uniforme con valores iguales en los extremos del intervalo, la diferencia telescópica es cero.
9. ¿Qué cambia al usar ocho subintervalos y qué se mantiene fijo?
10. ¿Por qué las dos sumas se acercan a la misma integral?
11. ¿Dónde se definen la función, la partición y el criterio de muestra en nuestro código?
12. ¿Qué respalda cada fuente, qué aportó cada persona y cómo se verificó la ayuda de IA?

Hacer al menos un ensayo por integrante como representante, incluyendo una variación sencilla del ejemplo, sin necesidad de renderizar otro video ni memorizar sintaxis.

### Reglas que hay que conocer

- Ausencia sin justificación aceptada: 1.0 individual en el EID. Llegar después del sorteo no habilita otro sorteo; retirarse sin autorización cuenta como ausencia.
- Responder, complementar o corregir sin autorización: descuento acumulable de 0.5 puntos sobre la nota final del grupo por intervención diferenciada, con piso 1.0.
- Ayuda encubierta, señas, mensajes, dispositivos o apuntes/IA no autorizados: 1.0 para el grupo completo, incluso si el intento no resulta.
- Solo pueden consultarse recursos expresamente habilitados por el evaluador.
- La falta de dominio afecta la nota de defensa según la rúbrica; no implica automáticamente 1.0 en todo el EID.

## 12. Responsabilidades y plan de ejecución

Asignar una persona principal por fila, manteniendo revisión cruzada y comprensión común:

| Responsabilidad | Resultado esperado | Fecha interna |
| --- | --- | --- |
| Matemática y explicación | Fuentes seleccionadas, ejemplo validado, cálculos y guion de 5 minutos | 10 de octubre |
| Visualización y código | Escenas coherentes con el guion, parámetros documentados y ejecución reproducible | 14 de octubre |
| Revisión e integración | Tres voces, edición, créditos, MP4 final y revisión de ficha | Primer ensamblado el 16; final antes del 18 |
| Los tres | Revisión completa, comprobación de entrega y ensayo de defensa | 17–20 de octubre |

Orden recomendado desde el 9 de octubre:

1. Confirmar inscripción, entrega de ética y fecha autorizada; asignar responsables técnicos.
2. Consultar fuentes adicionales y acordar el ejemplo. Si se cambia el propuesto, recalcular todo antes de animarlo.
3. Cerrar cálculos y guion el 10 de octubre; repartir voces y definir escenas.
4. Implementar y revisar las escenas entre el 11 y el 14; completar README y dependencias.
5. Grabar voces y ensamblar entre el 15 y el 16; comprobar la duración con créditos.
6. El 17, revisar video completo contra la rúbrica, verificar reproducción y corregir errores. Preparar la ficha.
7. Antes del límite del 18, publicar la versión final, registrar SHA y duración reales, comprobar permisos, cargar archivos y guardar comprobantes. Dejar margen para problemas técnicos.
8. El 19 y el 20, ensayar la defensa con los tres y confirmar horario de inscripción. El 21, asistir y cumplir el procedimiento.

Para participación, aplicar el acuerdo existente: aviso anticipado de dificultades; revisar ausencias a dos reuniones, falta de avances o más de 48 horas sin comunicación; acordar recuperación con plazo máximo de 48 horas; informar a la docente si persiste antes de la defensa con antecedentes verificables. El grupo no puede expulsar integrantes ni imponer sanciones académicas.

## 13. Lista final de verificación

### Matemática y video

- [ ] La comparación principal usa la misma función y exactamente la misma partición.
- [ ] Se explican punto muestra, altura, ancho, aporte y sumatoria.
- [ ] Los resultados coinciden entre guion, código, etiquetas y narración.
- [ ] Se explica qué permanece fijo y cómo cambiar la muestra afecta las alturas.
- [ ] La respuesta central aparece explícitamente en el cierre.
- [ ] La comparación por crecimiento se limita a las condiciones que la justifican.
- [ ] La conexión con la integral es correcta y distingue el refinamiento de la comparación fija.
- [ ] El video dura 4–6 minutos con presentación y créditos incluidos.
- [ ] Las tres voces tienen explicación matemática sustantiva e identificación.
- [ ] Audio, gráficos, fórmulas y créditos se entienden y son legibles.

### Documentación y entrega

- [ ] Inscripción y ética confirmadas; discrepancia del 6/7 de octubre resuelta con antecedente docente.
- [ ] Responsables técnicos asignados y aceptación del acuerdo comprobada.
- [ ] Apunte, dos fuentes matemáticas adicionales y documentación oficial de Manim consultados y registrados.
- [ ] Recursos adaptados e IA declarados, con verificaciones reales documentadas.
- [ ] Guion y cálculos localizables desde README/ficha.
- [ ] README completo, versiones reales y escenas reproducibles.
- [ ] Repositorio público accesible y archivos necesarios publicados.
- [ ] SHA final corresponde al código de las escenas utilizadas en el video.
- [ ] Ficha PDF completa con duración real, enlace y SHA.
- [ ] MP4 y PDF con nombres correctos, abiertos y revisados antes de cargar.
- [ ] Entrega final comprobada por todos y comprobantes conservados.

### Defensa

- [ ] Horario y modalidad confirmados en Blackboard.
- [ ] Cada integrante explica el proyecto completo y localiza sus parámetros en el código.
- [ ] Cada integrante reconstruye cálculos y justifica una variación sencilla.
- [ ] Cada integrante ha ensayado como representante.
- [ ] Todos conocen las reglas de asistencia, silencio y recursos autorizados.

## 14. Decisiones pendientes inmediatas

1. Confirmar qué consta efectivamente como inscrito y entregado.
2. Asignar los tres responsables técnicos; los roles de líder y sublíder no bastan para esa distribución.
3. Acordar el ejemplo propuesto o elegir otro con la misma función y partición en ambas sumas.
4. Seleccionar y consultar dos fuentes matemáticas adicionales y la documentación de Manim.
5. Definir entorno de ejecución, escenas, reparto de voces y herramienta de edición.

Con esas decisiones se puede pasar a cálculos y guion, luego a Manim, audio y edición, documentación final y preparación de la defensa.
x