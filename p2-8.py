# Gauss ve Simpson - karsilastirma
from numpy import *
def gaussq6(a,b,n):
    if n!=6:
        print("N sayisi 6 olmali !")
        return
    else:
        x=empty(6,float)
        w=empty(6,float)
        x[0] = -0.932469514203152
        x[1] = -0.661209386466265
        x[2] = -0.238619186083197
        x[3] = -x[2]
        x[4] = -x[1]
        x[5] = -x[0]
        w[0] = 0.171324492379170
        w[1] = 0.360761573048139
        w[2] = 0.467913934572691
        w[3] = w[2]
        w[4] = w[1]
        w[5] = w[0]
        s=0.0
        for i in range(n):
            x[i]=0.5*((b-a)*x[i]+b+a)
            s=s+w[i]*f(x[i])
        s=0.5*(b-a)*s
        return s
def simpson(a,b,n):
    if n<1 or a>b:
        print ("Hatali veri!")
    elif n%2==1:
        print("n sayisi cift degil!")
    else:
        h=(b-a)/float(n)
        s=f(a)+f(b)
        for i in range(1,n):
            katsayi=2*(i%2+1)
            x=a+i*h
            s=s+katsayi*f(x)
    return h*s/3.0
def f(x):
    return exp(-x)
n=6
a=0.0
b=3.0
print("Simpson = ", "%.8f" % simpson(a,b,n), "Gauss = ",  "%.8f" % gaussq6(a,b,n))
