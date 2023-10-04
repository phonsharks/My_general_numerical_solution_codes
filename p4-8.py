# Gezegen hareketi
from numpy import *
from pylab import *
def rk4m(x,y,h,n):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    for i in range(n):
        k0 = f(x,y)
        k1 = f(x + h/2.0, y + (h/2)*k0)
        k2 = f(x + h/2.0, y + (h/2)*k1)
        k3 = f(x + h, y + h*k2)
        y=y+(h/6)*(k0 + 2.0*k1 + 2.0*k2 + k3)    
        x = x + h
        X.append(x)
        Y.append(y)
    return X,Y
def f(x,y):
    f = zeros((4))
    f[0] = y[2]
    f[1] = y[3]
    f[2] = -40.0*y[0]/sqrt(y[0]**2+y[1]**2)**3
    f[3] = -40.0*y[1]/sqrt(y[0]**2+y[1]**2)**3
    return f
h=0.005
n=180
t0 = 0.0
y0 = array([1., 0.0, 0.0, 6.])
T,Y = rk4m(t0,y0,h,n)
x1=[x1 for x1,x2,x3,x4 in Y]
y1=[u2 for u1,u2,u3,u4 in Y]
y0 = array([1., 0.0, 0.0, 8.])
T,Y = rk4m(t0,y0,h,n)
x2=[w1 for w1,w2,w3,w4 in Y]
y2=[z2 for z1,z2,z3,z4 in Y]
for i in range (n):
    print "%12.3f"% x1[i], "%12.3f"% y1[i], "%12.3f"% x2[i], "%12.3f"% y2[i]
scatter(x1,y1)
scatter(x2,y2)
show()
