import shutil
from pathlib import Path


def copy_file(file_path: Path, target_dir: Path):
    """
    Копіює файл у підпапку target_dir відповідно до його розширення.
    """
    ext = file_path.suffix[1:].lower()
    if not ext:
        return
    ext_dir = target_dir / ext
    ext_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, ext_dir / file_path.name)
