# built-in modules
from os import walk
from os.path import join, relpath
from zipfile import ZipFile

def percentage(part: float | int, whole: float | int) -> float | int:
    return 100 * part / whole

def formatted_sizeof(num: int, suffix: str = 'B') -> str:
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return f'{num:3.1f}{unit}{suffix}'
        num /= 1024.0
    return f'{num:.1f}Yi{suffix}'

def zipdir(name: str, zipr: ZipFile):
    for folder_name, _, file_names in walk(name):
        for file_name in file_names:
            file_path = join(folder_name, file_name)
            zipr.write(file_path, arcname=relpath(file_path, name))