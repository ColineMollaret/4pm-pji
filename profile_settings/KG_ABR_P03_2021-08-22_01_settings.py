# Settings file for profile KG_ABR_P03_2021-08-22_01

#############################################
# to find "invlib" in the main folder
import sys, os
path = os.popen("git rev-parse --show-toplevel").read().strip("\n")
sys.path.insert(0, path)
#############################################

from fpinv import FourPhaseModel

### MESH SETTINGS ###########################
paraDX =         1  # 0.5 for 1 cell node interpolated between each sensor (0.1 for 9 cell nodes between each sensor)
paraDepth =      60   # Maximum Depth of the paraDomain mesh
paraMaxCellSize= 50   # Maximum Cell Size of the paraDomain mesh
boundary=        1    # Boundary width to be appended for domain prolongation in absolute para domain width. Values lower than 0 force the boundary to be 4 times para domain width.
paraBoundary =   1    # Offset to the parameter domain boundary in absolute sensor spacing.

### DATA ERROR LEVEL ########################
erte =  0.05   # 1 = 100 % (i.e. 0.05 = 5 %)
rste =  0.00075 # in seconds (i.e. 0.003 = 3 ms)

######### Individual INVERSION SETTINGS #########
# ERT
lame= 10
zWeighte=0.25
maxItere=15
# RST
lams= 50
zWeights=0.25
maxIters=15
# Seismic start model
vTop= 500
vBottom= 10000

########## Joint Inversion settings #########
zWeight = 0.25 # four times more smoothing in lateral direction
maxIter = 10 # maximum number of iterations
lam= 10
beta = 10000
weighting = False

# Inversion Contraint settings (to compute in the main code fr_min and fr_max
poro_min = 0.1
poro_max = 1

# Inversion Contraint settings
fr_min, fr_max = 1-poro_max, 1-poro_min
fa_min, fa_max = 0, 0.8
fi_min, fi_max = 0, 1
fw_min, fw_max = 0, 0.8

# Petrophysical settings
poro = 0.6 # start porosity (i.e. initial porosity)
phi = poro
equa = 'G' # Geometric mean model used
#equa = 'A' # Archie's law used
                     
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
rhoi=500000
rhoa=1000000
rhor=3000


# Plotting parameters
cMine, cMaxe, cMape = 1000, 1000000, "plasma_r" # ERT plot
cMins, cMaxs, cMaps = 300, 6000, "viridis_r" # Seismic plot
cMinw, cMaxw, cMapw = 0, 1, "Blues" # water
cMini, cMaxi, cMapi = 0, 1, "Purples" # ice
cMina, cMaxa, cMapa = 0, 1, "Greens" # air
cMinr, cMaxr, cMapr = 0, 1, "Oranges" # rock

##########################################
##########################################

