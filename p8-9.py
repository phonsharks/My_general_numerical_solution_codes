# Molekuler Dinamik
from numpy import *
from pylab import *
def rasgele(jbasla):
    ia=211;ib=1663;ic=7875
    jbasla=(jbasla*ia+ib)%ic
    return float(jbasla)/float(ic), jbasla
def f(r):
    global rz
    return (-1.0+(rz/r)**7)/r**2
akenar=10.0;alfa=2.0;natom=24;jbasla=1881
rz=2.0
x = zeros(60);y = zeros(60)
for i in range(natom):
    xd,jbasla=rasgele(jbasla)
    x[i]=akenar*xd
    yd,jbasla=rasgele(jbasla)
    y[i]=akenar*yd
for k in range(1000):
    for i in range(natom):
        fxi=0.0
        fyi=0.0
        for j in range(natom):
            if j!=i:
                rij=sqrt((x[j]-x[i])**2+(y[j]-y[i])**2)
                fxi=fxi+f(rij)*(x[i]-x[j])/rij
                fyi=fyi+f(rij)*(y[i]-y[j])/rij
        dx=alfa*fxi
        dy=alfa*fyi
        if dx<(-0.01*akenar): dx=-0.01*akenar
        if dy<(-0.01*akenar): dy=-0.01*akenar
        if dx>(0.01*akenar):  dx=0.01*akenar
        if dy>(0.01*akenar):  dy=0.01*akenar
        x[i]=x[i]+dx
        y[i]=y[i]+dy
scatter(x,y,s=700,alpha=.9,color="b")
show()
