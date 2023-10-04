# Millikan 
from pylab import *
import numpy
#from gaussPivot import *
def gausel(a,b,tol):
    n = len(b)
# i.ci sutundaki maksimum elemani bul
    s = zeros((n),dtype=float)
    for i in range(n):
        s[i] = max(abs(a[i,:]))
    for k in range(0,n-1):
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
def ekk(xData,yData,m):
    tol=1.e-6
    a = zeros((m+1,m+1))
    b = zeros(m+1)
    s = zeros(2*m+1)
    for i in range(len(xData)):
        temp = yData[i]
        for j in range(m+1):
            b[j] = b[j] + temp
            temp = temp*xData[i]
        temp = 1.0
        for j in range(2*m+1):
            s[j] = s[j] + temp
            temp = temp*xData[i]
    for i in range(m+1):
        for j in range(m+1):
            a[i,j] = s[i+j]
    return gausel(a,b,tol)

xi=[float(i) for i in range (4,19)]
yi = [6.558,8.206,9.880,11.50,13.14,14.82,16.40,18.04, \
      19.68,21.32,22.96,24.60,26.24,27.88,29.52]
n=len(yi)
m=1
polinom = zeros((n),dtype=float)
tol=1.0e-12
c = ekk(xi,yi,m)
sigma=0.03
chi2=0.0
for i in range(n):
    polinom[i]=c[1]*xi[i]+c[0]
    chi2=chi2+(yi[i]-polinom[i])**2/sigma**2
print "e = ","%.3f" % c[1],", n-m=",n-m-1,", Ki_kare = ","%.2f"%chi2
plot(xi,yi,"ko")
plot(xi,polinom)
show()
