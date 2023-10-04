# Kubik serit
def spline(xi,yi):
    a=yi[:]
    n=len(a)
    h = [0]*(n-1)
    alfa = [0]*(n-1)
# l, u, z are used in the method for solving the linear system
    l = [0]*(n+1)
    u = [0]*(n)
    z = [0]*(n+1)
    # b, c, d will be the coefficients along with a.
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
def splinex(xi,a,b,c,d,x):
    i=0
    while x>xi[i]:
        i=i+1
    i=i-1
    xd=x-xi[i]
    return a[i]+xd*(b[i]+xd*(c[i]+xd*d[i]))

xi=[0.,0.25,0.50,0.75,1.0,1.25,1.5,1.75,2.0]
yi=[0.0,0.276326,0.5205,0.711156,0.842701,\
    0.922900,0.966105,0.986672,0.995322]
a,b,c,d=spline(xi,yi)
x=1.1
print "erf(",x,") = %.6f" % splinex(xi,a,b,c,d,x)
