import numpy as np

from agd import Eikonal
from vclog import Logger


class HFM:
    def __init__(self, dimensions: int, mode: str) -> None:
        self.hfm_in: Eikonal.dictIn = Eikonal.dictIn({
            'model': 'Isotropic2' if dimensions == 2 else 'Isotropic3',
            'mode': mode,
            'exportValues': True,
        })

    def run(self, starting_point: np.ndarray, goal_point: np.ndarray, w_matrix: np.ndarray) -> np.ndarray:
        self.hfm_in['cost'] = 1.0 - w_matrix
        self.hfm_in['tip'] = starting_point
        self.hfm_in['seed'] = goal_point

        self.hfm_in.SetRect(sides=[[1, w_matrix.shape[0]], [1, w_matrix.shape[1]]], dimx=w_matrix.shape[0])

        hfm_out: Eikonal.dictOut = self.hfm_in.Run()  # type: ignore

        path = []
        for geodesic in hfm_out['geodesics']:
            path = geodesic

        return np.array(path)
