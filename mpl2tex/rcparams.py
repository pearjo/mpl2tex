# -*- coding: utf-8 -*-
import matplotlib as mpl


class RcParams(object):
    r"""Generate rcParams for matplotlib.

    Updates the matplotlibrc for best export to LaTeX.

    Parameters
    ----------
    width : float
        Width in relation to columnwidth e.g. ``0.5*columnwidth``.
        Default is 1.0.
    columnwidth : float
        Column width of the LaTeX document. Get the value by using
        ``\showthe\columnwidth`` in LaTeX.
    fontsize : float
        Font size of the LaTeX document. Default is 10.
    ratio : {float, 'gr', 'sq'}
        Aspect ratio of the figure. Optional values are 'gr' for golden ratio
        and 'sq' for square ratio. Default is 'gr'.
    serif : boolean, optional
        Set all fonts serif. Default is True.
    linewidth : float
        Axes line width in pt. Default is 0.6.
    frame : float
        Line width of the figure frame in pt. Default is 0.4.
    bw : boolean
        Lines will be black and the linestyle cycles through '-', '--', '-.'
        and ':'. Default is False.
    marker : boolean
        The marker style cycles through all possible matplotlib markers.
        Default is False.

    """

    def __init__(self, width=1.0, columnwidth=345, fontsize=10, ratio='gr',
                 serif=True, bw=False, marker=False):
        self.width = width
        self.columnwidth = columnwidth
        self.fontsize = float(fontsize)
        self.ratio = ratio
        self.serif = serif
        self.linewidth = 0.4
        self.everytick = 0.2
        self.everyaxisgrid = 0.2
        self.bw = bw
        self.marker = marker

        self.rcParams = dict()
        self.__figsize__()
        self.__params__()
        mpl.rcParams.update(self.rcParams)

    def __params__(self):
        """Update rcParams.

        Update the rcParams with a dictionary ``items``.

        """
        items = {'text.usetex': True,
                 'text.latex.unicode': True,
                 'text.latex.preamble': r'\usepackage{amsmath}',
                 'grid.linestyle': '-',
                 'grid.alpha': '0.25',
                 'grid.color': '000000',
                 'grid.linewidth': self.everyaxisgrid,
                 'axes.linewidth': self.linewidth,
                 'patch.linewidth': self.linewidth,
                 'font.size': self.fontsize,
                 'axes.titlesize': self.fontsize,
                 'axes.labelsize': self.fontsize,
                 'xtick.labelsize': self.fontsize,
                 'ytick.labelsize': self.fontsize,
                 'xtick.major.width': self.everytick,
                 'xtick.minor.width': self.everytick,
                 'ytick.major.width': self.everytick,
                 'ytick.minor.width': self.everytick,
                 'figure.figsize': self.figsize,
                 'figure.autolayout': True,
                 'lines.markeredgewidth': 0.0,
                 'lines.linewidth': self.linewidth,
                 'legend.edgecolor': '0.0',
                 'legend.fancybox': False,
                 'legend.frameon': True,
                 'legend.framealpha': 1.0}

        if self.serif is True:
            self.rcParams.update({'font.family': 'serif'})

        if self.bw is True:
            self.__bw__()

        if self.marker is True:
            self.__marker__()

        self.rcParams.update(items)

    def __figsize__(self):
        r"""Calculate figure size.

        Calculate the figure size for a given ratio, columnwidth
        and width. Get the columnwidth of a document with the
        command ``\showthe\columnwidth``.

        """
        figwidth_pt = self.columnwidth*self.width
        inches_per_pt = 1.0/72.27  # Convert pt to inches

        if self.ratio == 'gr':
            ratio = 1.61803  # Aesthetic ratio (1+sqrt(5)) / 2
        elif self.ratio == 'sq':
            ratio = 1.0
        else:
            ratio = self.ratio

        figwidth = figwidth_pt * inches_per_pt
        figheight = figwidth/ratio

        self.figsize = [figwidth, figheight]

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
