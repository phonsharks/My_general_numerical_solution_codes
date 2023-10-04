# Sayisal turevde hata payi
from math import *
def f(x):
    return sin(x)
a=1.0
h=0.1
for i in range(14):
    f1=(f(a+h)-f(a))/h
    print("%.12f" % h,"%.10f" % \
        f1,"%.10f" % float(cos(a)-f1))
    h=h/10.0
