
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

def NRM(fun,x0,errorArg=0.5e-6,m=1):
    '''
    # 牛顿方法（牛顿-拉弗森方法）
    ## 参数说明
        `fun`：需要求解的方程fun(x)==0
        `x0`：求解初始值
        `errorArg`：求解精度，默认为1e-6
        `m`：根的重述，默认为1
    '''
    error=1
    while error>2*errorArg:
        x=x0-fun(x0)/derivative(fun,x0,dx=errorArg)
        error=np.abs(x-x0)
        x0=x
    return x0


def f(x):
    return 27*x**3+54*x**2+36*x+8

print(NRM(f,0))