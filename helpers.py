from pathlib import Path
import subprocess
from typing import List
import config


def compile(path):
    path = Path(path)
    output = path.parent / f"{path.stem}_ui.py"
    args = ["pyside6-uic", str(path), "-o", str(output)]
    subprocess.run(args)


def find_ui_files(folder: Path, depth=0, term_search="") -> List[Path]:
    if depth >= config.max_depth:
        return []
    items = []
    for entry in folder.iterdir():
        if entry.is_dir():
            items += find_ui_files(entry, depth + 1, term_search=term_search)
        elif entry.suffix == ".ui":
            if term_search != "" and term_search not in entry.name:
                continue
            items.append(entry)
    return items
