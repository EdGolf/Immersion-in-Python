from random import randint, sample, randbytes
from string import ascii_letters
from pathlib import Path

__all__ = ["random_files_creator", "random_files_creator_ex"]


def random_files_creator(dir_path: Path, *, ext: str, min_name_len: int = 6, max_name_len: int = 30,
                         min_file_size: int = 256,
                         max_file_size: int = 4096, count: int = 42) -> None:
    """
    Создает файлы со случайным именем и содержимым.
    """
    while count > 0:
        name_len = randint(min_name_len, max_name_len)
        size = randint(min_file_size, max_file_size)
        file_name = ''.join(sample(ascii_letters, name_len)) + f".{ext}"
        file_path = dir_path / file_name
        if not file_path.exists():
            with file_path.open('wb') as f:
                f.write(randbytes(size))
            count -= 1


def random_files_creator_ex(dir_path: str | Path, *args, **kwargs) -> None:
    """
    Создает файлы со случайным именем и содержимым.
    """
    if not isinstance(dir_path, Path):
        dir_path = Path(dir_path)

    if not dir_path.exists():
        dir_path.mkdir(parents=True)
    elif not dir_path.is_dir():
        return

    for i in range(0, len(args) & ~0b1, 2):
        if isinstance(args[i], str) and isinstance(args[i + 1], int):
            random_files_creator(dir_path=dir_path, ext=args[i], count=args[i + 1], max_name_len=10)

    for ext, count in kwargs.items():
        if isinstance(count, int):
            random_files_creator(dir_path=dir_path, ext=ext, count=count, max_name_len=10)