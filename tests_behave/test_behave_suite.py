# tests_behave/test_behave_suite.py
import subprocess
import pathlib
import pytest
from utils.logger_config import logger

REPORTS_DIR = pathlib.Path('reports/behave')
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

FEATURES_DIR = 'features'


def _ejecutar_behave(tags: str, nombre_run: str):
    """
    Ejecuta behave vía subprocess, filtrando por tag,
    generando reporte JSON y reporte pretty (legible) por separado.
    """
    json_output = REPORTS_DIR / f"{nombre_run}.json"
    pretty_output = REPORTS_DIR / f"{nombre_run}_pretty.txt"

    comando = [
        "py", "-m", "behave", FEATURES_DIR,
        "--tags", tags,
        "-f", "json", "-o", str(json_output),
        "-f", "pretty", "-o", str(pretty_output),
    ]

    logger.info(f"Ejecutando behave con tags={tags}, comando: {' '.join(comando)}")
    resultado = subprocess.run(comando, capture_output=True, text=True)
    logger.info(f"Behave finalizo con returncode={resultado.returncode}")

    return resultado


@pytest.mark.smoke
def test_behave_smoke():
    """
    Ejecuta únicamente los escenarios etiquetados @smoke
    """
    resultado = _ejecutar_behave(tags="@smoke", nombre_run="smoke")
    assert resultado.returncode == 0, resultado.stdout + resultado.stderr


@pytest.mark.regression
def test_behave_regression():
    """
    Ejecuta únicamente los escenarios etiquetados @regression
    """
    resultado = _ejecutar_behave(tags="@regression", nombre_run="regression")
    assert resultado.returncode == 0, resultado.stdout + resultado.stderr