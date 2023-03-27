Examples
========

Basic Usage
-----------

.. code-block:: Python
    
    import numpy as np
    import matplotlib.pyplot as plt

    from fm2 import FM2
    from fm2.entities import FM2Map, FM2Info


    def main():
        fm2: FM2 = FM2(mode='cpu')

        # Generate map
        image: np.ndarray = np.ones((100, 100))
        image[:, 0] = 0.0
        image[:, -1] = 0.0
        image[0, :] = 0.0
        image[-1, :] = 0.0

        image[25:75, 25:75] = 0.0

        fm2_map: FM2Map = FM2Map.from_binary_map(image)
        fm2.set_map(fm2_map)

        # Calculate path
        start_point: tuple[int, int] = (5, 50)
        goal_point: tuple[int, int] = (95, 95)
        info: FM2Info = fm2.get_path(start_point, goal_point)

        if info.path is None:
            return

        # Representation
        fig, axes = plt.subplots(1, 2, figsize=(8, 4))
        axes[0].imshow(fm2_map.binary_map, cmap='gray')
        axes[0].set_title('Binary image')

        axes[1].imshow(fm2_map.w_matrix, cmap='gray')
        axes[1].set_title('Distance transform')
        axes[1].plot(*info.path, c='#924242')
        axes[1].scatter(*start_point, c='#3fad50')
        axes[1].scatter(*goal_point, c='#924242')

        plt.show()

    if __name__ == '__main__':
        main()