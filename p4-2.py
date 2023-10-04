# Euler yontemi
from math import *
def euler(x0,y0,h,n):
    x=x0; y=y0; xd=[x0]; yd=[y0];
    for i in range(n+1):
        y = y + h*f(x,y)
        yd.append(y)
        x=x+h
        xd.append(x)
    return(xd,yd)
def f(x,y):
    return x+y
n=10
h=0.1
x0=0.0
y0=1.0
x,y=euler(x0,y0,h,n)
y_tam=[2*exp(x[i])-x[i]-1.0 for i \
       in range(n+1)]
print " x", "  y (Euler)", "y (Tam)"
for i in range(n+1):
    print "%.2f" % x[i], "%.6f" % y[i], \
          "%.6f" % y_tam[i]
