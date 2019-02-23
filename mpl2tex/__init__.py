"""
mpl2tex
=======

A module to update the matplotlibrc parameters to adapt the figure to
include it as pgf into a LaTeX document.
"""
__version__ = '1.0.0'

# from mpl2tex.rcparams import RcParams
from mpl2tex.rcparams import rcParamsDefault
from mpl2tex.rcparams import update_params
