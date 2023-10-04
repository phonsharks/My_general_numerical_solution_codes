# Adim uzunlugunun etkisi
from math import *
def f(x):
    return exp(x)
def f1(x):
    return exp(x)
h=0.1
x=1.0
for i in range(12):
    f1_simetrik=(f(x+h)-f(x-h))/(2*h)
    f1_tam=f1(x)
    fark=f1_tam-f1_simetrik
    print("%.12f" % h,"%.10f" % f1_simetrik,"%.10f" % f1_tam,"%.10f" % fark)
    h=h/10.0
