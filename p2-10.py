# Sarkac
from math import *
def strapez(a,b,n):
    if n<1 or a>b:
        print("Hatali veri!")
    else:
        h=(b-a)/n
        s=0.5*(f(a)+f(b))
        for i in range(1,n):
            x=a+i*h
            s=s+f(x)
        return h*s
def f(x):
    global genlik
    return 1.0/sqrt(1.0-(sin(genlik/2)*sin(x))**2)
a=0.0
g=9.8
L=1.0
b=pi/2
t_yaklasik=2*pi*sqrt(L/g)
n=200
for i in range(13):
    genlik=5*i*pi/180.0
    t_tam=4*sqrt(L/g)*strapez(a,b,n)
    print("%.1f" % float(genlik*180/pi),"%.6f" % t_yaklasik, "%.6f" % t_tam)
