import numpy as np
from scipy.ndimage import distance_transform_edt


from .use_cases import HFM


class FM2:
    def __init__(self, dimensions: int, mode: str = 'cpu') -> None:
        self.hfm: HFM = HFM(dimensions, mode)

    def get_path(self, starting_point: np.ndarray, goal_point: np.ndarray, map: np.ndarray | None = None, w_matrix: np.ndarray | None = None) -> np.ndarray:
        # Function requierements
        if map is None and w_matrix is None:
            raise Exception('either the map or the w_matrix must be passed as a parameter for the function')
        elif not np.all(np.logical_or(map == 0, map == 1)):
            raise ValueError('the map must be binary')
        elif w_matrix is None:
            w_matrix = self.get_w_matrix(map)  # type: ignore

        path: np.ndarray = self.hfm.run(starting_point, goal_point, w_matrix)

        return path

    def get_w_matrix(self, map: np.ndarray) -> np.ndarray:
        w_matrix = np.array(distance_transform_edt(map))
        w_matrix = w_matrix/np.max(w_matrix)
        return w_matrix
