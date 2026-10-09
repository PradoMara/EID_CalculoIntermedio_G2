# Tareas de Daniel Prado

## [ ] T-001 — Instalar dependencias y configurar el proyecto
- Prioridad: alta: habilita el código de los tres
- Detalles: Consultar documentación oficial, elegir versiones compatibles de Python/Manim y preparar entorno local, dependencias, configuración de render y ejecución de pruebas. Usar unittest de Python como opción inicial sin dependencia adicional; si el equipo necesita otra herramienta, documentarla. Crear estructura modular e instrucciones, revisar .gitignore. No incluir secretos ni el entorno virtual. Entregar: requirements.txt, configuración necesaria, paquetes src/tests, README inicial e investigacion/configuracion_daniel.md.
- Criterios de aceptación:
  - [ ] Versiones reales y herramientas externas necesarias registradas; comprobar LaTeX si se usa MathTex.
  - [ ] Instalación y render mínimo comprobados, errores y soluciones anotados.
  - [ ] Comando de pruebas definido y ejecutable; sin reportar una suite vacía como validación del producto.
  - [ ] README permite preparar otro equipo y explica las rutas de módulos; entorno/cachés no se suben.
  - [ ] Documento breve explica decisiones, documentación consultada y comandos reales.

## [ ] T-022 — Crear la función `funcion_ejemplo(x)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Devolver x²+1; definir los datos del ejemplo principal en una sola ubicación, sin importar Manim. Entregar: src/matematica.py. Requiere: T-001 en dprado.md.
- Criterios de aceptación:
  - [ ] f(0)=1, f(0.5)=1.25, f(1)=2, f(1.5)=3.25 y f(2)=5.
  - [ ] La función acepta valores numéricos del intervalo y tiene documentada su entrada/salida.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-023 — Crear la función `validar_particion(particion)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Comprobar una secuencia numérica finita de al menos dos puntos estrictamente crecientes; rechazar entradas inválidas con ValueError. Entregar: src/matematica.py. Requiere: T-001 en dprado.md.
- Criterios de aceptación:
  - [ ] Aceptar [0,0.5,1,1.5,2] y una partición no uniforme.
  - [ ] Rechazar secuencias vacías, un punto, duplicados, desorden, valores no numéricos, NaN e infinito.
  - [ ] No modificar la secuencia recibida.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-024 — Crear la función `crear_particion_uniforme(a, b, n)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Calcular n+1 límites entre a y b con ancho (b-a)/n; validar a<b, límites finitos y n entero positivo. Entregar: src/matematica.py. Requiere: T-023 en dprado.md.
- Criterios de aceptación:
  - [ ] Para (0,2,4), devolver [0,0.5,1,1.5,2], incluyendo ambos extremos.
  - [ ] Rechazar n=0, n negativo/no entero y límites inválidos.
  - [ ] Servir también para n=8 y n=16; no redondear puntos de forma que altere la partición.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-025 — Crear la función `seleccionar_muestra(izquierda, derecha, criterio)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Devolver el límite izquierdo o derecho según criterio 'izquierda' o 'derecha'; no evaluar la función ni dibujar. Entregar: src/matematica.py. Requiere: T-001 en dprado.md.
- Criterios de aceptación:
  - [ ] En [1,1.5], devolver 1 o 1.5 respectivamente.
  - [ ] Rechazar criterio desconocido e intervalo con izquierda>=derecha.
  - [ ] Documentar los dos valores admitidos para criterio.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-026 — Crear la función `calcular_rectangulos(funcion, particion, criterio)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Validar partición/criterio y devolver una lista de registros con izquierda, derecha, muestra, ancho, altura y aporte. Usar seleccionar_muestra; altura=funcion(muestra), aporte=altura*ancho. Entregar: src/matematica.py. Requiere: T-023 y T-025 en dprado.md; T-022 para el ejemplo.
