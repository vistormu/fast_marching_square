import numpy as np
from typing import NamedTuple


class FM2Info(NamedTuple):
    '''
    The `FM2Info` is a `NamedTuple` that contains the information of the calculated path

    Attributes
    ----------
    path : np.ndarray | None
        the calculated path. Returns None if a path is not found

    d_matrix: np.ndarray
        the propagation matrix of the electromagnetic wave. It has the same size as the given map
    '''
    path: np.ndarray | None
    d_matrix: np.ndarray
