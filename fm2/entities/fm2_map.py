import numpy as np
from PIL import Image

from dataclasses import dataclass
from scipy.ndimage import distance_transform_edt


@dataclass
class FM2Map:
    '''
    The `FM2Map` is a `dataclass` that contains the information of the map

    Attributes
    ----------
    shape : tuple[int, int] | tuple[int, int, int]
        the shape of the map

    dimensions : int
        the dimensionality of the map

    binary_map: np.ndarray
        the binary map

    w_matrix: np.ndarray
        the speed matrix

    Methods
    -------
    from_binary_map(cls, binary_map: np.ndarray, create_border: bool = False) -> FM2Map:
        creates a map from a binary map

    from_image(cls, filename: str, create_border: bool = False) -> FM2Map:
        creates a map from an image
    '''

    def __init__(self, binary_map: np.ndarray) -> None:
        '''
        Parameters
        ----------
        binary_map: np.ndarray
            the bainary map

        Notes
        -----
        the preferred way to instantiate the class is through the class methods
        '''
        self.shape: tuple[int, int] | tuple[int, int, int] = binary_map.shape
        self.dimensions: int = len(binary_map.shape)
        self.binary_map: np.ndarray = binary_map.astype(int)
        self.w_matrix: np.ndarray = self._create_w_matrix(binary_map)

    @classmethod
    def from_binary_map(cls, binary_map: np.ndarray, create_border: bool = False):
        '''
        instantiates the map from a binary map

        Parameters
        ----------
        binary_map: np.ndarray
            the binary map

        create_border : bool, optional
            when `True` the map gets surrounded by walls

        Raises
        ------
        ValueError
            if the map is nor binary

        Returns
        -------
        out : ~.entities.FM2Map
            an instance of the class
        '''
        if not np.all(np.logical_or(binary_map == 0, binary_map == 1)):
            raise ValueError('the map must be binary')

        if create_border:
            binary_map = cls._create_border(binary_map)

        return cls(binary_map)

    @classmethod
    def from_image(cls, filename: str, create_border: bool = False):
        '''
        instantiates the map from an image

        Parameters
        ----------
        filename : str
            the path to the image

        create_border : bool, optional
            when `True` the map gets surrounded by walls

        Raises
        ------
        ValueError
            if the map is nor binary

        Returns
        -------
        out : ~.entities.FM2Map
            an instance of the class
        '''
        binary_map: np.ndarray = np.array(Image.open(filename))[:, :, 0].astype(int)//255

        if not np.all(np.logical_or(binary_map == 0, binary_map == 1)):
            raise ValueError('the map must be binary')

        if create_border:
            binary_map = cls._create_border(binary_map)

        return cls(binary_map)

    @staticmethod
    def _create_w_matrix(binary_map: np.ndarray) -> np.ndarray:
        w_matrix: np.ndarray = np.array(distance_transform_edt(binary_map))
        return w_matrix/np.max(w_matrix)

    @staticmethod
    def _create_border(binary_map: np.ndarray) -> np.ndarray:
        if len(binary_map.shape) == 2:
            binary_map[:, 0] = 0.0
            binary_map[:, -1] = 0.0
            binary_map[0, :] = 0.0
            binary_map[-1, :] = 0.0
        else:
            binary_map[:, :, 0] = 0.0
            binary_map[:, :, -1] = 0.0
            binary_map[:, 0, :] = 0.0
            binary_map[:, -1, :] = 0.0
            binary_map[0, :, :] = 0.0
            binary_map[-1, :, :] = 0.0

        return binary_map
