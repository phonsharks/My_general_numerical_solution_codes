# Rasgele yuruyus
import numpy as np
from pylab import *
from math import *
def rasgele(jbasla):
    ia=211;ib=1663;ic=7875
    jbasla=(jbasla*ia+ib)%ic
    return float(jbasla)/float(ic), jbasla

jbasla=37;nadim=80
adim = np.zeros(nadim+1)
yer = np.zeros(nadim+1)
adim[0]=1.0
yer[0]=0.0
for j in range(nadim):
    adim[j+1]=j+1
    xd,jbasla=rasgele(jbasla)
    if xd<0.5:
        yer[j+1]=yer[j]-1
    else:
        yer[j+1]=yer[j]+1
plot(yer,adim,"ko")
plot(yer,adim)
x=[0.0,0.0]
y=[0.0,50.0]
plot([0.0,0.0],[0.0,50.0],"r--") #Direk
show()
