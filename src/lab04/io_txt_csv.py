import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    """Читаем текст целиком в указанной кодировке."""
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path):
    """Создаём родительские каталоги для указанного файла."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows, path: str | Path, header=None):
    """Проверяем длину строк и записываем CSV в UTF-8."""
    width = None
    if header is not None:
        width = len(header)
    for row in rows:
        if width is None:
            width = len(row)
        if len(row) != width:
            raise ValueError("Все строки CSV должны иметь одинаковую длину")

    ensure_parent_dir(path)
    with Path(path).open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)
