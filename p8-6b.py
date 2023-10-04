# Rasgele yuruyus - ortalama
from numpy import *
from pylab import *
def rasgele(jbasla):
    ia=211;ib=1663;ic=7875
    jbasla=(jbasla*ia+ib)%ic
    return float(jbasla)/float(ic), jbasla
jbasla=788711;nadim=100;nyuruyen=200
adim = zeros(nadim)
yerortalama = zeros(nadim)
for j in range(nadim):
    yerortalama[j]=0.0
for i in range(nyuruyen):
    yer=0.0
    for j in range(nadim):
        xd,jbasla=rasgele(jbasla)
        if xd<0.5:
            yer=yer-1
        else:
            yer=yer+1
        yerortalama[j]=yerortalama[j]+yer**2
for j in range(nadim):
    yerortalama[j]=yerortalama[j]/nyuruyen
    adim[j]=j
plot(adim,yerortalama,"kx")
plot(adim,adim)
show()
