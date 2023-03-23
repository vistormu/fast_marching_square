import numpy as np

from agd import Eikonal
from vclog import Logger

from scipy.optimize import minimize

import matplotlib.pyplot as plt


class HFM:
    def __init__(self, dimensions: int, mode: str) -> None:
        self.hfm_in: Eikonal.dictIn = Eikonal.dictIn({
            'model': 'Isotropic2' if dimensions == 2 else 'Isotropic3',
            'mode': mode,
            'exportValues': 1,
            'gridScale': 1.0,
            'order': 1,
            'origin': (0, 0),
        })

    def set_map(self, map: np.ndarray, w_matrix: np.ndarray) -> None:
        map_dict: dict = {
            'speed': w_matrix,
            'walls': 1.0 - map,
            'dims': map.shape,
        }

        self.hfm_in.update(map_dict)

    def run(self, starting_point: tuple[int, int], goal_point: tuple[int, int]) -> np.ndarray:
        points_dict: dict = {
            'tip': starting_point,
            'seed': goal_point,
        }

        self.hfm_in.update(points_dict)

        hfm_out: Eikonal.dictOut = self.hfm_in.Run()  # type: ignore

        path = []
        for geodesic in hfm_out['geodesics']:
            Logger.debug(geodesic)

        d = hfm_out['values']

        d[d == np.inf] = 0
        d = d/np.max(d[1:])

        # plt.figure()
        ax = plt.figure().add_subplot(111, projection='3d')
        x = y = np.arange(0, 100, 1)
        X, Y = np.meshgrid(x, y)

        ax.plot_surface(X, Y, d, cmap='jet')
        plt.show()

        def callback(xk) -> bool:
            Logger.warning(xk)
            return False

        def gradient_function(x, d):

            return [(d[x[0].astype(int), x[1].astype(int)]/1000), (d[x[0].astype(int), x[1].astype(int)]/1000)]

        def objective_function(x, d):
            Logger.error(d[x[0].astype(int), x[1].astype(int)])
            return d[x[0].astype(int), x[1].astype(int)]

        result = minimize(fun=objective_function, jac=gradient_function, x0=starting_point, method='BFGS', args=(d),
                          callback=callback, options={'maxiter': 1000, 'disp': True, 'gtol': 1e-6, 'step_size': 0.1})
        print(result.x)
        # Logger.debug(hfm_out['values'])

        return hfm_out['geodesics'][0]
