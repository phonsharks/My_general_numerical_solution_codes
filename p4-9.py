## Van Der Pol salinicisi
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
    f = zeros((2))
    f[0] = y[1]
    f[1] = -y[0]-1.0*(y[0]**2-1.0)*y[1]
    return f
h=0.3
n=198
t0 = 0.0
y0 = array([0.01,0.01])
T,Y = rk4m(t0,y0,h,n)
y1=[u1 for u1,u2 in Y]
y2=[z2 for z1,z2 in Y]
for i in range (n):
    print "%12.3f"% T[i], "%12.3f"% y1[i], "%12.3f"% y2[i]
plot(y1,y2)
show()
