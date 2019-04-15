.. _intro:

.. image:: https://readthedocs.org/projects/mpl2tex/badge/?version=latest
   :target: https://mpl2tex.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

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

Clone the repository from GitHub by::

  git clone https://github.com/pearjo/mpl2tex.git

In order to use the Python module you need the ``matplotlib`` package.

Install mpl2tex by doing::

  python setup.py install


.. _usage:


Usage
=====

To use the class import it to your code and call before start plotting::

  from mpl2tex import RcParams

  RcParams()

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
