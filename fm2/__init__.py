from .fm2 import FM2


def _create_binary_txt() -> None:
    import os
    import fm2

    path: str = os.path.abspath(fm2.__file__)
    path = path.split('__init__.py')[0]

    with open('FileHFM_binary_dir.txt', 'w+') as file:
        file.write(path+'bin/')


_create_binary_txt()
