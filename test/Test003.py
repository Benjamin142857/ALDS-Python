"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 9/27/2019
    Remark      : Test003
"""

import numpy as np


def f1(x, y):
    n = len(x)
    ret = (n*np.sum(x*y) - x.sum()*y.sum()) / (n*np.sum(x**2)-x.sum()**2)
    return ret

def f2(x, y):
    ret = np.sum((x-np.average(x))*(y-np.average(y))) / (np.sum((x-np.average(x))**2))
    return ret

if __name__ == '__main__':
    x = np.array([3, 4, 5, 6, 7, 8])
    y = np.array([2, 6, 7, 4, 5, 9])
    print(f1(x, y))
    print(f2(x, y))
