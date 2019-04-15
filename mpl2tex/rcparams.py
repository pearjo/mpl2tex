# -*- coding: utf-8 -*-
"""Update Matplotlib parameter for LaTeX export."""
import matplotlib as mpl


class RcParams():
    """Update the rcParams for LaTeX export.

    Parameters
    ----------
    width : float
        Width in relation to columnwidth e.g. ``0.5*columnwidth``.
        Default is 1.0.
    columnwidth : float
        Column width of the LaTeX document. Get the value by using
        ``\\showthe\\columnwidth`` in LaTeX.
    fontsize : float
        Font size of the LaTeX document. Default is 10.
    ratio : {float, 'gr', 'sq'}
        Aspect ratio of the figure. Optional values are 'gr' for golden
        ratio and 'sq' for square ratio. Default is 'gr'.
    serif : bool, optional
        Set all fonts serif. Default is True.
    linewidth : float
        Axes line width in pt. Default is 0.6.
    frame : float
        Line width of the figure frame in pt. Default is 0.4.
    bw : bool
        Lines will be black and the linestyle cycles through '-', '--',
        '-.' and ':'. Default is False.
    marker : bool
        The marker style cycles through all possible matplotlib markers.
        Default is False.

    """

    def __init__(self, width=1.0, columnwidth=345, fontsize=10, linewidth=0.4,
                 markeredgewidth=0.0, ratio='gr', serif=True, bw=False,
                 marker=False):
        self.rcParams = dict()
        self.width = width
        self.columnwidth = columnwidth
        self.fontsize = fontsize
        self.linewidth = linewidth
        self.markeredgewidth = markeredgewidth
        self.ratio = ratio
        self.serif = serif
        self.bw = bw
        self.marker = marker

        items = {'text.usetex': True,
                 'text.latex.unicode': True,
                 'text.latex.preamble': r'\usepackage{amsmath}',
                 'grid.linestyle': '-',
                 'grid.alpha': '0.25',
                 'grid.color': '000000',
                 'grid.linewidth': 0.2,
                 'axes.linewidth': 0.4,
                 'patch.linewidth': 0.4,
                 'ytick.direction': 'in',
                 'xtick.direction': 'in',
                 'xtick.major.width': 0.2,
                 'xtick.minor.width': 0.2,
                 'ytick.major.width': 0.2,
                 'ytick.minor.width': 0.2,
                 'figure.autolayout': True,
                 'legend.edgecolor': '0.0',
                 'legend.fancybox': False,
                 'legend.frameon': True,
                 'legend.framealpha': 1.0,
                 'font.size': self.fontsize,
                 'lines.markeredgewidth': self.markeredgewidth,
                 'lines.linewidth': self.linewidth}

        mpl.rcParams.update(mpl.rcParamsDefault)
        self.__figsize__()
        self.rcParams.update(items)

        if self.serif is True:
            self.rcParams.update({'font.family': 'serif'})

        if self.bw is True:
            self.__bw__()

        if self.marker is True:
            self.__marker__()

        mpl.rcParams.update(self.rcParams)

    def __figsize__(self):
        r"""Calculate figure size.

        Calculate the figure size for a given ratio, columnwidth
        and width. Get the columnwidth of a document with the
        command ``\\showthe\\columnwidth``.

        """
        figwidth_pt = self.columnwidth*self.width
        inches_per_pt = 1.0/72.27  # Convert pt to inches

        if self.ratio == 'gr':
            ratio = 1.61803  # Aesthetic ratio (1 + sqrt(5))/2
        elif self.ratio == 'sq':
            ratio = 1.0

        figwidth = figwidth_pt * inches_per_pt
        figheight = figwidth/ratio
        figsize = {'figure.figsize': [figwidth, figheight]}
        self.rcParams.update(figsize)

    def __bw__(self):
        """Black and white.

        Make black and white plots. All lines are black and the line style
        cycles through all line styles.

        """
        linestyle = 'cycler("linestyle", ["-", "--", "-.", ":"])'
        self.rcParams.update({'lines.color': 'k',
                              'axes.prop_cycle': linestyle})

    def __marker__(self):
        """Cycle through all matplotlib marker styles."""
        marker = r'cycler("marker", [".", ",", "o", "v", "^", "<", ">", "1", \
                                     "2", "3", "4", "8", "s", "p", "P", "*", \
                                     "h", "H", "+", "x", "X", "d", "D", "|", \
                                     "_", "TICKLEFT", "TICKRIGHT", "TICKUP", \
                                     "TICKDOWN", "CARETLEFT", "CARETRIGHT", \
                                     "CARETUP", "CARETDOWN", "CARETLEFTBASE", \
                                     "CARETRIGHTBASE", "CARETUPBASE"])'
        self.rcParams.update({'axes.prop_cycle': marker})


def rcParamsDefault():
    """Reset rcParams to default."""
    mpl.rcParams.update(mpl.rcParamsDefault)
