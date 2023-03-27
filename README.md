# Fast Marching Square

The [Fast Marching Square (FM2) method](https://www.researchgate.net/profile/Santiago-Garrido/publication/305377309_FM2_A_real_Fast_Marching_sensor-based_Motion_Planner/links/59649679aca2728c1129ec03/FM2-A-real-Fast-Marching-sensor-based-Motion-Planner.pdf) is a path planning algorithm which is a variation of the [original Fast Marching Method](https://epubs.siam.org/doi/abs/10.1137/S0036144598347059), which it is based on the idea of guiding the desired path by following light propagation. The path that light follows is always the fastest feasible one, so the proposed planning method ensures the calculation of the path of least possible time. Since the method is based on wave propagation, if there is a feasible solution, it is always found, so it is complete.

This implementation of the Fast Marching Squared method is based on the [Mirebeau implementation](https://github.com/Mirebeau/HamiltonFastMarching), so feel free to visit the repository.

## Installation

Follow the next steps for installing the simulation on your device.

**Requirements:**
- Python 3.10.0 or higher


### Install miniconda (highly-recommended)
It is highly recommended to install all the dependencies on a new virtual environment. For more information check the conda documentation for [installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and [environment management](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). For creating the environment use the following commands on the terminal.

```bash
conda create -n fm2 python==3.10.9
conda activate fm2
```
### Install from pip

The ADAM simulator is available as a pip package. For installing it just use:
```
pip install fast-marching-square
```

### Install from source
Firstly, clone the repository in your system.
```bash
git clone https://github.com/vistormu/fast_marching_square.git
```

Then, enter the directory and install the required dependencies
```bash
cd fast_marching_square
pip install -r requirements.txt
```

## Documentation
The official documentation of the package is available on [Read the Docs](https://fast-marching-square.readthedocs.io/en/latest/). Here you will find the [installation instructions](https://fast-marching-square.readthedocs.io/en/latest/src/installation.html), the [API reference](https://fast-marching-square.readthedocs.io/en/latest/src/api_reference.html) and some [minimal working examples](https://fast-marching-square.readthedocs.io/en/latest/src/examples.html).