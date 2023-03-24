import numpy as np

from agd import Eikonal

from .entities import FM2Map, FM2Info


class FM2:
    def __init__(self, mode: str = 'cpu') -> None:
        self.hfm_in: Eikonal.dictIn = Eikonal.dictIn({
            'verbosity': 0,
            'mode': mode,
            'exportValues': 1,
            'gridScale': 1.0,
        })

    def set_map(self, fm2_map: FM2Map) -> None:
        map_dict: dict = {
            'model': 'Isotropic2' if fm2_map.dimensions == 2 else 'Isotropic3',
            'speed': fm2_map.w_matrix,
            'dims': fm2_map.shape,
            'origin': (0, 0) if fm2_map.dimensions == 2 else (0, 0, 0),
        }

        self.hfm_in.update(map_dict)

    def get_path(self, starting_point: tuple[int, int] | tuple[int, int, int], goal_point: tuple[int, int] | tuple[int, int, int]) -> FM2Info:
        points_dict: dict = {
            'tip': starting_point,
            'seed': goal_point,
        }

        self.hfm_in.update(points_dict)

        hfm_out: Eikonal.dictOut = self.hfm_in.Run()  # type: ignore

        path: np.ndarray = hfm_out['geodesics'][0]

        path_found: bool = True
        if len(path[0]) == 1:
            path_found = False

        return FM2Info(path if path_found else None, hfm_out['values'])

    @staticmethod
    def _gradient_descent(matrix, start_point, learning_rate, num_iterations):
        x, y = start_point
        path = [(x, y)]
        value = matrix[x][y]

        for i in range(num_iterations):
            dx, dy = np.gradient(matrix)
            x -= learning_rate * dx[int(x)][int(y)]
            y -= learning_rate * dy[int(x)][int(y)]
            x = np.clip(x, 0, matrix.shape[0]-1)
            y = np.clip(y, 0, matrix.shape[1]-1)
            path.append((x, y))
            value = matrix[int(x)][int(y)]

        return (path, value)
