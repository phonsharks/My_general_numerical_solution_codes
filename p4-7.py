## Surtunmeli atis
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
    f[2] = -0.01*sqrt(y[2]**2+y[3]**2)*y[2]
    f[3] = -10.-0.01*sqrt(y[2]**2+y[3]**2)*y[3] 
    return f
h=0.01
n=180
t0 = 0.0
y0 = array([0.0, 0.0, 6.0, 8.])
T,Y = rk4m(t0,y0,h,n)
x=[y1 for y1,y2,y3,y4 in Y]
y=[z2 for z1,z2,z3,z4 in Y]
y_tam=(y0[2]/y0[3]-5*(x/y0[2]**2))*x
for i in range (n):
    print "%10.3f"% x[i], "%12.3f"% y[i], "%12.3f"% y_tam[i]
scatter(x,y)
scatter(x,y_tam)
xlim(0.0,10.)
ylim(-3.0,4.0)
show()
