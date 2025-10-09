# Settings file for profile CH_DOL_V01_2026-08-11_01

#############################################
# to find "fpinv" in the main folder
import sys, os
path = os.popen("git rev-parse --show-toplevel").read().strip("\n")
sys.path.insert(0, path)
#############################################

from fpinv import FourPhaseModel

### MESH SETTINGS ###########################

paraDX =         1  # 0.5 for 1 cell node interpolated between each sensor (0.1 for 9 cell nodes between each sensor)
paraDepth =      60   # Maximum Depth of the paraDomain mesh
paraMaxCellSize= 60   # Maximum Cell Size of the paraDomain mesh
boundary=        1    # Boundary width to be appended for domain prolongation in absolute para domain width. Values lower than 0 force the boundary to be 4 times para domain width.
paraBoundary =   1    # Offset to the parameter domain boundary in absolute sensor spacing.

### DATA ERROR LEVEL ########################
erte =  0.013   # 1 = 100 % (i.e. 0.05 = 5 %)
rste =  0.0007 # in seconds (i.e. 0.003 = 3 ms)


### Individual INVERSION SETTINGS #########
# ERT individal inversion parameters
lame= 5 
zWeighte=0.5 # zWeight =0.25 means four times more smoothing in lateral direction
maxItere=10

# RST individal inversion parameters
lams= 50
zWeights=0.5 # zWeight =0.25 means four times more smoothing in lateral direction
maxIters=10
# Velocity Start model
vTop= 300
vBottom= 7000



maxIter = 20 # maximum number of iterations


# Parameters by default
poro_min, poro, poro_max = 0, 0.6, 1   # min porosity,  start porosity model, max porosity
phi = poro
#fpm = FourPhaseModel(phi=poro, va=300., vi=3500., vw=1500, m=1.4, n=2.4, rhow=60, vr=7500)

# Inversion Contraint settings
fr_min, fr_max = 1-poro_max, 1-poro_min
fa_min, fa_max = 0, 0.8
fi_min, fi_max = 0, 1
fw_min, fw_max = 0, 0.8

m, n = 2, 2  # Archie parameter
lam, beta = 12, 10000 # 10, 5000 Regularization parameters
zWeight = 0.1
equa="G" # Archie law by default
rhow = float(100) # pore water resistivity (ohmm) default value
weighting = False

epsilon = 0.1  # default value
b = 0.001 # default value

#####
fix_poro = False
fix_water = False
fix_air = False
fix_ice = False
#fix_ice = vec_active_layer

constrained = False # True

# Phase VELOCITIES    
vw=1500
vi=3500
va=300
vr=6000

# Phase RESISTIVITIES    
rhow=100
rhoi=500000
rhoa=1000000
rhor=10000




### PLOT SETTINGS ###########################
# Color scale range
cMine, cMaxe, cMape = 1000, 1000000, "plasma_r" #"turbo_r" # # ERT plot
cMins, cMaxs, cMaps = 300, 5000, "viridis_r" # Seismic plot
cMinw, cMaxw, cMapw = 0, 0.5, "Blues" # water
cMini, cMaxi, cMapi = 0, 0.5, "Purples" # ice
cMina, cMaxa, cMapa = 0, 0.5, "Greens" # air
cMinr, cMaxr, cMapr = 0, 0.9, "Oranges" # rock

###########################
###########################

