# Settings file for profile CH_COR_V01_2007-07-13_01

#############################################
# to find "invlib" in the main folder
import sys, os
path = os.popen("git rev-parse --show-toplevel").read().strip("\n")
sys.path.insert(0, path)
#############################################

from fpinv import FourPhaseModel

### MESH SETTINGS ###########################
paraDX =         0.25  # 0.5 for 1 cell node interpolated between each sensor (0.25 for 3 cell nodes between each sensor)
paraDepth =      50   # Maximum Depth of the paraDomain mesh
paraMaxCellSize= 20   # Maximum Cell Size of the paraDomain mesh
boundary=        1    # Boundary width to be appended for domain prolongation in absolute para domain width. Values lower than 0 force the boundary to be 4 times para domain width.
paraBoundary =   1    # Offset to the parameter domain boundary in absolute sensor spacing.

### DATA ERROR LEVEL ########################
erte =  0.08   # 1 = 100 % (i.e. 0.05 = 5 %)
rste =  0.0015 # in seconds (i.e. 0.003 = 3 ms)

###### Individual INVERSION SETTINGS #################################
# ERT individal inversion parameters
lame= 5
zWeighte=0.5
maxItere=15

# RST individal inversion parameters
lams= 5
zWeights=0.5
maxIters=15
# Velocity Start model
vTop= 500
vBottom= 7000

####### Joint Inversion settings ################################################
zWeight = 1 # four times more smoothing in lateral direction
maxIter = 10 # maximum number of iterations
lam= 10



# Inversion Contraint settings
fr_min = 0
fr_max = 1

# Range contraint
fwmin, fwmax= 0, 1
fimin, fimax= 0, 1
famin, famax= 0, 1
frmin, frmax= 0, 1

#####
fix_poro = False
fix_water = False
fix_air = False
fix_ice = False

constrained = False


# Phase VELOCITIES    
vw=1500
vi=3500
va=300
vr=6000

# Archie parameter
a=1
m=2
n=2

# Phase RESISTIVITIES    
rhow=100
rhoi=100000
rhoa=1000000
rhor=5000

# Petrophysical settings
poro_min, poro, poro_max = 0, 0.6, 1   # min porosity,  start porosity model, max porosity 
fpm = FourPhaseModel(phi=poro, va=va, vi=vi, vw=vw, m=m, n=n, rhow=rhow, vr=vr)

# JOINT INVERSION SETTINGS
lam, beta = 10, 5000 # Regularization parameters
zWeight = 0.2 # fifth times more smoothing in lateral direction
weighting = False
#equa="A" # Archie law by default
equa="G" # Geometric mean model
epsilon = 0.1  # default value
b = 0.01 # default value   # 0.001

# JOINT INVERSION CONSTRAINT SETTINGS
fr_min, fr_max = 1-poro_max, 1-poro_min
fa_min, fa_max = 0, 0.8
fi_min, fi_max = 0, 1
fw_min, fw_max = 0, 0.8




### PLOT SETTINGS ###########################
# Color scale range
cMine, cMaxe, cMape = 1000, 1000000, "plasma_r" #"turbo_r" # # ERT plot
cMins, cMaxs, cMaps = 300, 5000, "viridis_r" # Seismic plot
cMinw, cMaxw, cMapw = 0, 0.5, "Blues" # water
cMini, cMaxi, cMapi = 0, 0.5, "Purples" # ice
cMina, cMaxa, cMapa = 0, 0.5, "Greens" # air
cMinr, cMaxr, cMapr = 0, 0.9, "Oranges" # rock


###############################################################################
############################# RESULTS #########################################
###############################################################################

indiv_ert_rms = 13.04
indiv_rst_rms = 32.59  # 15/11/2023 14:52:23

indiv_rst_rms_ms   = 1.50
indiv_rst_chi2   = 1.00
indiv_ert_rms_perc = 8.02
indiv_ert_chi2 = 0.98  # 14/05/2025 14:53:43

indiv_rst_rms_ms   = 1.48
indiv_rst_chi2   = 0.98
indiv_ert_rms_perc = 8.02
indiv_ert_chi2 = 0.98  # 14/05/2025 15:06:58
