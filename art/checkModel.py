import numpy as np

np.set_printoptions(linewidth=200)

nNodes = 6
fixes = [[1,1,1],[4,1,1]]

def getFreeDoF(fixes, nNodes):
    ndf = len(fixes[0])-1
    allDoF = list(range(1, ndf*nNodes+1))
    allDoF = set(allDoF)
    fix2 = []
    for fix in fixes:
        if fix[1] == 1:
            fix2.append(ndf*fix[0]-1)
        if fix[2] == 1:
            fix2.append(ndf*fix[0])
    fix2 = set(fix2)
    freeDoF = allDoF - fix2
    return list(freeDoF)


def checkModel(stiffMatFile, fixes, nNodes, tol=1e-6):
    freeDoF = getFreeDoF(fixes, nNodes)
    ndf = len(fixes[0])-1
    mat = np.genfromtxt(stiffMatFile)
    eig0 = list(np.linalg.eig(mat)[0])
    eig1 = np.linalg.eig(mat)[1]
    zeroEigs = []
    for e in eig0:
        if abs(e) < tol:
            zeroEigs.append(eig0.index(e))
    print("=====================================================")
    print("You have {} part/parts of you structure unstable".format(len(zeroEigs)))
    print("=====================================================")

    vcv = []
    for e in eig0:
        if abs(e) < tol:
            vcv.append(eig1[:, eig0.index(e)])
    for i1 in vcv:
        freedomIndex = []
        i1 = list(i1)
        for i2 in range(len(i1)):
            if abs(i1[i2]) > tol:
                freedomIndex.append(freeDoF[i2])
        print("These degrees of freedom are linearly dependent.")
        print(freedomIndex)
        freeNodes = np.array(freedomIndex)
        freeNodes = (freeNodes + ndf-1) // ndf
        freeNodes = list(set(list(freeNodes)))
        print("These are the nodes which the unstable nodes are located.")
        print(freeNodes)
        print("=====================================================")
    
    return


checkModel('mat.txt', fixes, nNodes)



