import numpy as np

from agd import Eikonal

from .entities import FM2Map, FM2Info


class FM2:
    '''
    The `FM2` class contains all the methods for calculating a path with the Fast Marching Square Method.

    Methods
    -------
    set_map(self, fm2_map: FM2Map) -> None:
        sets the map in which to calculate the path

    get_path(self, starting_point: tuple[int, int] | tuple[int, int, int], goal_point: tuple[int, int] | tuple[int, int, int]) -> FM2Info:
        gets the path given a start point and a goal point
    '''

    def __init__(self, mode: str = 'cpu') -> None:
        '''
        Parameters
        ----------
        mode : str, optional
            execute in cpu or in gpu. Default 'cpu'

        Note
        ----
        GPU mode is not supported yet
        '''
        if mode == 'gpu':
            raise NotImplementedError('GPU mode is not implemented')

        self.hfm_in: Eikonal.dictIn = Eikonal.dictIn({
            'verbosity': 0,
            'mode': mode,
            'exportValues': 1,
            'gridScale': 1.0,
        })

    def set_map(self, fm2_map: FM2Map) -> None:
        '''
        sets the map in which to calculate the path

        Parameters
        ----------
        fm2_map : ~.entities.FM2Map
            the specified map
        '''
        map_dict: dict = {
            'model': 'Isotropic2' if fm2_map.dimensions == 2 else 'Isotropic3',
            'speed': fm2_map.w_matrix,
            'dims': fm2_map.shape,
            'origin': (0, 0) if fm2_map.dimensions == 2 else (0, 0, 0),
        }

        self.hfm_in.update(map_dict)

    def get_path(self, start_point: tuple[int, int] | tuple[int, int, int], goal_point: tuple[int, int] | tuple[int, int, int]) -> FM2Info:
        '''
        returns the path given a start point and a goal point

        Parameters
        ----------
        start_point : tuple[int, int] | tuple[int, int, int]
            the start point of the path

        goal_point : tuple[int, int] | tuple[int, int, int]
            the goal point of the path

        Returns
        -------
        out : ~.entities.FM2Info
            the info of the calculated path
        '''

        points_dict: dict = {
            'tip': start_point,
            'seed': goal_point,
        }

        self.hfm_in.update(points_dict)

        hfm_out: Eikonal.dictOut = self.hfm_in.Run()  # type: ignore

        path: np.ndarray = hfm_out['geodesics'][0]

        path_found: bool = True
        if len(path[0]) == 1:
            path_found = False

        return FM2Info(path if path_found else None, hfm_out['values'])
