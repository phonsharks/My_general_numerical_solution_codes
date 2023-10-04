#Ising
#from numpy import *
import numpy as np
from pylab import *
from math import *
def rasgele(jbasla):
    ia=211;ib=1663;ic=7875
    jbasla=(jbasla*ia+ib)%ic
    return float(jbasla)/float(ic), jbasla
def c(t,komsu):
    t=float(it+1)/4
    e4=exp(-4./t)
    e8=e4**2
    if komsu==0:
        c=0.0
    if komsu==2:
        c=e4
    if komsu==4:
        c=e8
    if komsu==-2:
        c=1./e4
    if komsu==-4:
        c=1./e8
    return c

jbasla=345;L=32;mcarlo=1000
L2=L**2
print("T ", "M ortalama", "E ortalama")
#Sicaklik dongusu. 
for it in range(20):
    t=float(it)/4

#Baslangicta rasgele bir konfigurasyon olustur. E ve M yi hesapla.
    m=0
    spin = np.zeros((L,L))
#    spin = empty(L, L)
#    spin = numpy.empty((L, L))
    for i in range(L):
        for j in range(L):
            xras,jbasla=rasgele(jbasla)
            if xras<0.5:
                spin[i,j]=1
            else:
                spin[i,j]=-1
    enerji=0
    for j in range(L):
        if j==L-1:
            iust=1
        else:
            iust=j+1
        for i in range(L):
            if i==L-1:
                isag=1
            else:
                isag=i+1
            enerji=enerji-spin[i,j]*(spin[i,iust]+spin[isag,j])

# Monte Carlo dongusu. Spinleri alt-ust et. Enerjisini kiyasla.
#Calisiyo ama hala matris boyutlarinda hata olabilir (isol,isag,...)
    m_kumula=0
    e_kumula=0
    for imc in range(mcarlo):
        for k in range(L2):
            xras,jbasla=rasgele(jbasla)
            i=int(L*xras)
            xras,jbasla=rasgele(jbasla)
            j=int(L*xras)
            if i==0:
                isol=spin[L-1,j]
            else:
                isol=spin[i-1,j]
            if i==L-1:
                isag=spin[0,j]
            else:
                isag=spin[i+1,j]
            if j==0:
                ialt=spin[i,L-1]
            else:
                ialt=spin[i,j-1]
            if j==L-1:
                iust=spin[i,0]
            else:
                iust=spin[i,j+1]
            komsu=isol+isag+iust+ialt
            delta_E=spin[i,j]*komsu
            xras,jbasla=rasgele(jbasla)
            if delta_E<=0.0:
                spin[i,j]=-spin[i,j]
                m=m+2*spin[i,j]
                enerji=enerji-2*delta_E
            elif xras<c(t,komsu):
                spin[i,j]=-spin[i,j]
                m=m+2*spin[i,j]
                enerji=enerji-2*delta_E
        e_kumula=e_kumula+enerji
        m_kumula=m_kumula+m

    sabit=1.0/float(L2*mcarlo)
    e_orta=e_kumula*sabit
    m_orta=m_kumula*sabit
    print t, "%.8f" % e_orta, "%.8f" % m_orta
    plot(t,m_orta,"ko")
show()
