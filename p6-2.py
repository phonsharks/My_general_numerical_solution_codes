#  Kirchoff
from numpy import *
def gausel(a,b,tol):
    n = len(b)
# i.ci sutundaki maksimum elemani bul
    s = zeros((n),dtype=float)
    for i in range(n):
        s[i] = max(abs(a[i,:]))
    for k in range(n-1):
# a ve b nin satirlarini pivotla
        p = int(argmax(abs(a[k:n,k])/s[k:n])) + k
        if abs(a[p,k]) < tol: print('Matris tekil')
        if p != k:
            b[k,],b[p,] = copy(b[p,]),copy(b[k,])
            s[k,],s[p,] = copy(s[p,]),copy(s[k,])
            a[k,],a[p,] = copy(a[p,]),copy(a[k,])
# Pivotu sakla, a ve b sutun islemlerini yap
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                cc = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - cc*a[k,k+1:n]
                b[i] = b[i] - cc*b[k]
    if abs(a[n-1,n-1]) < tol: print('Matris tekil')
# Geri yerlestirme
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
a = array([[ 4.0,-1.0,-2.0],[-1.0,5.0,-2.0],[-2.0,-2.0,6.0]])
b = array([[0.0],[1.0], [5.0]])
tol=1.0e-6
x = gausel(a,b,tol)
for i in range(len(b[0])):
   print "x",i+1,"=",x[:,i]

