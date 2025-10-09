# Settings file for synthetic profile named 3L

#############################################
# to find "invlib" in the main folder
import sys, os
path = os.popen("git rev-parse --show-toplevel").read().strip("\n")
sys.path.insert(0, path)
#############################################
#############################################
import numpy as np
import pygimli.meshtools as mt

### MODEL GEOMETRY & CHARACTERISTICS ##############
# worldx = [110, 0] #[xmax, xmin]
worldx = [68, 0] #[xmax, xmin]
worldz = [0, -25] #[zmax, zmin]
interfaces = [-4, -15] #depth of interface(s)
rm = ([5, -2.5], [5, -6], [5, -20]) #positions (x, z) of region markers for all layers
vbh = [(worldx[0]-worldx[1])/2, worldz[1]] #per default the virtual borehole is in the center of the model


# poly1 = [[25, -7], [50, -7], [50, -10], [2, -10]] #[[x1,z1], [x2,z2], ..., [xn,zn]]
senposmin = 5 #position first sensor (within worldx)
senposmax = 63 #position last sensor (within worldx)
spacing = 2 #sensor spacing in [m]
shotres = 2 #resolution of shot points: spacing*shotres (the higher, the better the result)
shots = np.arange(senposmin, senposmax, spacing*shotres, dtype="float")  


### LAYER RES/VEL (per default, the synth model is calculated from the prescribed layer RES/VEL)
#layerres = np.array([600, 2000]) # resistivity for each layer
#layervel = np.array([1000, 4500]) # velocity for each layer

#philayers = np.array([0.3, 0.2])
#filayers = np.array([0.0, 0.5])
#fwlayers = np.array([0.1, 0.01])
#falayers = philayers - fwlayers - filayers
#falayers[np.isclose(falayers, 0.0)] = 0.0
#frlayers = 1 - philayers


# Model creation based on pore fractions
philayers = np.array([0.4, 0.6, 0.2])
frlayers = 1 - philayers
fwlayers = np.array([0.2, 0.05, 0.02])
filayers = np.array([0.0, 0.55, 0.18])
falayers = philayers - fwlayers - filayers



# ERT Config
ERT_config = 'wa' #known schemes ['wa', 'wb', 'pp', 'pd', 'dd', 'slm', 'hw', 'gr']
if ERT_config == 'dd': 
    spacing=[1,3,5,7,9] #only for dd
    
# Mesh geometry
area = 15
quality = 33.8
paraDX = 0.5
paraDepth = max(abs(min(worldz)), abs(max(worldz)))
paraMaxCellSize = 15
paraBoundary = 1 #Offset to the parameter domain boundary in absolute sensor spacing
boundary = 1 #Boundary width to be appended for domain prolongation in absolute para domain width. Values lower than 0 force the boundary to be 4 times para domain width
boundaryMaxCellSize = 70
noiselevelERT = 0.025 # add relative noise to the simulated data. noiseLevel*100 in % (0.025 = 2.5%)
noiseAbsERT = 0.03
noiselevelRST = 0.03
errorRST = 0.0004    # add absolute noise to the simulated data in ms
errorERT = 0.01    # add absolute noise to the simulated data in % (default ERT: 0.01)
showmesh=0
xbound = 200
ybound = 200

erte =  errorERT
rste =  errorRST


#ERT
lamERT = 5
zWeightERT = 0.25
maxIterERT = 6
lame = lamERT
zWeighte =  zWeightERT
maxItere = maxIterERT

#RST
lamRST = 50
zWeightRST = 0.2 #not too small!
maxIterRST = 8
gradfactor = 4 #increase factor for a stronger gradient of the startmodel: vBottom=np.max(veltrue)*gradfactor
secNodes = 2
lams = lamRST
zWeights =  zWeightRST
maxIters = maxIterRST


# Phase VELOCITIES    
vw=1500
vi=3500
va=300
vr=6000

# Archie parameters
a=1
m=2
n=2

# Phase RESISTIVITIES    
rhow=100
rhoi=500000
rhoa=1000000
rhor=3000


# Color scales Plotting parameters
cMine, cMaxe, cMape = 1000, 1000000, "plasma_r" # ERT plot
cMins, cMaxs, cMaps = 300, 6000, "viridis_r" # Seismic plot
cMinw, cMaxw, cMapw = 0, 1, "Blues" # water
cMini, cMaxi, cMapi = 0, 1, "Purples" # ice
cMina, cMaxa, cMapa = 0, 1, "Greens" # air
cMinr, cMaxr, cMapr = 0, 1, "Oranges" # rock

### MESH CREATION ############################################################
world = mt.createWorld(worldz, worldx, layers=interfaces, worldMarker=False)
geom = world

# # ADD POLYGONS
# block1 =  mt.createPolygon(poly1, isClosed=True)
# geom = mt.mergePLC([world, block1])
# block2 =  mt.createPolygon(poly1, isClosed=True)
# geom = mt.mergePLC([world, block1, block2])
    
# ADD REGION MARKERS AND DEFINE LAYER RESISTIVITY / VELOCITY 
# Loop through the rm array dynamically to add region markers
for i in range(len(rm)):
    geom.addRegionMarker(rm[i], i)  

# UNSTRUCTURED MESH 
mesh = mt.createMesh(geom, area=area)
#pg.show(mesh, markers=True, showMesh=True)


### END OF SETTINGS ########

###############################################################################
###############################################################################
