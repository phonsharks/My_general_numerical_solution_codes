# Monte-Carlo integrali
def rasgele(jbasla):
    ia=211;ib=1663;ic=7875
    jbasla=(jbasla*ia+ib)%ic
    return float(jbasla)/float(ic), jbasla
def f(x):
    return x**3
jbasla=113
nmax=1000
for i in range(10):
    toplam=0.0
    for j in range(nmax):
        x,jbasla=rasgele(jbasla)
        toplam=toplam+f(x)
    aintegral=toplam/nmax
    print nmax,  "%.8f" % aintegral
    nmax=nmax+1000
