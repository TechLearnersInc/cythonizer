==========
cythonizer
==========

*Cythonize one step faster*

.. image:: https://img.shields.io/badge/build-beta-brightgreen
   :target: https://github.com/TechLearnersInc/cythonizer

.. image:: https://img.shields.io/badge/license-MIT-green
   :target: LICENSE.txt

.. image:: https://img.shields.io/static/v1?label=Created%20with%20%E2%9D%A4%EF%B8%8F%20by&message=TechLearners&color=red
   :target: https://github.com/TechLearnersInc

Introduction
------------

:code:`cythonizer.py` is a script that will attempt to
automatically convert one or more :code:`.py` and :code:`.pyx` files into
the corresponding compiled :code:`.pyd | .so` binary modules
files. Example::

    $ python cythonizer.py myext.pyx

:code:`pip install cythonizer` will automatically create an
executable script in your :code:`Scripts/` folder, so you
should be able to simply::

    $ cythonizer myext.py

or even::

    $ cythonizer *.pyx

You can type::

    $ cythonizer -h

to obtain the following CLI::

    usage: cythonizer.py [-h] [--annotation] [--numpy-includes]
                         [--debugmode] filenames [filenames ...]

    positional arguments:
    filenames         .py and .pyx files only

    optional arguments:
    -h, --help        show this help message and exit
    --annotation      (default: False)
    --numpy-includes  (default: False)
    --debugmode       (default: False)


- :code:`--annotation` will create the HTML Cython annotation file.
- :code:`--numpy-includes` will add the numpy headers to the build command.
- Compiler flags :code:`-O2 -march=native` are automatically passed to the compiler.
