# Kare kuyu
from math import *
def yarila(a,b,tol):
    if f(a)*f(b)>0.0:
        cevap=False
        print("Bu aralikta kok yok.")
        return cevap
    else:
        dx=b-a
        while(abs(dx)>tol):
            xm=(a+b)/2
            if(f(a)*f(xm))<0.0:
               b=xm
               dx=b-a
            else:
               a=xm
               dx=b-a
        return xm
def f(x):
    global r,n
    return x+asin(x/r)-n*pi/2
sabit=3.81
a=3.0
v0=50.0
r=sqrt(v0/sabit)*a
tol=1.0e-6
print "n  " , "  Enerji "
for i in range(50):
    uilk=0.001*r
    uson=0.999*r
    n=i+1
    if yarila(uilk,uson,tol)==False:
        break
    else:
        enerji=sabit* \
                (yarila(uilk,uson,tol)/a)**2
        print n, enerji