- Criterios de aceptación:
  - [ ] Un registro por subintervalo, respetando el orden y anchos propios.
  - [ ] Izquierda: alturas [1,1.25,2,3.25], aportes [0.5,0.625,1,1.625].
  - [ ] Derecha: alturas [1.25,2,3.25,5], aportes [0.625,1,1.625,2.5].
  - [ ] No modificar la partición ni depender del render; documentar el formato compartido.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-002 — Crear la función `suma_riemann(funcion, particion, criterio)`
- Prioridad: alta: necesaria para construir y comprobar el ejemplo.
- Detalles: Sumar los aportes obtenidos con calcular_rectangulos y devolver el total numérico. Esta función completa el modelo matemático desglosado en T-022 a T-026. Entregar: src/matematica.py. Requiere: T-026 en dprado.md; T-005 en spereda.md como respaldo de cálculos.
- Criterios de aceptación:
  - [ ] Obtener 3.75 por izquierda y 5.75 por derecha para el ejemplo.
  - [ ] Funcionar con partición no uniforme usando cada ancho real.
  - [ ] No duplicar selección de muestras ni construcción de registros; propagar errores claros.
  - [ ] Asegurarse de que funcione correctamente y agregar los casos unitarios correspondientes a la tarea de pruebas del responsable.

## [ ] T-003 — Escribir pruebas unitarias del modelo matemático
- Prioridad: alta: evita propagar errores a las escenas
- Detalles: Crear tests/test_matematica.py con casos separados para funcion_ejemplo, validar_particion, crear_particion_uniforme, seleccionar_muestra, calcular_rectangulos y suma_riemann. Ejecutarlos y corregir errores para asegurar funcionamiento correcto. Entregar: Pruebas y evidencia en informes/dprado.md. Requiere: T-022 a T-026 y T-002 en dprado.md: funciones matemáticas y suma.
- Criterios de aceptación:
  - [ ] Validar aportes y totales del ejemplo acordado, no solo comparar dos funciones del mismo módulo.
  - [ ] Comprobar función constante, creciente y decreciente.
  - [ ] Comprobar una partición no uniforme: anchos por intervalo, sin aplicar fórmula telescópica uniforme.
  - [ ] Validar rechazos de entradas inválidas y ausencia de mutación.
  - [ ] Registrar comando, casos, resultados reales y commit verificado.

## [ ] T-004 — Verificar inscripción, ética y coordinación
- Prioridad: alta: plazos administrativos ya transcurridos
- Detalles: Comprobar Educa/Blackboard, discrepancia 6/7 octubre, aceptación del acuerdo, repositorio público y horario de defensa. Si hace falta consultar a la docente, Daniel lo gestiona; no asumir prórroga. Revisar asignación técnica con el grupo. Entregar: informes/administracion.md, con estado y referencias a comprobantes, sin publicar datos sensibles.
- Criterios de aceptación:
  - [ ] Distinguir confirmado, pendiente y discrepancias; no afirmar entregas sin evidencia.
  - [ ] Confirmar ética vigente y aceptación; cualquier actualización sigue la pauta.
  - [ ] Responsabilidades: Daniel entorno/cálculo, Sebastian fundamentos/construcción, Rodrigo comparación/integración; todos revisión y defensa.
  - [ ] Registrar horario/modalidad cuando se publiquen y límite final del 18 a las 23:59.
  - [ ] Coordinar propiedad temporal de archivos compartidos en main.

