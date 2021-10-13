from openseespy.opensees import *
# import numpy

p = 5e3 # N
E = 210e9 # Pa
# A = 5e-3 # m^2
A = 0.0
I = 4e-4 # m^4

wipe()
model('basic', '-ndm', 2, '-ndf', 3)

node(1, 0.0, 0.0)
node(2, 2.0, 0.0)
node(3, 2.0, 0.0)
node(4, 4.0, 0.0)

# mass(1, 1,1,1)
# mass(2, 1,1,1)
# mass(3, 1,1,1)
# mass(4, 1,1,1)

fix(1,1,1,0)
fix(4,1,1,0)

equalDOF(2,3,1,2)

geomTransf('Linear', 1)

element('elasticBeamColumn', 1, 1, 2, A, E, I, 1)
element('elasticBeamColumn', 2, 3, 4, A, E, I, 1)

# rigidLink('bar', 1,2)
# rigidLink('bar', 4,2)



# print(eigen(5))

############################################################

timeSeries("Constant", 1)
pattern('Plain', 1, 1)
load(2, 0, -p, 0)

constraints("Plain")
numberer("Plain")
integrator("LoadControl", 1)
system("FullGeneral")
algorithm("Linear")
analysis("Static")
analyze(1)

print(nodeDisp(2))

# printA('-file', 'stiffMat.txt')

# print(stiffMat)

# stiffMat = np.array(stiffMat)
# l = len(stiffMat[0])
# stiffMat = np.reshape(stiffMat, (np.sqrt(l), np.sqrt(l)))
# print(stiffMat)

