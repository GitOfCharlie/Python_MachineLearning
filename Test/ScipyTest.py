import numpy as np
import math


# 积分
from scipy.integrate import quad, dblquad, nquad
# 一元积分
print(quad(lambda x: np.exp(-x), 0, np.inf))
# 二元积分 第一层(第二个变量)积分上下限必须用函数表示
print(dblquad(lambda x, y: np.exp(-x*y)/x**3, 0, np.inf, lambda y: 1, lambda y: np.inf))
print(dblquad(lambda y, x: 16*x*y,  0, 0.5, lambda x: 0, lambda y: math.pow((1-4*y*y), 0.5)))  # 内层x的范围是y的函数

# n元积分


def f(x, y):
    return x*y


def bound_y():
    return [0, 0.5]


def bound_x(y):
    return [0, 1-2*y]


print(nquad(f, [bound_x, bound_y]))

# 优化器optimizer
from scipy.optimize import minimize

# 听不懂???

# 线性计算与矩阵分解
from scipy import linalg as lg
arr = np.array([[1, 2], [3, 4]])
print(lg.det(arr))
print(lg.inv(arr))

# Lu分解
print(lg.lu(arr))
