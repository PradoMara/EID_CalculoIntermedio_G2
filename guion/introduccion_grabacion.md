# Introducción para grabar — Daniel Prado

Video: `output/video/Introduccion_Riemann_Manim_1080p.mp4`.
Duración: 65 segundos. Sin audio, para incorporar tu propia voz.
Los tiempos incluyen la aparición de los objetos. Ensaya una vez con el video antes de grabar; no leas los títulos ni las fórmulas letra por letra.

| Tiempo | Locución |
| --- | --- |
| 00:00–00:11 | Hola, soy Daniel Prado. Junto a Sebastian Pereda y Rodrigo Pedraza preguntamos: ¿por qué dos sumas sobre la misma partición pueden dar valores distintos? |
| 00:11–00:20 | Consideremos una función continua y no negativa en un intervalo cerrado. Así, cada aporte rectangular representa un área geométrica. |
| 00:20–00:32 | La partición divide el intervalo en ene subintervalos. Cada uno tiene un ancho: delta equis, igual al extremo derecho menos el izquierdo. La partición fija las bases. |
| 00:32–00:45 | La suma de Riemann reúne ene aportes: altura por base. La altura es la función evaluada en un punto muestra del subintervalo; la base es su ancho. |
| 00:45–00:58 | Podemos elegir el extremo izquierdo o el derecho como punto muestra. Al cambiarlo, las bases permanecen iguales, pero las alturas pueden cambiar y producir aportes distintos. |
| 00:58–01:05 | Lo veremos con equis al cuadrado más uno, entre cero y dos: cuatro subintervalos de ancho cero coma cinco. |

## Grabación y montaje

1. Reproduce el MP4 y graba tu voz siguiendo los bloques. Es normal necesitar varias tomas.
2. Coloca la grabación desde el segundo cero en tu editor y ajusta los silencios entre frases.
3. Une esta introducción con la construcción de Sebastian desde 01:05. El clip es solo la introducción; el video completo debe durar entre 4 y 6 minutos.
4. Comprueba la sincronización especialmente en 00:50–00:52: allí los puntos y las alturas pasan del criterio izquierdo al derecho.

## Qué se animó con Manim

Se reconstruyeron los seis temas del PDF como texto, ejes, curva, partición, puntos muestra y rectángulos vectoriales. No se insertaron imágenes del PDF en el MP4. La comparación utiliza la función y partición compartidas de `src/matematica.py`; las bases se mantienen mientras se transforman las alturas. Las condiciones de continuidad y no negatividad describen el caso geométrico elegido, no requisitos universales para definir cualquier suma de Riemann.

## Reproducir el render

Desde la raíz del proyecto, en PowerShell:

```powershell
.\.venv\Scripts\python.exe -m manim render src/escenas/introduccion.py IntroduccionRiemann -r 1920,1080 --fps 30
```

Manim Community 0.22.0. Usa texto Unicode y no requiere LaTeX. El archivo original del render queda en `media/videos/introduccion/1080p30/IntroduccionRiemann.mp4`.

## Atribución y revisión pendiente

Basado en `docs/introduccion/Anatomía_de_las_Sumas_de_Riemann.pdf` (las láminas muestran una marca Gemini Notebook). Adaptación del contenido y programación de las animaciones asistidas por Codex. Daniel debe revisar el contenido, comprender el código y grabar su propia explicación. Registrar esta adaptación y el apoyo de IA en los créditos generales. Usar Manim satisface esa parte técnica, pero no garantiza puntaje: también se evalúan explicación, sincronización, fuentes, participación y defensa.
