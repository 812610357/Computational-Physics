import numpy as np
from scipy.misc import derivative

steps=0
s=0
def NRM(fun,x0,errorArg=1e-6,m=1,procedure=False):
    '''
    # 牛顿方法（牛顿-拉弗森方法）
    ## 参数说明
        `fun`：需要求解的方程fun(x)==0
        `x0`：求解初始值
        `errorArg`：求解精度，默认为1e-6
        `m`：根的重述，默认为1
    '''
    global steps
    global s
    steps=0
    error=1
    print('        x              e(i)        e(i)/e(i-1)    e(i)/e(i-1)^2')
    while error>errorArg/2:
        x=x0-m*fun(x0)/derivative(fun,x0,dx=errorArg/2,order=7)
        error0=error
        error=np.abs(x-x0)
        if procedure==True:
            print('%16.8e%16.8e%16.8e%16.8e'%(x0,error,error/error0,error/error0**2))
        x0=x
        steps+=1
    return x0

def f(x):
    return np.exp(np.sin(x)**3)+x**6-2*x**4-x**3-1

print('r=%.6f'%NRM(f, 0.1,m=4,procedure=True),'steps=%d'%steps)