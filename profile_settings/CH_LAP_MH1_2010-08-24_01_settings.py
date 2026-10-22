# Settings file for profile CH_LAP_MH1_2021-08-24_01

#############################################
# to find "invlib" in the main folder
import sys, os
path = os.popen("git rev-parse --show-toplevel").read().strip("\n")
sys.path.insert(0, path)
#############################################
#############################################


### MESH SETTINGS ###########################
paraDX =         0.5  # 0.5 for 1 cell node interpolated between each sensor (0.1 for 9 cell nodes between each sensor)
paraDepth =      50   # Maximum Depth of the paraDomain mesh
paraMaxCellSize= 30   # Maximum Cell Size of the paraDomain mesh
boundary=        1    # Boundary width to be appended for domain prolongation in absolute para domain width. Values lower than 0 force the boundary to be 4 times para domain width.
paraBoundary =   1    # Offset to the parameter domain boundary in absolute sensor spacing.

### DATA ERROR LEVEL ########################
erte =  0.03   # 1 = 100 % (i.e. 0.05 = 5 %)
rste =  0.001 # in seconds (i.e. 0.003 = 3 ms)

### Individual INVERSION SETTINGS #########
# ERT
zWeighte = 0.25 # zWeight ERT  relative weight for vertical boundaries
lame =     100    # lambda ERT (~10 - 50)
maxItere = 6    # ERT Maximum number of Iteration

# RST
zWeights = 0.2 # zWeight RST  relative weight for vertical boundaries
lams =     30 # lambda RST (~50 - 200)
vTop =     200 # Top velocity for gradient starting model
vBottom =  10000 # Bottom velocity for gradient starting model (should be > 6000 to account for greater depth of the mesh)
secNodes = 2
maxIters = 10  # RST Maximum number of Iteration

### JOINT INVERSION SETTINGS ################
zWeight = 0.25 # for values < 1 more smoothing in lateral direction
maxIter = 6 # maximum number of iterations
lam =     15
beta =    10000 # default beta = 10000
equa="A"  # Archie law by default
#equa="G"  # Geometric mean model
weighting = False

# Inversion constraints
poro =     0.4 # start porosity (i.e. initial porosity)
poro_min = 0.2
poro_max = 0.7

# Inversion Contraint settings
fr_min, fr_max = 1-poro_max, 1-poro_min
fa_min, fa_max = 0, 0.6
fi_min, fi_max = 0, 1
fw_min, fw_max = 0, 0.6

# Archie parameters
rhow=100.
a=1.
m=1.5
n=2.5

# Phase VELOCITIES    
vw=1500
vi=3500
va=300
vr=6000

# Phase RESISTIVITIES    
# rhow=100
rhoi=500000
rhoa=1000000
rhor=3000

### PLOT SETTINGS ###########################
# Color scale range
cMine, cMaxe, cMape = 1000, 100000, "plasma_r" #"turbo_r" # # ERT plot
cMins, cMaxs, cMaps = 300, 6000, "viridis_r" # Seismic plot
cMinw, cMaxw, cMapw = 0, 0.5, "Blues" # water
cMini, cMaxi, cMapi = 0, 0.5, "Purples" # ice
cMina, cMaxa, cMapa = 0, 0.5, "Greens" # air
cMinr, cMaxr, cMapr = 0, 0.9, "Oranges" # rock

###############################################################################
############################# RESULTS #########################################
###############################################################################

indiv_rst_rms_ms   = 1.24
indiv_rst_chi2   = 1.53
indiv_ert_rms_perc = 3.38
indiv_ert_chi2 = 1.31  # 31/05/2025 21:25:25

indiv_rst_rms_ms   = 1.24
indiv_rst_chi2   = 1.53
indiv_ert_rms_perc = 3.25
indiv_ert_chi2 = 1.22  # 31/05/2025 21:28:20


joint_inv_chi2 = 135.78 
joint_inv_rms = 85.60
joint_ert_chi2 = 2346.33 
joint_ert_rms = 145.32
joint_rst_chi2 = 27.11 
joint_rst_rms = 19.54  # 31/05/2025 21:31:09


joint_inv_chi2 = 2.96 
joint_inv_rms = 8.90
joint_ert_chi2 = 2.71 
joint_ert_rms = 4.94
joint_rst_chi2 = 2.97 
joint_rst_rms = 10.34  # 31/05/2025 21:38:32
