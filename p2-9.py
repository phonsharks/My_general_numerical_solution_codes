def gaussqn(a,b,n):
    if n%2!=0:
        print("N sayisi cift olmali!")
        return
    else:
        eps=3.0e-14
        x=empty(n,float)
        w=empty(n,float)
        m=(n+1)/2
        xm=0.5*(b+a)
        xl=0.5*(b-a)
        for i in range(n):
            z=cos(pi*(i+0.75)/(n+0.5))
            z1=0.0
            while(abs(z-z1))>eps:
                  r1=1.0
                  r2=0.0
                  for j in range(n):
                      r3=r2
                      r2=r1
                      r1=((2*j+1)*z*r2-j*r3)/float(j+1)
                  rr=n*(z*r1-r2)/(z*z-1)
                  z1=z
                  z=z1-r1/rr
            x[i]=xm-xl*z
            x[n-1-i]=xm+xl*z
            w[i]=2.0*xl/((1.0-z*z)*rr*rr)
            w[n-1-i]=w[i]
    s=0.0
    for i in range(n):
        s=s+w[i]*f(x[i])
    return s
