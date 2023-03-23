import numpy as np
from scipy.ndimage import distance_transform_edt, distance_transform_cdt


from .use_cases import HFM


class FM2:
    def __init__(self, dimensions: int, mode: str = 'cpu') -> None:
        self.hfm: HFM = HFM(dimensions, mode)

    def set_map(self, map: np.ndarray) -> None:
        if not np.all(np.logical_or(map == 0, map == 1)):
            raise ValueError('the map must be binary')

        w_matrix: np.ndarray = self.get_w_matrix(map)
        self.hfm.set_map(map, w_matrix)

    def get_path(self, starting_point: tuple[int, int], goal_point: tuple[int, int]) -> np.ndarray:
        path: np.ndarray = self.hfm.run(starting_point, goal_point)

        return path

    def get_w_matrix(self, map: np.ndarray) -> np.ndarray:
        # w_matrix: np.ndarray = np.array(distance_transform_cdt(map, metric='taxicab'))
        w_matrix: np.ndarray = np.array(distance_transform_edt(map))
        w_matrix = w_matrix/np.max(w_matrix)
        return w_matrix
