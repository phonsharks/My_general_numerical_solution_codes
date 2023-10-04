# Topcu atisi
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
xa=0.0;xb=1.0;ya=1.0;yb=0.36787944
n=100
h=(xb-xa)/n
tol=1.0e-6
dene1=1.0
dd=0.01
dene2=dene1+dd
x0=xa
for i in range(10):
    y0=array([ya,dene1])
    X,Y = rk4m(x0,y0,h,n)
    hata1=Y[n][0]-yb
    y0=array([ya,dene2])
    X,Y = rk4m(x0,y0,h,n)
    hata2=Y[n][0]-yb
    dhata=hata2-hata1
    if abs(dhata)<tol:
        print("Cozum bulundu")
        break
    else:
        gecici=dene2-hata2*(dene2-dene1)/dhata
        dene1=dene2
        dene2=gecici
y1=[y1 for y1,y2 in Y]
m = len(Y)
y_tam=zeros(m,float)
for i in range(m):
    y_tam[i]=exp(-X[i]**2)
    print "%10.3f"% X[i], "%12.3f"% y1[i], "%12.3f"% y_tam[i]
plot(X,y1,"k",linewidth=5)
plot(X,y_tam,"r--",linewidth=4)
show()
