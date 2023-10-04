# LAplace denklemi
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
    f[1] = -2*y[1]/x
    return f
ra=1.0;rb=2.0;va=100.0;vb=0.0
n=100
h=(rb-ra)/n
tol=1.0e-6
dene1=1.0
dd=0.01
dene2=dene1+dd
r0=ra
for i in range(10):
    v0=array([va,dene1])
    R,V = rk4m(r0,v0,h,n)
    hata1=V[n][0]-vb
    v0=array([va,dene2])
    R,V = rk4m(r0,v0,h,n)
    hata2=V[n][0]-vb
    dhata=hata2-hata1
    if abs(dhata)<tol:
        print("Cozum bulundu")
        break
    else:
        gecici=dene2-hata2*(dene2-dene1)/dhata
        dene1=dene2
        dene2=gecici
v=[v1 for v1,v2 in V]
m = len(V)
v_tam=zeros(m,float)
for i in range(m):
    v_tam[i]=(rb-R[i])*ra*va/((rb-ra)*R[i])
    print "%10.3f"% R[i], "%12.3f"% v[i], "%12.3f"% v_tam[i]
plot(R,v,"kx",ms=10)
plot(R,v_tam,"r--",linewidth=3)
show()
