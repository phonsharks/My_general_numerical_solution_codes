## Av-Avci
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
    f[0] = 0.25*y[0]-0.01*y[0]*y[1]
    f[1] = -1.0*y[1]+0.01*y[0]*y[1]
    return f
h=0.5
n=200
x0 = 0.0
y0 = array([80.0, 30.0])
X,Y = rk4m(x0,y0,h,n)
y1=[y1 for y1,y2 in Y]
y2=[z2 for z1,z2 in Y]
print "t","  y[1]"," y[2]"
for i in range (n):
    print "%10.3f"% X[i], "%12.3f"% y1[i], "%12.3f"% y2[i]
scatter(y1,y2)
show()
