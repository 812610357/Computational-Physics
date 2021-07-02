import numpy as np
import matplotlib.pyplot as plt

m = 1
q = 1
B = np.array([0, 0, 4])
r0 = np.array([-3, 3, 0])    # 初始位置
v10 = np.array([1, 2, 0.1])  # 初始速度
v20 = q*np.cross(v10, B)/m   # 初始加速度
y0 = np.append(r0, v10)

c = 2.99792458e8
epsilon = 8.854187817e-12
k = q**2/(6*np.pi*epsilon*c**3)


def f(t, x):
    x1 = x[:3]
    x2 = x[3:]
    s1 = x2
    s2 = q*np.cross(x2, B)/m
    s = np.append(s1, s2)
    return s


def RK4(f, t, h, y0):
    n = int(t/h)
    t = np.linspace(0, t, n+1)
    w = np.zeros((len(y0), n+1))
    w[:, 0] = np.array([y0])
    for i in range(n):
        s1 = f(t[i], w[:, i])
        s2 = f(t[i] + h/2, w[:, i] + s1*h/2)
        s3 = f(t[i] + h/2, w[:, i] + s2*h/2)
        s4 = f(t[i] + h, w[:, i] + s3*h)
        w[:, i+1] = w[:, i] + (s1 + 2*s2 + 2*s3 + s4)*h/6
    return t, w


t, r = RK4(f, 5, 1e-3, y0)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r[0], r[1], r[2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Path of particle')
plt.savefig('p.pdf')
plt.show()


def g(t):
    x = (-10 - 2*np.cos(4*t) + np.sin(4*t))/4
    y = (11 + np.cos(4*t) + 2*np.sin(4*t))/4
    z = 0.1*t
    return np.array([x, y, z])


r0 = g(t)
error = np.linalg.norm(r[:3]-r0, ord=2, axis=0)
plt.plot(t, error)
plt.title('Error')
plt.xlabel('t')
plt.ylabel('$||r-r_0||_2$')
plt.savefig('e.pdf')
plt.show()

print(np.min(np.linalg.norm(r[:3], ord=2, axis=0)))
