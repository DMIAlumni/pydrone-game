PyDrone game
============

This project is part of a Computer Science thesis.

Thesis title
------------

Solving a direction finding problem with a single anchor positioning algorithm

Description
-----------

Not available at the moment.

Usage
-----

:: code-block::

    Usage: pydrone.py [OPTIONS] ANCHOR_X ANCHOR_Y DRONE_X DRONE_Y

    Options:
      --size INTEGER  Matrix size
      --help          Show this message and exit.

Interactive mode is available during drone algorithm execution.
By default ``GeometricDrone`` is executed with these default values:

:: code-block::

    size: 40x40 matrix
    anchor x: 5
    anchor y: 19
    drone x: 30
    drone y: 30

To run tests in interactive mode, got to project root and run:

.. code-block::

    $ python curses_tests.py

and follow the instruction on the screen.

For more tests, check:

.. code-block::

    $ python better_tests.py -h

License
-------

BSD License. See ``LICENSE`` file for more details.
