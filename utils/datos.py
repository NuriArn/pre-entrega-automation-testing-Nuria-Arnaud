import csv
from pathlib import Path
from typing import List, Tuple


def leer_csv_login(ruta_csv: str) -> List[Tuple[str, str, bool]]:
    """
    Lee un CSV de login con columnas: usuario,password,debe_funcionar
    debe_funcionar puede ser: true/false, si/no, 1/0
    Retorna lista de tuplas (usuario, password, debe_funcionar)
    """
    path = Path(ruta_csv)
    if not path.exists():
        raise FileNotFoundError(f"No existe el CSV: {ruta_csv}")

    casos = []
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            usuario = (row.get("usuario") or "").strip()
            password = (row.get("password") or "").strip()
            debe = (row.get("debe_funcionar") or "").strip().lower()
            debe_bool = debe in ("true", "1", "si", "sí", "yes", "y")
            casos.append((usuario, password, debe_bool))

    return casos
