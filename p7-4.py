def splinex(xi,a,b,c,d,x):
    i=0
    while x>xi[i]:
        i=i+1
    i=i-1
    xd=x-xi[i]
    return a[i]+xd*(b[i]+xd*(c[i]+xd*d[i]))
