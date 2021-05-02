from sympy import *


def myinterpolate(x,y):
    x=list(x)
    y=list(y)
    if len(x) != len(y):
        print('x and y are not the same size')
        return
    l=len(x)
    k=zeros(l,l)
    for i in range(l):
        for j in range(l):
            k[i,j]=x[i]**j
    k=Inverse(k)
    k=k*(Matrix(y))
    t=symbols('t')
    tl=Matrix(ones(1,l))
    for i in range(l):
        tl[i]=t**i
    k=tl*k
    k=k[0,0]
    return k


def triangleShF(p1,p2,p3):
    a2a=p2[0]*p3[1]+p1[0]*p2[1]+p1[1]*p3[0]-p1[1]*p2[0]-p1[0]*p3[1]-p3[0]*p2[1]
    r1=[p2[0]*p3[1]-p2[1]*p3[0], p2[1]-p3[1], p3[0]-p2[0]]
    r1=[i/a2a for i in r1] 
    r2=[p3[0]*p1[1]-p1[0]*p3[1], p3[1]-p1[1], p1[0]-p3[0]]
    r2=[i/a2a for i in r2]
    r3=[p1[0]*p2[1]-p2[0]*p1[1], p1[1]-p2[1], p2[0]-p1[0]]
    r3=[i/a2a for i in r3]
    r = Matrix([[r1],[r2],[r3]])
    return r





