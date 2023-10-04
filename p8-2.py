jbasla=18
nmax=10
for i in range(7):
    idaire=0
    for j in range(nmax):
        x,jbasla=rasgele(jbasla)
        y,jbasla=rasgele(jbasla)
        if (x**2+y**2)<=1.0:
            idaire=idaire+1
    pisayisi=4*float(idaire)/nmax
    print nmax,  "%.8f" % pisayisi
    nmax=10*nmax
