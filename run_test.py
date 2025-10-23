import pytest

#Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login2.py",
    "tests/test_inventory2.py",
]

# Argumentos para ejecutar pruebas: archivos + reporte HTML
pytest_args = test_files + [
    "--html=report.html",
    "--self-contained-html",
    "-v",
]

pytest.main(pytest_args)