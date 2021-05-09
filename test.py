import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

steps = 0
s = 0


def FPI(fun, x0, errorArg):
    '''
    # 不动点迭代法求解函数
    ## 参数说明
    输入函数g(x)==x```fun```，求解起点```x0```，求解误差```errorArg```
    ## 举例
    >>> import numpy as np
    >>> Bisecion(np.cos, 1 ,1e-8)
    0.7390851300853067
    >>> def f(x):\n
            return (1+2*x**3)/(1+3*x**2)
    >>> Bisecion(f ,1 ,1e-8)
    0.6823278038280193
    '''
    global steps
    global s
    steps = 0
    error = 1
    while error > errorArg:
        x = fun(x0)
        error = np.abs(x-x0)
        x0 = x
        steps += 1
    s = np.abs(fun(x0)-x0)/error
    return x0


def g1(x):
    return x/3+1/(3*x**3)

np.aran
print('r=%.6f' % FPI(g1, 1.89, 1e-5), 'steps=%d' % steps)
