def det(A):
    nr,nc = len(A),len(A[0])
# Eleme islemi
    sign=1
    for j in range(nr):
# Pivot satirini bul
        pivot_mag = abs(A[j][j])
        jpivot = j
        for ir in range(j+1, len(A)):
            this_mag = abs(A[ir][j])
            if this_mag > pivot_mag:
                jpivot = ir
                pivot_mag = this_mag
        if jpivot > j:
            A[j], A[jpivot] = A[jpivot], A[j]
            sign = -1 * sign
        pivot = A[j][j]
        if abs(pivot) < 1.0e-15:
            print "Matris tekil"
            return 0.0
# j.ci sutunun altindakileri ele
        for i in range(j+1,nr):
            alpha = -A[i][j]/pivot
            for jc in range(nc):
                A[i][jc]=A[i][jc]+alpha*A[j][jc]
# Kosegen elemanlardan determinanti kur
        d = sign
        for i in range(nr):
            d = d*A[i][i]
    return d
