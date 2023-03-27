Installation
============

Follow the next steps for installing the simulation on your device.

**Requirements:**

* Ubuntu
* Python 3.10.0 or higher


Install miniconda (highly-recommended)
--------------------------------------

It is highly recommended to install all the dependencies on a new virtual environment. For more information check the conda documentation for `installation`_ and `environment management`_. For creating the environment use the following commands on the terminal.

.. _installation: https://conda.io/projects/conda/en/latest/user-guide/install/index.html
.. _environment management: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Install from pip
----------------

The Fast Marching Square is available as a PyPi package!

.. code-block:: bash

    pip install fast-marching-square

Install from source
-------------------

Firstly, clone the repository in your system.

.. code-block:: bash
    
    git clone https://github.com/vistormu/fast_marching_square.git

Finally, enter the directory and install the required dependencies

.. code-block:: bash

    cd fast_marching_square
    pip install -r requirements.txt