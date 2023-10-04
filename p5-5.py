# Hidrojen
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
    global L,ozdeger
    f = zeros((2))
    f[0] = y[1]
    if x==0:
        f[1]=0
    else:
        f[1] = (0.25+(L*(L+1)/x-ozdeger)/x)*y[0]
    return f
L = eval(raw_input("L degerini girin (0,1,2,3,4) ="))
n=200
h=0.1
tol=1.0e-10
x0=0.0
y0=array([0.0,0.1])
ddilk=0.5
dd=ddilk
ozeski=ddilk
ozdeger=ozeski
nsayi=0
X,Y = rk4m(x0,y0,h,n)
yeski=Y[n][0]
m=len(Y)
while nsayi<3:
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
            print ("n = ", nsayi, "ozdeger = " "%.8f" % ozdeger)
            if nsayi<4:
                y1=[y1 for y1,y2 in Y]
                for i in range(len(y1)):
                    if i==0:
                        y1[0]=0
                    else:
                        y1[i]=(y1[i]/X[i])**2
                plot(X,y1)
            dd=ddilk
            ozeski=ozyeni+dd
            yeski=yyeni
show()
