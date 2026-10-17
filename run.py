"""Genera y abre la simulación de sumas de Riemann: python run.py."""

import argparse
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
ESCENAS = {
    "comparacion": "ComparacionSumas",
    "detalle": "DetalleIntervalo",
    "integral": "CierreIntegral",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--escena", choices=[*ESCENAS, "todas"],
                        default="comparacion", help="Escena a generar.")
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

    escenas = list(ESCENAS.values()) if args.escena == "todas" else [ESCENAS[args.escena]]
    comando = [python, "-m", "manim", "render", f"-q{args.calidad}"]
    if not args.sin_abrir:
        comando.append("-p")
    comando.extend([str(ROOT / "src" / "escenas" / "comparacion.py"), *escenas])
    print("Generando simulación: " + ", ".join(escenas), flush=True)
    resultado = subprocess.run(comando, cwd=ROOT)
    if resultado.returncode == 0:
        print(f"Videos guardados en: {ROOT / 'media' / 'videos' / 'comparacion'}")
    return resultado.returncode


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nSimulación cancelada.", file=sys.stderr)
        sys.exit(130)
