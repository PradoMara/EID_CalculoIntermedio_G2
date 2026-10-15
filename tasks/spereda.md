# Tareas de Sebastian Pereda

## [x] T-005 — Investigar fundamentos y verificar el ejemplo elegido
- Prioridad: alta: fija los datos antes de programar
- Detalles: Leer apunte y una fuente matemática complementaria identificable. Desarrollar cálculos manuales para el ejemplo confirmado: f(x)=x²+1, [0,2], n=4, Δx=0.5 y P={0,0.5,1,1.5,2}. La elección ya está aprobada por Daniel; documentar y comprobar los resultados, sin volver a solicitar su selección. Entregar: investigacion/fundamentos_sebastian.md y guion/calculos.md.
- Criterios de aceptación:
  - [x] Fuente realmente consultada con autor/institución, título, año disponible, enlace/sección y afirmaciones respaldadas.
  - [x] Definir función, intervalo, partición, n, anchos, muestra, altura y aporte.
  - [x] Ejemplo coincidente con README; cálculos y tabla completa verificables por Daniel/Rodrigo.
  - [x] Resultados esperados: L=3.75,R=5.75,diferencia=2 y referencia exacta 14/3 como verificación.
  - [x] Distinguir mismas bases de mismas alturas; no copiar apunte como único desarrollo.

## [x] T-010 — Investigar Manim y documentar la representación
- Prioridad: alta: previene errores de coordenadas y bases
- Detalles: Consultar documentación oficial de Manim Community, coordinar compatibilidad con versiones que fije Daniel. Explicar conversión de coordenadas y mantenimiento de bases. Proponer archivos visuales separados de datos matemáticos. Entregar: investigacion/manim_sebastian.md. Requiere: Ninguna para investigar; aplicar hallazgos a la versión real cuando T-001 se complete.
- Criterios de aceptación:
  - [x] Referencia oficial identificada y consultada; registrar qué se aplicará.
  - [x] Explicar ejes, escala, ubicación de muestra y rectángulo sobre [x_i-1,x_i].
  - [x] Distinguir coordenadas matemáticas y dimensiones de pantalla.
  - [x] Documentar etiquetas, colores accesibles y cómo se revisará el render.
  - [x] Código adaptado con procedencia; no afirmar que una API se probó antes de ejecutarla.

## [x] T-006 — Integrar guion, fuentes y reparto de voces
- Prioridad: alta: alinea matemáticas, escenas y audio
- Detalles: Integrar investigaciones de ambos, apunte y Manim; organizar secciones propuestas en docs/context/analisis.md. Daniel explica conceptos, Sebastian construcciones/cálculos, Rodrigo causa/interpretación/integral, ajustando equilibrio de voz. Entregar: guion/guion.md y referencias.md. Requiere: T-005 en spereda.md: ejemplo y fundamentos validados; T-007 en rpedraza.md: investigación de interpretación; T-010 en spereda.md: investigación Manim.
- Criterios de aceptación:
  - [x] Guion contiene narrador, escena, texto, tiempos y notas matemáticas; total incluye créditos.
  - [x] Incluye presentación, teoría, ejemplo, respuesta explícita y vínculo con integral.
  - [x] Cada persona tiene explicación matemática sustantiva.
  - [x] Referencias incluyen apunte + dos fuentes matemáticas complementarias distintas + Manim, con datos completos.
  - [x] Ejemplo central con partición fija; refinamiento delimitado como otra etapa; créditos legibles y compatibles con tiempo.
  - [x] Coordinar nombres concretos de escenas con T-011/T-015; actualizar guion tras revisión.

## [x] T-027 — Crear la función `preparar_datos_rectangulos(funcion, particion, criterio)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Consumir calcular_rectangulos y preparar los datos geométricos para Manim: base de izquierda a derecha y altura desde y=0. Mantener datos puros para pruebas sin render. Entregar: src/datos_rectangulos.py. Requiere: T-026 en dprado.md.
- Criterios de aceptación:
  - [x] Cuatro bases iguales entre ambas opciones; muestras y alturas provenientes del modelo.
  - [x] Cada dato conserva los seis campos matemáticos y define sus vértices, sin mover la base al punto muestra.
  - [x] No convertir unidades matemáticas en píxeles en esta función.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-028 — Crear la función `crear_ejes()`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Construir y devolver ejes Manim con rangos que incluyan x de 0 a 2 e y de 0 a 5; fijar una única escala para todas las escenas. Entregar: src/escenas/construcciones.py. Requiere: T-001 en dprado.md; T-010 en spereda.md.
- Criterios de aceptación:
  - [x] Etiquetar ejes y mantener margen visible para curva y rectángulos.
  - [x] Usar los mismos rangos y dimensiones en las dos sumas y la comparación.
  - [x] Render de revisión sin etiquetas recortadas; comprobar propiedades configuradas en pruebas.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-029 — Crear la función `crear_grafica(ejes, funcion)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Devolver la curva de la función sobre [0,2] y su etiqueta, usando los ejes recibidos. Entregar: src/escenas/construcciones.py. Requiere: T-028 en spereda.md; T-022 en dprado.md.
- Criterios de aceptación:
  - [x] Representar x²+1, desde (0,1) hasta (2,5).
  - [x] Etiqueta de función legible y ubicada sin ocultar la comparación.
  - [x] No crear otros ejes ni sustituir la función por números codificados.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-030 — Crear la función `crear_marcas_particion(ejes, particion)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Devolver marcas y etiquetas para cada límite de la partición usando coordenadas de los ejes. Entregar: src/escenas/construcciones.py. Requiere: T-028 en spereda.md; T-023 en dprado.md.
