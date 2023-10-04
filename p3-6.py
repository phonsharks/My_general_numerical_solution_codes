# Newton-Raphson Yontemi
from math import *
def newton(a,tol):
    x1=a
    x=x1-f(x1)/f1(x1)
    iter=1
    while(iter<=50):
        while(abs(x-x1)>tol):
            x1=x
            x=x1-f(x1)/f1(x1)
        if iter>50:
            print("50 iterasyonda kok bulunamadi!")
            return x
        iter=iter+1
    return x
def f(x):
    return cos(x)-x
def f1(x):
    return -sin(x)-1
a=1.0
tol=1.0e-8
x=newton(a,tol)
print("x = " "%.10f" % x)
