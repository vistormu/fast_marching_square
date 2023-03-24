import numpy as np
from typing import NamedTuple


class FM2Info(NamedTuple):
    path: np.ndarray | None
    d_matrix: np.ndarray