## [ ] T-008 — Verificar reproducción y completar README
- Prioridad: alta: exigencia de entrega y reproducibilidad
- Detalles: Completar README con curso, nombres/cuentas, tema, pregunta, versiones, dependencias, escenas, pruebas, ejecución y enlaces. Ejecutar suite de los tres y reconstruir escenas desde entorno limpio o reproducido por otro integrante. Entregar: README final e informes/reproduccion.md. Requiere: T-003 en dprado.md: pruebas de cálculo; T-012 en spereda.md: pruebas visuales de datos; T-016 en rpedraza.md: pruebas de comparación; T-006 en spereda.md: guion y referencias; T-014 en rpedraza.md: declaración IA y créditos.
- Criterios de aceptación:
  - [ ] Pruebas completas pasan con evidencia real; fallos se devuelven al responsable y se corrigen.
  - [ ] Todas las escenas se pueden reconstruir y se identifican por archivo/nombre.
  - [ ] Recursos necesarios están disponibles y rutas funcionan.
  - [ ] README enlaza cálculos, guion, fuentes, IA e informes individuales.
  - [ ] No declarar reproducibilidad basándose solo en que funciona en el equipo original.

## [ ] T-018 — Grabar explicación matemática de Daniel
- Prioridad: alta: participación de los tres obligatoria
- Detalles: Grabar la sección asignada en el guion, por ejemplo partición, ancho y muestras. Revisar contenido y ruido; entregar audio al integrador. Entregar: recursos/audio/daniel.* e identificación en guion. Requiere: T-006 en spereda.md: guion y referencias; T-002 en dprado.md: módulo matemático e interfaz; T-011 en spereda.md: construcción visual.
- Criterios de aceptación:
  - [ ] Voz propia y nombre identificable; explicación sustantiva, no solo presentación.
  - [ ] Contenido correcto y comprensible, coordinado con visuales.
  - [ ] Audio entendible y tiempos informados a Rodrigo.
  - [ ] Registrar toma usada y verificación en informe personal.

## [ ] T-009 — Preparar ficha y coordinar entrega final
- Prioridad: alta: cierre antes del 18 de octubre a las 23:59
- Detalles: Tras aprobación final, fijar commit del código/recursos usado para el video y anotar SHA completo. Preparar ficha PDF y cargar MP4/ficha por separado en Blackboard; todos verifican. No se ejecuta esta entrega al crear el plan. Entregar: entrega/MAT1188_EID_G02_2026.pdf, MP4 final y comprobantes de entrega. Requiere: T-008 en dprado.md: reproducción e integración; T-013 en spereda.md: auditoría final; T-017 en rpedraza.md: video ensamblado; T-004 en dprado.md: verificación administrativa.
- Criterios de aceptación:
  - [ ] Ficha con curso, tres integrantes, tema, pregunta, duración medida, GitHub, SHA, referencias e IA.
  - [ ] SHA corresponde al código utilizado; no intentar que la ficha contenga el SHA del mismo commit que la incorpora.
  - [ ] Archivos con nombres MAT1188_EID_G02_2026 y extensiones correspondientes; abren correctamente.
  - [ ] Repo público accesible; confirmar con todos y conservar comprobantes.
  - [ ] Ética independiente vigente; tamaño de video resuelto solo mediante alternativa autorizada; no alterar versión entregada sin autorización.

## [ ] T-019 — Subir resumen de Daniel y preparar defensa completa
- Prioridad: alta: comprensión individual y evidencia de aportes
- Detalles: Mantener informe desde el primer avance; consolidarlo al cerrar su código. Después revisar también los módulos ajenos y ensayar conceptos, cálculos, parámetros y variaciones antes del 21. Entregar: informes/dprado.md y registro personal de ensayo. Requiere: T-003 en dprado.md: pruebas de cálculo; T-008 en dprado.md: reproducción e integración; T-018 en dprado.md: voz de Daniel.
- Criterios de aceptación:
  - [ ] Resumen breve por tarea: qué, por qué, archivos/commit, prueba y resultado, pendientes.
  - [ ] Incluir fuentes y uso de IA con verificación humana real; informar a Rodrigo para consolidación.
  - [ ] Explicar cálculo, construcción visual y comparación, además del propio módulo.
  - [ ] Resolver una variación sencilla y reconocer condiciones/limitaciones.
  - [ ] Ensayo individual como seleccionado, dudas corregidas y reglas de silencio/recursos comprendidas.
