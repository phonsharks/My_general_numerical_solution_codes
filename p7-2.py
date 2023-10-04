# Lagrange interpolasyon
def lagrange(x,xi,yi):
    n=len(xi)
    px = 0.0
    # sum over points
    for i in range(n):
        terim=1.0
        for j in range(n):
            if j!=i:
                terim=terim*(x-xi[j])/(xi[i]-xi[j])
        px = px + yi[i]*terim
    return px
xi=[200.,250.,273.,300.,350.,400.]
yi=[4.13,4.04,4.01,3.98,3.94,3.92]
x=320.
print("K = %.2f" % lagrange(x,xi,yi))


