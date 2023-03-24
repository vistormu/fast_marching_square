import numpy as np
from PIL import Image

from dataclasses import dataclass
from scipy.ndimage import distance_transform_edt


@dataclass
class FM2Map:
    def __init__(self, binary_map: np.ndarray) -> None:
        self.shape: tuple[int, int] | tuple[int, int, int] = binary_map.shape
        self.dimensions: int = len(binary_map.shape)
        self.binary_map: np.ndarray = binary_map.astype(int)
        self.w_matrix: np.ndarray = self._create_w_matrix(binary_map)

    @classmethod
    def from_binary_map(cls, binary_map: np.ndarray, create_border: bool = False):
        if not np.all(np.logical_or(binary_map == 0, binary_map == 1)):
            raise ValueError('the map must be binary')

        if create_border:
            binary_map = cls._create_border(binary_map)

        return cls(binary_map)

    @classmethod
    def from_image(cls, filename: str, create_border: bool = False):
        binary_map: np.ndarray = np.array(Image.open(filename))[:, :, 0]//255

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
