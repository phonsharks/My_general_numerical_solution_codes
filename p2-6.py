# Trapez ve Simpson - karsilastirma
from numpy import *
def trapez(a,b,n):
    if n<1 or a>b:
        print("Hatali veri!")
    else:
        h=(b-a)/n
        s=0.5*(f(a)+f(b))
        for i in range(1,n):
            x=a+i*h
            s=s+f(x)
        return h*s
def simpson(a,b,n):
    if n<1 or a>b:
        print("Hatali veri!")
    elif n%2==1:
        print("n cift degil!")
    else:
        h=(b-a)/n
        s=f(a)+f(b)
        for i in range(1,n):
            katsayi=2*(i%2+1)
            x=a+i*h
            s=s+katsayi*f(x)
    return h*s/3.0
def f(x):
    return exp(x)
a=0.0
b=1.0
stam=f(1.0)-1.0
n=4
print "N", "Trapez hatasi", "Simpson hatasi"
for i in range(6):
    print n, "%.8f" % float(trapez(a,b,n)-stam), "%.8f" % float(simpson(a,b,n)-stam)
    n=n+4
