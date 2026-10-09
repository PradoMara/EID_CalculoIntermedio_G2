# Tareas de Rodrigo Pedraza

## [ ] T-007 — Investigar interpretación y conexión con integral
- Prioridad: alta: justifica la respuesta central
- Detalles: Consultar segunda fuente matemática complementaria distinta de la de Sebastian; coordinar para no duplicarla. Investigar creciente/decreciente/constante, compensación, continuidad y refinamiento. Revisar cálculos de T-005 cuando estén disponibles. Entregar: investigacion/interpretacion_rodrigo.md. Requiere: Ninguna para investigar; revisar el ejemplo después de T-005 en spereda.md.
- Criterios de aceptación:
  - [ ] Fuente real identificada, datos y enlace/sección; conclusiones aplicadas al tema.
  - [ ] Explicar que muestras cambian alturas, aportes y posiblemente total.
  - [ ] No generalizar izquierda=inferior/derecha=superior a toda función.
  - [ ] Distinguir convergencia de ilustración numérica y no sustituir n por infinito.
  - [ ] Verificar ejemplo recibido y suministrar a Sebastian contenido para guion/fuentes.

## [ ] T-014 — Consolidar declaración de IA y recursos para créditos
- Prioridad: alta: documentación obligatoria de apoyos
- Detalles: Crear declaración inicial de IA del análisis y esta planificación; pedir datos de cada autor y actualizar durante desarrollo. Recibir referencias de Sebastian y registrar recursos externos/licencias para créditos. No declarar verificaciones futuras como hechas. Entregar: declaracion_ia.md y aportes de créditos entregados a Sebastian. Requiere: Ninguna para iniciar; cerrar con referencias T-006 y registros reales de los tres.
- Criterios de aceptación:
  - [ ] Herramienta, finalidad, partes apoyadas y revisión humana real por cada uso.
  - [ ] IA no figura como sustituto de las dos fuentes matemáticas.
  - [ ] Recursos adaptados con autor/procedencia y permisos aplicables.
  - [ ] Declaración y créditos actualizados antes de T-008/T-017; resumen posterior no es requisito para iniciar consolidación.
  - [ ] Datos localizables desde README y ficha; conversaciones completas no exigidas.

## [ ] T-034 — Crear la función `comparar_sumas(funcion, particion)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Construir los registros de ambos criterios sobre una misma partición; devolver totales, diferencia total y diferencias por aporte. Reutilizar calcular_rectangulos y suma_riemann. Entregar: src/comparacion.py. Requiere: T-026 y T-002 en dprado.md.
- Criterios de aceptación:
  - [ ] Devolver 3.75,5.75 y diferencia 2; diferencias por aporte [0.125,0.375,0.625,0.875].
  - [ ] Verificar correspondencia de cantidad y bases antes de emparejar registros; no truncar listas silenciosamente.
  - [ ] No concluir que la derecha siempre es mayor.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-035 — Crear la función `extraer_detalle_intervalo(comparacion, indice)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Recibir resultado de comparar_sumas y devolver el par de registros y su diferencia para un índice desde cero; rechazar índices fuera de rango. Entregar: src/comparacion.py. Requiere: T-034 en rpedraza.md.
- Criterios de aceptación:
  - [ ] Para índice 2, intervalo [1,1.5], ancho 0.5, alturas 2/3.25 y aportes 1/1.625.
  - [ ] Devolver diferencia de aporte 0.625 sin modificar datos recibidos.
  - [ ] No seleccionar el intervalo mediante alturas ni asumir que siempre hay cuatro registros.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-036 — Crear la función `calcular_refinamientos(funcion, a, b, cantidades)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Crear una partición uniforme para cada n y comparar ambas sumas; devolver tabla de n,ancho,totales y diferencia, manteniendo función/intervalo. Entregar: src/comparacion.py. Requiere: T-024 y T-002 en dprado.md; T-034 en rpedraza.md.
- Criterios de aceptación:
  - [ ] n=4: 0.5,3.75,5.75,2; n=8: 0.25,4.1875,5.1875,1.
  - [ ] n=16: 0.125,4.421875,4.921875,0.5.
  - [ ] Cada fila usa la misma partición para ambas opciones; validar cantidades como enteros positivos.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-015 — Crear la escena `DetalleIntervalo.construct()`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Animar sobre [1,1.5] el paso de muestra izquierda a derecha y transformar altura de 2 a 3.25 con base fija. Consumir extraer_detalle_intervalo y helpers visuales de Sebastian. Entregar: src/escenas/comparacion.py. Requiere: T-035 en rpedraza.md; T-028 a T-032 en spereda.md; T-006 en spereda.md.
- Criterios de aceptación:
  - [ ] Mostrar base 0.5 invariable, puntos muestra 1/1.5 y aportes 1/1.625.
  - [ ] La transformación conserva ambos límites horizontales del rectángulo.
  - [ ] Escena renderiza correctamente y explica la causa de la diferencia.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-037 — Crear la escena `ComparacionSumas.construct()`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Mostrar las dos construcciones con los mismos ejes/escala y sus totales; resaltar elementos fijos y cambio del punto muestra. Consumir comparar_sumas y helpers existentes. Entregar: src/escenas/comparacion.py. Requiere: T-034 en rpedraza.md; T-027 a T-032 en spereda.md; T-006 en spereda.md.
