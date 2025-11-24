import pytest

# Ejecuta toda la suite (UI + API) y genera reporte HTML en reports/
pytest_args = [
    "-v",
    "--html=reports/report.html",
    "--self-contained-html",
]

raise SystemExit(pytest.main(pytest_args))
