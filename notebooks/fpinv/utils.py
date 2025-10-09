import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnchoredText
from matplotlib.path import Path
from scipy.spatial import ConvexHull

import pygimli as pg

def logFormat(val):
    base, exponent = ("%.2E" % val).split("E")
    return r"%s × 10$^{%d}$" % (base, int(exponent))

def NN_interpolate(inmesh, indata, outmesh, nan=99.9):
    """ Nearest neighbor interpolation. """
    outdata = []
    for pos in outmesh.cellCenters():
        cell = inmesh.findCell(pos)
        if cell:
            outdata.append(indata[cell.id()])
        else:
            outdata.append(nan)
    return np.array(outdata)


def rst_cov(mesh, cov):
    """ Simplify refraction coverage with convex hull. """
    points_all = np.column_stack((
        pg.x(mesh.cellCenters()),
        pg.y(mesh.cellCenters()),
    ))

    points = points_all[np.nonzero(cov)[0]]
    hull = ConvexHull(points)
    hull_path = Path(points[hull.vertices])

    covs = []
    for cell in mesh.cells():
        if hull_path.contains_point(points_all[cell.id()]):
            covs.append(1)
        else:
            covs.append(0)
    return np.array(covs)


def add_inner_title(ax, title, loc, size=None, c="k", frame=True, fw="semibold", borderpad=0.2, **kwargs):
    """ Add inner title to plot. """
    if size is None:
        size = dict(size=plt.rcParams['legend.fontsize'], color=c, fontweight=fw)
    else:
        size = dict(size=size, color=c, fontweight=fw)

    at = AnchoredText(title, loc=loc, prop=size, pad=0., borderpad=borderpad,
                      frameon=False, bbox_transform=ax.transAxes, **kwargs)

    ax.add_artist(at)
    return at

def set_style(fs=8, style="seaborn-ticks"):
    """ Figure cosmetics for publications. """
    from matplotlib import rcParams
    import matplotlib.pyplot as plt
    rcParams['pdf.fonttype'] = 42

    plt.style.use(style)

    plt.rcParams['font.family'] = "Roboto"
    plt.rcParams['xtick.minor.pad'] = 1
    plt.rcParams['ytick.minor.pad'] = 1

    plt.rcParams['font.weight'] = 'regular'
    plt.rcParams['font.size'] = fs
    plt.rcParams['axes.labelsize'] = fs
    plt.rcParams['axes.titlepad'] = 4
    plt.rcParams['axes.labelweight'] = 'regular'
    plt.rcParams['xtick.labelsize'] = fs
    plt.rcParams['ytick.labelsize'] = fs
    plt.rcParams['legend.fontsize'] = fs
    plt.rcParams["savefig.dpi"] = 300
    plt.rcParams["savefig.bbox"] = "tight"
    plt.rcParams["savefig.pad_inches"] = 0
    
    ####################################################################################
    
def minmax(data):
    """Return minimum and maximum of data as a 2-line string."""
    tmp = np.array(data)
    if np.isclose(tmp.min(), 0, atol=9e-3):
        Min = 0
    else:
        Min = tmp.min()
    if np.max(tmp) > 10 and np.max(tmp) < 1e4:
        return "min: %d\nmax: %d" % (Min, tmp.max())
    if np.max(tmp) > 1e4:
        return "min: %.1e\nmax: %.1e" % (Min, tmp.max())
    else:
        return "min: %.2f\nmax: %.2f" % (Min, tmp.max())    
    

# Retrieve min and max coordinates of a mesh
def limXZ(mesh):
    minZ = min(np.round(pg.y(mesh.cellCenter())))
    maxZ = max(np.round(pg.y(mesh.cellCenter())))
    minX = min(np.round(pg.x(mesh.cellCenter())))
    maxX = max(np.round(pg.x(mesh.cellCenter())))
    return minX, maxX, minZ, maxZ

    