- Criterios de aceptación:
  - [ ] Mostrar L=3.75,R=5.75 y R-L=2 con datos calculados.
  - [ ] Función, intervalo, partición y bases visualmente iguales.
  - [ ] Explicar que la función crece en este intervalo; no presentar desigualdad como universal.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-038 — Crear la escena `CierreIntegral.construct()`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Mostrar respuesta central y un refinamiento breve con n=4,8,16 a partir de calcular_refinamientos; reutilizar ejes y rectángulos. Conectar con integral 14/3 sin convertir el cierre en lección de antiderivadas. Entregar: src/escenas/comparacion.py. Requiere: T-036 en rpedraza.md; T-027 a T-032 en spereda.md; T-007 y T-006 para explicación.
- Criterios de aceptación:
  - [ ] Respuesta explícita: cambia muestra, altura y aporte; misma partición puede producir distinta suma.
  - [ ] Al refinar, indicar que ahora cambia la partición y ambas sumas se acercan al mismo límite por continuidad.
  - [ ] Valores correctos, textos legibles, escena renderiza y cabe en tiempo previsto.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-016 — Escribir pruebas unitarias de comparación y secuencia
- Prioridad: alta: protege conclusiones y sincronización de datos
- Detalles: Crear tests/test_comparacion.py con casos separados para comparar_sumas, extraer_detalle_intervalo y calcular_refinamientos. Ejecutar y corregir errores; renderizar DetalleIntervalo, ComparacionSumas y CierreIntegral para asegurar que funcionan correctamente. Entregar: Pruebas y evidencia en informes/rpedraza.md. Requiere: T-034 a T-038 y T-015 en rpedraza.md: comparación, detalle, refinamiento y escenas.
- Criterios de aceptación:
  - [ ] Diferencia de totales y suma de diferencias de aportes coinciden con cálculo independiente.
  - [ ] Detalle conserva base mientras cambia altura; validar valores esperados.
  - [ ] Para f(x)=x²+1 en [0,2], refinamiento uniforme: n=8 ->4.1875/5.1875; n=16 ->4.421875/4.921875. La comparación principal sigue usando n=4.
  - [ ] Función constante da diferencia cero y decreciente invierte signo; no codificar derecha siempre mayor.
  - [ ] Registrar comando/resultados y fallos corregidos; revisar condiciones y legibilidad fuera de unitarias.

## [ ] T-017 — Integrar animaciones, voces y MP4 final
- Prioridad: alta: producto evaluado con 40%
- Detalles: Elegir y documentar herramienta de edición disponible sin agregar aplicación al proyecto. Recibir clips y audios, integrar nombres, narración, pausas y créditos. Producir primer ensamblado para el hito interno del 16 y corregir lo encontrado en auditoría. Entregar: entrega/MAT1188_EID_G02_2026.mp4 e informes/edicion.md. Requiere: T-012 en spereda.md: pruebas visuales de datos; T-016 en rpedraza.md: pruebas de comparación; T-018 en dprado.md: voz de Daniel; T-020 en spereda.md: voz, resumen y ensayo de Sebastian; T-014 en rpedraza.md: declaración IA y créditos; T-006 en spereda.md: guion y referencias. Requiere además el audio de Rodrigo producido en la fase de grabación de T-021; el ensayo posterior de T-021 no bloquea edición.
- Criterios de aceptación:
  - [ ] MP4 abre, dura 4–6 minutos incluyendo inicio/cierre/créditos.
  - [ ] Tres voces propias con contenido matemático e identificación.
  - [ ] Escenas coherentes con guion, matemáticas y partición fija; pausas suficientes.
  - [ ] Audio comprensible, sin recortes; expresiones/recursos/créditos legibles.
  - [ ] Procedimiento de edición, clips/tomas usados y duración medida registrados; entregar a T-013 para revisión y corregir hallazgos.

## [ ] T-021 — Grabar voz, subir resumen y ensayar defensa
- Prioridad: alta: participación y dominio individual
- Detalles: Fase A: tras T-006 y render T-015 grabar voz propia para T-017. Fase B: después de T-016 consolidar informe. Fase C: ensayar proyecto completo antes de defensa. Las fases no dependen de T-017 para comenzar. Entregar: recursos/audio/rodrigo.*, informes/rpedraza.md y registro de ensayo. Requiere: T-006 en spereda.md: guion y referencias; T-015 en rpedraza.md: comparación y cierre. T-016 para cerrar evidencia de pruebas, no para iniciar grabación.
- Criterios de aceptación:
  - [ ] Audio claro con explicación matemática sustantiva, nombre e interpretación correctos; entregar antes de ensamblado.
  - [ ] Resumen breve por ID, qué hizo, archivos/commit, resultados de pruebas, fuentes/IA y pendientes.
  - [ ] Verificaciones humanas reales y comprensión del código asistido por IA.
  - [ ] Conocer cálculo y construcciones de compañeros, justificar variación y condiciones.
  - [ ] Ensayo individual como representante y reglas de defensa comprendidas; no bloquear video esperando ensayo.
