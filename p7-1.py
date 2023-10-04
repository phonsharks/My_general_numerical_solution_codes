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


