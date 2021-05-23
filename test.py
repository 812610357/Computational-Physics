import numpy as np

data = np.array([[0.9120, 13.7],
                 [0.9860, 15.9],
                 [1.0600, 18.5],
                 [1.1300, 21.3],
                 [1.1900, 23.5],
                 [1.2600, 27.2],
                 [1.3200, 32.7],
                 [1.3800, 36.0],
                 [1.4100, 38.6],
                 [1.4900, 43.7]])


def r(c):
    return np.array(c[0]*np.power(data[:, 0], c[1])-data[:, 1])


def Dr(c):
    return np.column_stack((np.power(data[:, 0], c[1]), c[0]*np.power(data[:, 0], c[1])*np.log(data[:, 0])))


def Levenberg_Marquardt(r, Dr, x, lamb, iter_num):
    for i in range(iter_num):
        A = Dr(x)
        ATA = A.T.dot(A)
        v = -np.linalg.inv(ATA + lamb*np.diag(np.diag(ATA))).dot(A.T).dot(r(x))
        x += v
    return x


c = np.ones(2)
x = Levenberg_Marquardt(r, Dr, c, 1, 1000)
print(x)
