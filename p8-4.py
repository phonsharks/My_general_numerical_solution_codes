def rasgauss(jbasla):
    xd,jbasla=rasgele(jbasla)
    u=2*pi*xd
    xd,jbasla=rasgele(jbasla)
    t=-log(1.0-xd)
    return sqrt(t)*cos(u), \
           sqrt(t)*sin(u),jbasla
