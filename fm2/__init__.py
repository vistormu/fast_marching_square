from .fm2 import FM2


def _create_binary_txt() -> None:
    import os

    cwd: str = os.getcwd()

    with open('FileHFM_binary_dir.txt', 'w+') as file:
        file.write(cwd+'/fm2/bin/')


_create_binary_txt()
