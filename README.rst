PyDrone game
============

This project is part of a Computer Science thesis.

Thesis title
------------

Solving a direction finding problem with a single anchor positioning algorithm

Description
-----------

Not available at the moment.

Requirements
------------

Simply create your virtual env and install requirements:

.. code-block:: bash

    $ pip install -r requirements.txt

Usage
-----

.. code-block:: bash

    Usage: pydrone_game.py [OPTIONS] ANCHOR_X ANCHOR_Y DRONE_X DRONE_Y

    Options:
      --size INTEGER                Matrix size
      --benchmark / --no-benchmark  Start benchmark interfaces
      --help                        Show this message and exit.

Interactive mode is available during drone algorithm execution.
By default ``GeometricDrone`` is executed with these default values:

.. code-block:: bash

    size: 40x40 matrix
    anchor x: 5
    anchor y: 19
    drone x: 30
    drone y: 30

To run this project with default settings, simply:

.. code-block:: bash

    $ python pydrone_game.py

Benchmark interface
-------------------

To run tests between your algorithm and another one (``GreedyCompleteDrone`` at the moment)
run this command to execute a curses wrapper:

.. code-block::

    $ python pydrone_game.py --benchmark

and follow the instruction on the screen.

Settings
--------

In ``settings.py`` file you can define everything is needed to change project behaviour:

.. code-block:: bash

    EXECUTION_DRONE: class of executed drone during interaction mode
    BENCHMARK_DRONE: class of the best algorithm available during benchmarks

License
-------

BSD License. See ``LICENSE`` file for more details.
