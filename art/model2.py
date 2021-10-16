from openseespy.opensees import *


wipe()

model('basic', '-ndm', 2, '-ndf', 2)

node(1, 0.0, 0.0)
node(2, 2.0, 0.0)
node(3, 4.0, 0.0)
node(4, 6.0, 0.0)
node(5, 2.0, 2.0)
node(6, 4.0, 2.0)

mass(1,1,1)
mass(2,1,1)
mass(3,1,1)
mass(4,1,1)
mass(5,1,1)
mass(6,1,1)

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


recorder('Node', '-file', 'aaa.txt', '-node', *[2,3,5,6], '-dof', *[1,2], 'eigen 1')
nEigen = 7
nodeTags = [2,3,5,6] 
eigens = eigen(nEigen)
record()



def modelCheck(nodeTags, eigens, tol=1e-6):
    zeroEigs = []
    for e in eigens:
        if e < tol:
            zeroEigs.append(eigens.index(e))
    print("===========================================")
    print("You have {} part/parts of you structure unstable".format(len(zeroEigs)))
    print("===========================================")
    freeNodes = []
    freeDofs = []
    cnt = 1
    for e in eigens:
        if e < tol:
            for node in nodeTags:
                ev = nodeEigenvector(node, cnt)
                if abs(ev[0]) > tol or abs(ev[1]) > tol:
                    freeNodes.append(node)
                if abs(ev[0]) > tol:
                    freeDofs.append(2*node-1)
                if abs(ev[1]) > tol:
                    freeDofs.append(2*node)
        cnt += 1
    print("These degrees of freedom are linearly dependent.")
    print(freeDofs)
    print("These are the nodes which the unstable nodes are located.")
    print(freeNodes)
    print("===========================================")
    return



modelCheck(nodeTags, eigens)