- Criterios de aceptación:
  - [x] Mostrar 0,0.5,1,1.5,2 en sus posiciones correctas.
  - [x] No duplicar marcas si los ejes ya etiquetan esos valores.
  - [x] Funcionar con los puntos de partición recibidos, sin requerir la suma completa.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-031 — Crear la función `crear_rectangulo(ejes, dato, color)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Convertir los vértices matemáticos de un registro visual en un rectángulo Manim mediante los ejes; devolverlo sin animar. Entregar: src/escenas/construcciones.py. Requiere: T-027 y T-028 en spereda.md.
- Criterios de aceptación:
  - [x] La base ocupa [izquierda,derecha] y la altura es dato.altura.
  - [x] Sobre [1,1.5], ambas opciones conservan la base y alcanzan y=2/y=3.25.
  - [x] Comprobar geometría en coordenadas matemáticas; revisar opacidad y contorno legibles.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-032 — Crear la función `crear_marcadores_muestra(ejes, dato)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Devolver marcador en (muestra,0), punto en (muestra,altura) y guía vertical que los conecte. Entregar: src/escenas/construcciones.py. Requiere: T-027 y T-028 en spereda.md.
- Criterios de aceptación:
  - [x] Muestra y altura proceden del registro recibido.
  - [x] Marcadores izquierdos y derechos coinciden con los extremos correctos.
  - [x] No desplazar la base del rectángulo ni tapar etiquetas.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-011 — Crear la escena `ConstruccionIzquierda.construct()`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Reutilizar helpers para mostrar gráfica, partición, cuatro muestras izquierdas y aparición progresiva de rectángulos; mostrar aportes y suma 3.75. Entregar: src/escenas/construcciones.py. Requiere: T-027 a T-032 en spereda.md; T-002 en dprado.md; T-006 en spereda.md.
- Criterios de aceptación:
  - [x] Criterio 'izquierda', misma función/partición del README.
  - [x] Narración puede seguir muestra ->altura ->aporte ->suma.
  - [x] Totales calculados con el modelo; escena renderiza correctamente y sin recortes.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-033 — Crear la escena `ConstruccionDerecha.construct()`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Reutilizar los mismos helpers y escala para construir rectángulos con muestras derechas; mostrar aportes y suma 5.75. Entregar: src/escenas/construcciones.py. Requiere: T-027 a T-032 en spereda.md; T-002 en dprado.md; T-006 en spereda.md.
- Criterios de aceptación:
  - [x] Criterio 'derecha'; conservar partición y bases utilizadas por la construcción izquierda.
  - [x] Muestras derechas y alturas correctas; total del modelo, no texto independiente.
  - [x] Render coherente con guion y comparación visual.
  - [x] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [x] T-012 — Escribir pruebas unitarias de construcción visual
- Prioridad: alta: evita desalinear bases y muestras
- Detalles: Crear tests/test_datos_rectangulos.py para preparar_datos_rectangulos. Agregar tests/test_helpers_visuales.py para ejes, gráfica, marcas, geometría de rectángulos y marcadores, sin renderizar el video completo en cada test. Ejecutar y corregir fallos; renderizar ambas escenas para comprobar funcionamiento y legibilidad. Entregar: Pruebas y evidencia en informes/spereda.md. Requiere: T-027 a T-033 y T-011 en spereda.md: helpers y ambas escenas.
- Criterios de aceptación:
  - [x] Número de rectángulos y límites/ancho de cada base correctos.
  - [x] Izquierda y derecha comparten bases; muestras distintas en los extremos correctos.
  - [x] Alturas/aportes coinciden con expectativas manuales del ejemplo aprobado.
  - [x] Casos que detecten desplazamiento de base o confusión entre coordenadas y altura.
  - [x] Pruebas ejecutadas con resultados registrados; revisión visual adicional documentada, sin confundirla con unitarias.

## [ ] T-013 — Auditar video y documentos contra rúbrica
- Prioridad: alta: detectar omisiones antes de entregar
- Detalles: Ver video completo y documentos, comprobar accesibilidad, correspondencia de valores/escenas, voces, fuentes e IA. Registrar errores con responsable; revalidar después de correcciones. Entregar: informes/revision_final.md. Requiere: T-017 en rpedraza.md: video ensamblado; T-008 en dprado.md: reproducción e integración.
- Criterios de aceptación:
  - [ ] Matriz V1–V8 y D1–D6 con evidencia ubicable y pendientes concretos.
  - [ ] Duración medida 4–6 minutos, tres voces identificadas, créditos legibles.
  - [ ] Respuesta central, misma partición y condiciones matemáticas explícitas.
  - [ ] Cálculos, código, guion y video coinciden; no se aprueba con fallos pendientes relevantes.
  - [ ] Revisión D1–D6 identifica preparación faltante; no sustituye los ensayos personales.

## [ ] T-020 — Grabar voz, subir resumen y ensayar defensa
- Prioridad: alta: participación y comprensión individual
- Detalles: Tras guion y render de revisión, grabar voz propia sobre las dos sumas. Mantener resumen desde cada avance; cerrar pruebas/investigación y ensayar todo el proyecto antes del 21. Entregar: recursos/audio/sebastian.*, informes/spereda.md y registro de ensayo. Requiere: T-006 en spereda.md: guion y referencias; T-012 en spereda.md: pruebas visuales de datos.
- Criterios de aceptación:
  - [ ] Audio sustantivo, claro, nombre identificado y sincronizable; entregar toma a Rodrigo.
  - [ ] Resumen breve: IDs, archivos/commit, qué hizo, resultados reales y pendientes.
  - [ ] Investigación enlazada y herramienta/finalidad/partes IA verificadas; entregar datos a Rodrigo.
  - [ ] Explicar módulos de Daniel/Rodrigo y contestar variación sin ayuda.
  - [ ] Ensayo como representante, dudas resueltas y reglas de defensa comprendidas.
