import numpy as np
import matplotlib.pyplot as plt

from fm2.entities import FM2Map


def main():
    # From array without borders
    image: np.ndarray = np.ones((100, 100))
    image[:, 0] = 0.0
    image[:, -1] = 0.0
    image[0, :] = 0.0
    image[-1, :] = 0.0

    image[25:75, 25:75] = 0.0

    first_map: FM2Map = FM2Map.from_binary_map(image)

    # From array without borders
    image: np.ndarray = np.ones((100, 100))
    image[25:75, 25:75] = 0.0

    second_map: FM2Map = FM2Map.from_binary_map(image, create_border=True)

    # From image
    third_map: FM2Map = FM2Map.from_image('tests/assets/pies2.png')

    # Show images
    _, axes = plt.subplots(3, 2, figsize=(8, 4))

    axes[0][0].imshow(first_map.binary_map, cmap='gray')
    axes[0][1].imshow(first_map.w_matrix, cmap='gray')

    axes[1][0].imshow(second_map.binary_map, cmap='gray')
    axes[1][1].imshow(second_map.w_matrix, cmap='gray')

    axes[2][0].imshow(second_map.binary_map, cmap='gray')
    axes[2][1].imshow(second_map.w_matrix, cmap='gray')

    plt.show()

    # 3D map
    image: np.ndarray = np.ones((100, 100, 100))
    image[25:75, 25:75, 0:50] = 0.0

    fm2_map: FM2Map = FM2Map.from_binary_map(image)

    map_to_plot = 1 - fm2_map.binary_map

    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(map_to_plot, facecolors='red', edgecolor='k')

    plt.show()


if __name__ == '__main__':
    main()
