# Telde kararli dalgalar
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
    global ozdeger
    f = zeros((2))
    f[0] = y[1]
    f[1] = -ozdeger**2*y[0]
    return f
n=100
h=1.0/n
tol=1.0e-8
x0=0.0
y0=array([0.0,0.1])
ddilk=0.5
dd=ddilk
ozeski=ddilk
ozdeger=ozeski
X,Y = rk4m(x0,y0,h,n)
yeski=Y[n][0]
nsayi=0
m=len(Y)
while nsayi<6:
    ozyeni=ozeski+dd
    ozdeger=ozyeni
    X,Y = rk4m(x0,y0,h,n)
    yyeni=Y[n][0]
    if yyeni*yeski>0.0:
        ozeski=ozyeni
        yeski=yyeni
    else:
        dd=dd/2.0
        if dd<tol:
            nsayi=nsayi+1
            print ("n = ", nsayi, "kn = " "%.10f" % ozdeger, "kn/pi=" "%.8f" % float(ozdeger/pi))
            if nsayi<5:
                y1=[y1 for y1,y2 in Y]
                plot(X,y1)
            dd=ddilk
            ozeski=ozyeni+dd
            yeski=yyeni
xlim(0.0,1.0)
show()
