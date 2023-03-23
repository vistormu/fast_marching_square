import numpy as np
import matplotlib.pyplot as plt

from fm2 import FM2

from vclog import Logger


def main():
    fm2: FM2 = FM2(dimensions=2, mode='cpu')

    # Generate map
    image: np.ndarray = np.ones((100, 100))
    image[:, 0] = 0.0
    image[:, -1] = 0.0
    image[0, :] = 0.0
    image[-1, :] = 0.0

    image[25:75, 25:75] = 0.0

    fm2.set_map(image)

    # Calculate path
    goal_point: tuple[int, int] = (10, 10)
    start_point: tuple[int, int] = (90, 90)
    path: np.ndarray = fm2.get_path(start_point, goal_point)

    # Representation
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Binary image')

    w_matrix: np.ndarray = fm2.get_w_matrix(map=image)

    axes[1].imshow(w_matrix, cmap='gray')
    axes[1].set_title('Distance transform')

    # plt.figure()
    plt.scatter([start_point[0], goal_point[0]], [start_point[1], goal_point[1]])
    plt.plot(*path)
    plt.show()


if __name__ == '__main__':
    main()
