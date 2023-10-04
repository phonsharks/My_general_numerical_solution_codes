# Runge-Kutta yontemi
from math import *
def rk4(x0,y0,h, n):
    x=x0;y=y0;xd=[x0];yd=[y0]
    for i in range(n+1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5*h, y + 0.5*k1)
        k3 = h * f(x + 0.5*h, y + 0.5*k2)
        k4 = h * f(x + h, y + k3)
        y= y + (k1 + 2*(k2 + k3) + k4)/6.0
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
x,y=rk4(x0,y0,h,n)
y_tam=[2*exp(x[i])-x[i]-1.0 for i in range(n+1)]
print("x", "y (Runge-Kutta)", "y (Tam)")
for i in range(n+1):
    print("%.2f" % x[i],  "%.6f" % y[i],  "%.6f" % y_tam[i])
