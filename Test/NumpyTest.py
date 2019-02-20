import numpy as np

# 2-2ndarray简介
lst = [[1, 2, 3], [4, 5, 6]]

# 创建ndarray对象
np_list = np.array(lst)
print(type(np_list))  # <class 'numpy.ndarray'>

# 定义类型
np_list = np.array(lst, dtype=np.uint)

# 属性
print(np_list.shape)  # (2,3) 2行3列
print(np_list.ndim)  # 维数，2
print(np_list.dtype)  # 类型
print(np_list.itemsize)  # 每个元素的大小，uint32占32位，4字节，输出4
print(np_list.size)  # 这个list的大小，2*3=6


# 2-3常用数组
print(np.zeros([2, 4]))  # 初始化数组，全0
print(np.ones([3, 5]))  # 全1

print(np.random.rand(2, 4))  # 生成随机数矩阵,2行4列

print(np.random.randint(1, 10, 3))  # 生成随机整数，参数1~10是范围，3是大小，即生成三个整数

print(np.random.randn(2, 4))  # 生成正态分布随机数，2行4列

print(np.random.choice([10, 20, 30]))  # 指定值里面生成随机数

print(np.random.beta(1, 10, 100))  # beta分布，1~10生成100个


# 2-4numpy操作
print(np.arange(1, 11, 2))  # 产生等差数列1到10一维数组 第三个参数是步长(公差):[1 3 5 7 9]
npList = np.arange(1, 11).reshape([2, 5])  # 可以reshape成2行5列
print(np.exp(npList))  # 指数函数效果追加到数组的每个元素
# print(np.exp2(npList))  # 指数平方
# print(np.sqrt(npList))  # 开方
# print(np.sin(npList))  # 三角函数

oneList = np.array([[[1, 2, 3, 4], [4, 5, 6, 7]],
                    [[7, 8, 9, 10], [10, 11, 12, 13]],
                    [[14, 15, 16, 17], [17, 18, 19, 20]]])
print(oneList.sum())  # 248 所有的和
print(oneList.sum(axis=0))  # 深入0层 3个元素里面每个数字对应的和
print(oneList.sum(axis=1))  # 深入1层
print(oneList.sum(axis=2))  # 深入2层
print(oneList.max())
print(oneList.max(axis=0))

l1 = np.array([1, 2, 3, 4])
l2 = np.array([2, 3, 4, 5])
print(l1 + l2)  # 加法
print(l1**2)  # 乘方
print(np.dot(l1.reshape([2, 2]), l2.reshape([2, 2])))  # 矩阵点乘

print(np.concatenate((l1, l2), axis=0))  # 矩阵转接
print(np.vstack((l1, l2)))  # 其他写法 垂直方向接
print(np.hstack((l1, l2)))  # 水平接，和concatenate效果一样

print(np.split(l1, 2)[0])  # 分离

print(np.copy(l1))  # 拷贝一份


# 2-5矩阵和线性代数
from numpy.linalg import *

print(np.eye(3))  # 单位矩阵
A = np.array([[1, 0], [0, 4]])
print(inv(A))  # 逆
print(A.transpose())  # 转置
print(det(A))  # 行列式值
print(eig(A))  # 特征值 特征向量

y = np.array([[5], [7]])
print(solve(A, y))  # 解方程 Ax = y

p = np.poly1d([2, 1, 3])  # 生成多项式
print(p)
print(type(p))  # <class 'numpy.lib.polynomial.poly1d'>
