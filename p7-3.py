def spline(xi,yi):
    a=yi[:]
    n=len(a)
    h = [0]*(n-1)
    alfa = [0]*(n-1)
    l = [0]*(n+1)
    u = [0]*(n)
    z = [0]*(n+1)
    b = [0]*n
    c = [0]*(n+1)
    d = [0]*(n)    
    for i in range(n-1):
        h[i] = xi[i+1]-xi[i]  
    for i in range(1, n-1):
        alfa[i]=(3./h[i])*(a[i+1]-a[i])-(3./h[i-1])*(a[i]-a[i-1])
    l[0] = 1      
    u[0] = 0      
    z[0] = 0
    for i in range(1, n-1):
        l[i] = 2*(xi[i+1] - xi[i-1]) - h[i-1]*u[i-1]
        u[i] = h[i]/l[i]
        z[i] = (alfa[i] - h[i-1]*z[i-1])/l[i]
    l[n] = 1
    z[n] = 0
    c[n] = 0
    for j in range(n-2, -1, -1):      
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3.
        d[j] = (c[j+1] - c[j])/(3*h[j]) 
    return a,b,c,d
