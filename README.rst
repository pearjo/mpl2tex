.. _intro:


===========================================================
**mpl2tex** - Configure Matplotlib for better LaTeX export.
===========================================================

A Python module to update the matplotlibrc parameters to adapt the figure to
include it as pgf into a LaTeX document.


.. _getting_started:


***************
Getting started
***************


.. _installing-mpl2tex:


Installing mpl2tex
==================

In order to use the Python module you need the ``matplotlib`` package.

Install mpl2tex by doing::

  python setup.py install


.. _usage:


Usage
=====

To use the class import it to your code and call before start plotting::

  from mpl2tex import RcParams

  RcParamsSetup(width, fontsize, ratio, serif, linewidth, bw)

To include the figure in your TeX document save it as ``pgf`` and write in
your TeX code:

.. sourcecode:: latex

  \begin{figure}
    \centering
    \input{<filename>.pgf}
    \caption{Sinus and cosinus function generated with Matplotlib and mpl2tex}
  \end{figure}

Make sure to load the required ``pgf`` package in your preamble. If you
save the figure not in your document's root directory you can use the
``import`` package:

.. sourcecode:: latex

  \begin{figure}
    \centering
    \import{<path to file>}{<filename>.pgf}
    \caption{Sinus and cosinus function generated with Matplotlib and mpl2tex}
  \end{figure}

.. _mpl2tex_help:

Help in Python
--------------

If you are running IPython, you can get direct help for the modules.

.. sourcecode:: python

    >>> import mpl2tex
    >>> help(mpl2tex.RcParams)
    Help on class RcParams in module mpl2tex.rcparams:

    class RcParams(builtins.object)
     |  RcParams(width=1.0, columnwidth=345, fontsize=10, ratio='gr', serif=True, bw=False, marker=False)
     |
     |  Generate rcParams for matplotlib.
     |
     |  Updates the matplotlibrc for best export to LaTeX.


.. _users_guide:


User's Guide
============

For a full documentation change into `doc` and build the documentation for
example as html.

.. sourcecode:: bash

    $ cd doc/
    $ make html
