.. _example:


*******
Example
*******

To use mpl2tex you need to know the pager width and font size of your TeX
document. If you don't know them add ``\showthe\columnwidth`` to your TeX
code. When running ``pdflatex`` it will stop and show you the columnwidth
of your document. For a ``\documentclass[a4paper]{article}``
document it will be 345 pt and the font size will be 10 pt by default.
To plot the sin and cos function write::

  import matplotlib.pyplot as plt
  import numpy as np
  from mpl2tex import RcParams

  RcParams(bw=True)  # set the figure parameter

  x = np.linspace(0, 2*np.pi, 100)
  sin = np.sin(x)
  cos = np.cos(x)

  plt.plot(x, sin, label=r'sin($x$)')
  plt.plot(x, cos, label=r'cos($x$)')
  plt.xlabel(r'$x$')
  plt.ylabel(r'$f(x)$')
  plt.legend(loc=1)
  plt.tight_layout()
  plt.show()

.. plot::

    import matplotlib.pyplot as plt
    import numpy as np
    from mpl2tex import RcParams

    RcParams(bw=True)  # set the figure parameter

    x = np.linspace(0, 2*np.pi, 100)
    sin = np.sin(x)
    cos = np.cos(x)

    plt.plot(x, sin, label=r'sin($x$)')
    plt.plot(x, cos, label=r'cos($x$)')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.legend(loc=1)
    plt.tight_layout()
    plt.show()

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
