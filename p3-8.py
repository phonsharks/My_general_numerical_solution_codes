# Wien yasasi
from math import *
def yarila(a,b,tol):
    if f(a)*f(b)>0.0:
        print("Bu aralikta kok yok.")
    else:
        dx=b-a
        while(abs(dx)>tol):
            xm=(a+b)/2
            if(f(a)*f(xm))<0.0:
               b=xm
               dx=b-a
            else:
               a=xm
               dx=b-a
    return xm
def f(x):
    return 5.0-x-5*exp(-x)
h=6.626e-34;c=3.0e8;akb=1.38e-23
a=1.0
b=10.0
tol=1.0e-8
x=yarila(a,b,tol)
sabit=(h*c)/(akb*x)
print "Xmax = " "%.4f" % x, "Sabit = " "%.6f" % sabit
