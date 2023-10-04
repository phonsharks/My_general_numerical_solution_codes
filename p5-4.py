# Kuantum salinici
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
    f[1] = (x**2-ozdeger)*y[0]
    return f
iparite = eval(raw_input("Tek durumlar icin 1, cift durumlar icin 2 girin ="))
n=200
h=0.03
tol=1.0e-9
x0=0.0
if iparite==1:
    print("Tek durumlar :")
    y0=array([0.0,1.0])
else:
    print("Cift durumlar :")
    y0=array([1.0,0.0])
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
            nozdeger=2*nsayi-iparite
            print ("n = ", nozdeger, "ozdeger = " "%.8f" % ozdeger)
            if nsayi<4:
                y1=[y1 for y1,y2 in Y]
                nn=len(X)
                yd=zeros(2*nn-1)
                xd=zeros(2*nn-1)
                for i in range(nn-1):
                        xd[i]=-X[nn-1-i]
                        xd[i+nn]=X[i+1]
                        yd[i]=(2*iparite-3)*y1[nn-1-i]
                        yd[i+nn]=y1[i+1]
                        yd[nn-1]=y1[0]
                plot(xd,yd)
            dd=ddilk
            ozeski=ozyeni+dd
            yeski=yyeni
xlim(-5.0,5.0)
show()
