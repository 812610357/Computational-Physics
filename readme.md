# 四川大学【计算物理】

## 课程介绍

### 教材
《数值分析》，Timothy Sauer，机械工业出版社，2014

## 课程安排

### Class1 20210308

### Class2 20210311

### Class3 20210315

1.1 二分法
1.2 不动点迭代法

### Class4 20210318

1.3 精度的极限

根的敏感公式：
$$\Delta r \thickapprox -\frac{\varepsilon g(r)}{F'(r)} $$

条件数（误差放大因子）：
$$\kappa = \left\lvert \frac{\Delta r / r}{\varepsilon g(r)/g(r)} \right\lvert = \left\lvert \frac{g(r)}{r F'(r)}\right\lvert$$

### Homework1 20210320

    P26: 习题 1.1-5
    P27: 编程 1.1-2,6
    P37: 习题 1.2-5,10
    P38: 习题 1.2-29,31
    P39: 编程 1.2-4,6
    P45: 习题 1.3-2
    P46: 编程 1.3-5

### Class5 20210322 

1.4 牛顿方法 

$$x_{i+1}= x_i - \frac{f(x_i)}{f'(x_i)}$$

$$\lim_{i \rightarrow \infty} \frac{e_{x+1}}{e_i^2} = M =\frac{f"(r)}{2f'(r)}$$

对于单重根，为二次收敛，对于多重根，为线性收敛，此时

$$\lim_{i \rightarrow \infty} \frac{e_{x+1}}{e_i} = S =\frac{m-1}{m}$$

但是也可以进行改进，达到二次收敛，对于m重根，可作

$$x_{i+1}= x_i - \frac{m f(x_i)}{f'(x_i)}$$



### Class6 20210325

1.5 割线法

$$x_{i+1}=x_i-f(x_i) \frac{x_i-x_{i-1}}{f(x_i)-f(x_{i-1})}$$