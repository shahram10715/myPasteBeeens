from openseespy.opensees import *

wipe()

model('basic', '-ndm', 2, '-ndf', 2)

node(1, 0.0, 0.0)
node(2, 2.0, 0.0)
node(3, 4.0, 0.0)
node(4, 6.0, 0.0)
node(5, 2.0, 2.0)
node(6, 4.0, 2.0)

fix(1, 1, 1)
fix(4, 1, 1)

A = 5e-3
E = 210e9

uniaxialMaterial("Elastic", 1, E)

element("Truss", 1, 1, 2, A, 1)
element("Truss", 2, 2, 3, A, 1)
element("Truss", 3, 3, 4, A, 1)
element("Truss", 4, 1, 5, A, 1)
element("Truss", 5, 2, 5, A, 1)
element("Truss", 6, 3, 6, A, 1)
element("Truss", 7, 4, 6, A, 1)
element("Truss", 8, 5, 6, A, 1)


timeSeries("Linear", 1)
pattern("Plain", 1, 1)
load(3, 0.0, -5000.0)


system("FullGeneral")  # IMPORTAN NOTICE. SET THE SYSTEM TO FULLGENERAL.
numberer("Plain")
constraints("Plain")
integrator("LoadControl", 1.0)
algorithm("Linear")
analysis("Static")
analyze(1)

# PRINT THE PARTITIONED STIFFNESS MATRIX TO A FILE
printA('-file', 'mat.txt')



