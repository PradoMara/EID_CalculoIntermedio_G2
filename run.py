"""Menú para renderizar las escenas de sumas de Riemann o abrir el video con voz."""

import argparse
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
VIDEO_CON_VOZ = ROOT / "video" / "MAT1188_EID_G02_2026.mp4"

OPCIONES_MENU = {
    "1": ("Introducción", "introduccion"),
    "2": ("Desarrollo", "desarrollo"),
    "3": ("Cierre", "cierre"),
    "4": ("Video completo", "guion"),
    "5": ("Video completo con voz", "voz"),
}

ESCENAS = {
    "introduccion": ("introduccion.py", "IntroduccionRiemann"),
    "desarrollo": ("presentacion.py", "DesarrolloGuion"),
    "cierre": ("presentacion.py", "CierreGuion"),
    "completo": ("presentacion.py", "PresentacionGuion"),
    "guion": ("presentacion.py", "PresentacionGuion"),
    "izquierda": ("construcciones.py", "ConstruccionIzquierda"),
    "derecha": ("construcciones.py", "ConstruccionDerecha"),
    "detalle": ("comparacion.py", "DetalleIntervalo"),
    "comparacion": ("comparacion.py", "ComparacionSumas"),
    "integral": ("comparacion.py", "CierreIntegral"),
}


def abrir_archivo(ruta: Path) -> int:
    """Abre un archivo multimedia con el reproductor predeterminado del sistema."""
    if not ruta.is_file():
        print(f"No se encontró el archivo de video en: {ruta}", file=sys.stderr)
        return 1
    print(f"Abriendo video con voz: {ruta}", flush=True)
    if sys.platform.startswith("win"):
        os.startfile(str(ruta))
        return 0
    comando = ["open", str(ruta)] if sys.platform == "darwin" else ["xdg-open", str(ruta)]
    return subprocess.run(comando, cwd=ROOT).returncode


def solicitar_opcion_menu() -> str:
    """Despliega el menú interactivo y devuelve la clave de escena seleccionada."""
    print("\n==================================================")
    print("  Sumas de Riemann — Grupo 2 (MAT1188)")
    print("==================================================")
    print("Seleccione el video que desea ejecutar:")
    print("  1) Introducción")
    print("  2) Desarrollo")
    print("  3) Cierre")
    print("  4) Video completo")
    print("  5) Video completo con voz (abre video\\MAT1188_EID_G02_2026.mp4)")
    print("==================================================")
    while True:
        eleccion = input("Ingrese una opción (1-5): ").strip()
        if eleccion in OPCIONES_MENU:
            return OPCIONES_MENU[eleccion][1]
        print("Opción inválida. Por favor ingrese un número del 1 al 5.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--escena",
        choices=[*ESCENAS, "todas", "voz", "1", "2", "3", "4", "5"],
        default=None,
        help="Opción (1-5) o nombre de escena a ejecutar. Si se omite, muestra el menú.",
    )
    parser.add_argument("--calidad", choices=["l", "m", "h"], default="l",
                        help="l: rápida, m: 720p, h: 1080p.")
    parser.add_argument("--sin-abrir", action="store_true",
                        help="Generar sin abrir el reproductor.")
    args = parser.parse_args()

    if args.escena is None:
        seleccion = solicitar_opcion_menu()
    elif args.escena in OPCIONES_MENU:
        seleccion = OPCIONES_MENU[args.escena][1]
    elif args.escena == "todas":
        seleccion = "guion"
    else:
        seleccion = args.escena

    if seleccion == "voz":
        return abrir_archivo(VIDEO_CON_VOZ)

    candidatos = [ROOT / ".venv" / "Scripts" / "python.exe",
                  ROOT / ".venv" / "bin" / "python"]
    python = next((str(p) for p in candidatos if p.is_file()), sys.executable)
    comprobacion = subprocess.run(
        [python, "-c", "import manim"], cwd=ROOT, capture_output=True, text=True,
    )
    if comprobacion.returncode:
        print("No se pudo cargar Manim en el entorno seleccionado.", file=sys.stderr)
        print(comprobacion.stderr, file=sys.stderr)
        print(f'Instala las dependencias: "{python}" -m pip install -r "{ROOT / "requirements.txt"}"',
              file=sys.stderr)
        return comprobacion.returncode

    archivo, escena = ESCENAS[seleccion]
    comando = [python, "-m", "manim", "render", f"-q{args.calidad}"]
    if not args.sin_abrir:
        comando.append("-p")
    comando.extend([str(ROOT / "src" / "escenas" / archivo), escena])
    print("Generando: " + escena, flush=True)
    if seleccion in ("guion", "completo"):
        print("0:00 Daniel · 1:05 izquierda · 2:00 derecha · "
              "2:55 detalle · 3:25 comparación · 3:55 integral · 4:30 créditos")
        print("Guion actualizado: narradores, fórmula general y créditos de fuentes e IA. Sin audio; validen la locución con el video.")
    resultado = subprocess.run(comando, cwd=ROOT)
    if resultado.returncode == 0:
        print(f"Videos guardados en: {ROOT / 'media' / 'videos' / Path(archivo).stem}")
    return resultado.returncode


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nSimulación cancelada.", file=sys.stderr)
        sys.exit(130)

