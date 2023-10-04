# Ozdeger ve ozvektorler
from numpy import *
a = array([[3.,0.,-2.],[0.,4.,0.],[-2.,0.,3.]])
tol=1.0e-9
ozdeger,ozvektor= jacobi(a,tol)
print "Ozdeger", " Ozvektor"
for i in range(len(ozvektor)):
    print ozdeger[i],ozvektor[:,i]
