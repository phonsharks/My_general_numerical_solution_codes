# Ozdeger ve ozvektorler
from numpy import *
def jacobi(a,tol): # Jacobi metodu
    n = len(a)
    maxRot = 5*(n**2)
    p = eye(n)*1.0
    for i in range(maxRot):
        aMax = 0.0
        for m in range(n-1):
            for j in range(m+1,n):
                if abs(a[m,j]) >= aMax:
                    aMax = abs(a[m,j])
                    k = m; l = j
        if aMax < tol: return diagonal(a),p
        aDiff = a[l,l] - a[k,k]
        if abs(a[k,l]) < abs(aDiff)*1.0e-36: \
           t = a[k,l]/aDiff
        else:
            phi = aDiff/(2.0*a[k,l])
            t = 1.0/(abs(phi) + sqrt(phi**2 + 1.0))
            if phi < 0.0: t = -t
        c = 1.0/sqrt(t**2 + 1.0); s = t*c
        tau = s/(1.0 + c)
        temp = a[k,l]
        a[k,l] = 0.0
        a[k,k] = a[k,k] - t*temp
        a[l,l] = a[l,l] + t*temp
        for i in range(k):
            temp = a[i,k]
            a[i,k] = temp - s*(a[i,l] + tau*temp)
            a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
        for i in range(k+1,l):
            temp = a[k,i]
            a[k,i] = temp - s*(a[i,l] + tau*a[k,i])
            a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
        for i in range(l+1,n):
            temp = a[k,i]
            a[k,i] = temp - s*(a[l,i] + tau*temp)
            a[l,i] = a[l,i] + s*(temp - tau*a[l,i])
        for i in range(n):
            temp = p[i,k]
            p[i,k] = temp - s*(p[i,l] + tau*p[i,k])
            p[i,l] = p[i,l] + s*(temp - tau*p[i,l])
    print "Cozum yok"

a = array([[ 3.0, 0.0,  -2.0],[0.0,  4.0,  0.0],[ -2.0,  0.0, 3.0]])
tol=1.0e-9
ozdeger,ozvektor= jacobi(a,tol)
print "Ozdeger", " Ozvektor"
for i in range(len(ozvektor)):
    print ozdeger[i],ozvektor[:,i]
