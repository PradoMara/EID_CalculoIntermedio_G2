"""Genera y abre la presentación continua del guion: python run.py (4:45, sin audio)."""

import argparse
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
ESCENAS = {
    "guion": ("presentacion.py", "PresentacionGuion"),
    "introduccion": ("introduccion.py", "IntroduccionRiemann"),
    "izquierda": ("construcciones.py", "ConstruccionIzquierda"),
    "derecha": ("construcciones.py", "ConstruccionDerecha"),
    "detalle": ("comparacion.py", "DetalleIntervalo"),
    "comparacion": ("comparacion.py", "ComparacionSumas"),
    "integral": ("comparacion.py", "CierreIntegral"),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--escena", choices=[*ESCENAS, "todas"],
                        default="guion", help="guion/todas: presentación completa; otras: ensayo individual.")
    parser.add_argument("--calidad", choices=["l", "m", "h"], default="l",
                        help="l: rápida, m: 720p, h: 1080p.")
    parser.add_argument("--sin-abrir", action="store_true",
                        help="Generar sin abrir el reproductor.")
    args = parser.parse_args()

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

    seleccion = "guion" if args.escena == "todas" else args.escena
    archivo, escena = ESCENAS[seleccion]
    comando = [python, "-m", "manim", "render", f"-q{args.calidad}"]
    if not args.sin_abrir:
        comando.append("-p")
    comando.extend([str(ROOT / "src" / "escenas" / archivo), escena])
    print("Generando: " + escena, flush=True)
    if seleccion == "guion":
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
