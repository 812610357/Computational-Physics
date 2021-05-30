import numpy as np

def romberg(f, a, b, n=10):
    h = b - a
    R = np.zeros((n, n))
    R[0, 0] = (f(a) + f(b))*h/2

    for j in range(1, n):
        h /= 2
        R[j, 0] = R[j-1, 0]/2 + sum([f(a + (2*k+1)*h) for k in range(2**(j-1))])*h
        for k in range(0, j):
            R[j, k+1] = ((4**(k+1)*R[j, k] - R[j-1, k])) / (4**(k+1) - 1)
        if R[j-1,j-1]-R[j-2,j-2]<0.5e-10:
            return R

def f(x):
    return x/np.sqrt(x**2+9)

I=romberg(f,0,4)
print('I =',I)
print('e =',np.abs(I-2))
