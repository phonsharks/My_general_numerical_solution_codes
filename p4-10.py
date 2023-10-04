# Lorenz modelinde kaos
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
    f = zeros((3))
    f[0] = 10.*(y[1]-y[0])
    f[1] = -y[0]*y[2]+28*y[0]-y[1]
    f[2] = y[0]*y[1]-y[2]*8.0/3.0
    return f
h=0.03
n=1999
t0 = 0.0
y0 = array([1.,1.,20.])
freq = 1
T,Y = rk4m(t0,y0,h,n)
x=[x1 for x1,x2,x3 in Y]
y=[y2 for y1,y2,y3 in Y]
z=[z3 for z1,z2,z3 in Y]
for i in range (n):
    print "%8.3f"% T[i], "%12.3f"% x[i], "%12.3f"% y[i], "%12.3f"% z[i]
#Asagidaki 3 grafik komutundan birini secin
plot(x,y)
#plot(x,z)
#plot(y,z)
show()
