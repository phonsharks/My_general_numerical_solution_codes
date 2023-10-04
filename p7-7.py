# En kucuk kareler    
from numpy import *
from pylab import *
def gausel(a,b,tol):
    n = len(b)
# i.ci sutundaki maksimum elemani bul
    s = zeros((n),float)
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
    tol=1.0e-6
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

n=30
xi = zeros((n),float)
yi = zeros((n),float)
for i in range(n):
    xi[i]=0.1*(i+1)
    yi[i]=cos(xi[i])
c = ekk(xi,yi,4)
x = zeros((10),float)
y = zeros((10),float)
polinom = zeros((10),float)
print " x",   "    cos x", "     p(x)"
for i in range(10):
    x[i]=0.32*(i+1)
    y[i]=cos(x[i])
    m = len(c) - 1
    polinom[i] = c[m]
    for j in range(m):
        polinom[i] = polinom[i]*x[i] + c[m-j-1]
    print x[i],  "%.7f" % y[i], "%.7f" % polinom[i]
plot(x,y,"ko")
plot(x,polinom)
show()
