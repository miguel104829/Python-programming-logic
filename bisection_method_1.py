from math import *

def pol(x):
    return x**3 + 4*x**2 - 10

def bisec(f, a, b, tol, n):
    i = 1
    while i <= n:
        p = a+(b-a)/2.0
        print (" Iter = " , " %03d" % i, " ; p = " , " %.14f" % p)
        if abs(f(p)) <= 1e-15 or (b-a)/2.0 < tol:
            return p
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    print (" Iteraciones agotadas: Error! ")
    return

print (" \n" +r" -- Bisecci \ ’ on funci \ ’ on pol(x): " +" \n")
bisec(pol, 1.0, 2.0, 1e-8, 100)
