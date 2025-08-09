from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from .file_handler import copy_file


def process_directory(directory: Path, target_dir: Path, file_executor: ThreadPoolExecutor, dir_executor: ThreadPoolExecutor):
    """
    Рекурсивно обходить директорії.
    Для кожного підкаталогу створює новий потік у dir_executor.
    Для кожного файлу створює новий потік у file_executor.
    """
    futures = []
    for entry in directory.iterdir():
        if entry.is_dir():
            futures.append(
                dir_executor.submit(process_directory, entry, target_dir, file_executor, dir_executor)
            )
        elif entry.is_file():
            file_executor.submit(copy_file, entry, target_dir)
    return futures
