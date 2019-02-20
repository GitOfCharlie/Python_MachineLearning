import numpy as np
import pandas as pd

# Series介绍：
# pandas中的一维数据结构,有一组索引(默认非负整数)与元素对应
s1 = pd.Series([i*2 for i in range(1, 11)])
print(s1)
print(type(s1))  # <class 'pandas.core.series.Series'>
# 可以自行指定index
s2 = pd.Series([i*2 for i in range(1, 5)], index=["A", "B", "C", "D"])
print(s2)
# 传入字典作为参数,通过指定索引方式进行筛选和排序（Rose在字典中没有key对应，对应元素NaN）
scores = {"Jack": 80, "John": 90, "Amy": 92, "Charlie": 75}
names = ["Charlie", "John", "Rose", "Jack"]
s3 = pd.Series(scores, index=names)
print(s3)
# Series元素访问,index不是整数时用整数作index也有效，以下两者等价
print(s3[1])
print(s3["John"])

print(s3[[1, 2]])  # 连续访问
# 访问index，values
s3.index = range(1, 5)
s3[s3.index] = "aaa"  # 修改所有的值
print("----------------------------------")
print(s3.values)  # <class 'numpy.ndarray'>
#  Series对象运算
s4 = pd.Series([1, 2, 3, 4])
print(s4*2)
print(s4[s4.values <= 2])  # 筛选


# DataFrame介绍
# 从2017-03-01开始连续的八天,作为index
dates = pd.date_range("20170301", periods=8)  # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
#  创建DataFrame对象，日期作为第一列的index，以A，B，C，D，E作为五个柱，内容为8行5列的随机数，打印出表格
frame = pd.DataFrame(np.random.rand(8, 5), index=dates, columns=list("ABCDE"))
print(frame)
# 另一种初始化方式
new_frame = pd.DataFrame({
    "A": 1,
    "B": pd.Timestamp("20170301"),
    "C": pd.Series(1, index=list(range(4))),
    "D": np.array([3]*4, dtype=np.float32),
    "E": pd.Categorical(["police", "student", "teacher", "doctor"])
})
print(new_frame)

# pandas基本操作，以上面frame为例
print(frame.head(3))  # 前3行
print(frame.tail(3))  # 后3行
print(frame.index)  # 打印index
print(frame.values)  # 打印内容，格式为二维数组
# print(frame.transpose)  # 转置
print(frame.describe())  # 打印表格每列数据的信息

# 排序
df = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=['c', 'a', 'b'], index=['D', 'B', 'C', 'A'])
print(df)
print(df.sort_index(axis=0, ascending=False))  # axis=0按index字段排序，False表示降序
print(df.sort_index(axis=1))  # axis=1按column字段排序，ascending默认为True升序

print(df.sort_values(by=["b"], ascending=False))  # axis默认为0，by根据某一列排序
print(df.sort_values(by=["A"], axis=1, ascending=False))  # axis=1，by根据某个index排序

# 选择（切片）
print(frame["A"])  # 选择A一列，类型为Series  所以DataFrame由一个个Series组成
print(frame[:3])  # 选择第0,1,2行
print(df["D":"C"])  # 用index也能切片

print(frame.loc[dates[0]])  # 一般情况的选择
print(frame.loc["20170301":"20170304", ["B", "D"]])  # 先index切片，再column列表

print(frame.at[dates[0], "C"])  # 具体某一个位置
print(df.at["D", 'a'])

print(frame.iloc[1:3, 2:4])  # 根据下标选择
print(frame.iloc[1, 3])  # 选择一个位置
print(frame.iat[1, 3])  # 同上
# 筛选
print(df[df.c < 6])  # c列< 6 的项筛选出来
print(df[df["c"] < 6])  # 两种写法等价
print(df[df["c"].isin([3, 9])])  # c列中的值属于列表中的项筛选出来

# Set
addSeries = pd.Series(list(range(10, 18)), index=dates)
frame["F"] = addSeries
print(frame)

frame.loc[:, ["D"]] = np.array([4]*len(frame))  # D列全部设置为4
print(frame)

# 拷贝
frame2 = frame.copy()
frame2[frame2 < 0.5] = 0
print(frame2)

# DataFrame缺失值处理
lst = np.array([[1, 2, 3], [4, np.nan, 6], [7, np.nan, 9]])
frame_nan = pd.DataFrame(lst, columns=["A", "B", "C"])
print(frame_nan)
print(frame_nan.dropna())  # 丢弃处理
print(frame_nan.fillna(value=1))  # 填充处理，value参数


# 统计整合
print(frame.mean())  # 均值，Series对象
print(frame.var())  # 方差
s = pd.Series([1, 2, 2, np.nan, 5, 7, 9, 10], index=dates)
print(s)
print(s.shift(2))  # 每个值向后移2个单位，前面的值不补足，变成NaN
print(s.diff())  # 差值，后一项减去前一项的值
print(s.value_counts())  # 统计每一个值在Series中出现的次数 结果也是Series对象
print(df.apply(np.cumsum))  # 应用函数（cumsum()为累加）
print(df.apply(lambda x: x.max() - x.min()))  # 自定义函数，极差，得到Series对象

# 表格拼接
pieces = [frame[:3], frame[-3:]]  # 要拼接的片段
print(pd.concat(pieces))  # concat拼接（concatenate）函数

frame3 = pd.DataFrame({"A": ["a", "b", "c", "b"], "B": np.array(range(0, 4))})
print(frame3)
print(frame3.groupby("A").sum())  # 把A列相同项聚合，B列对应项以sum形式结合


# 时间序列
time = pd.date_range("20170301", periods=10, freq="S")  # 10个片段，以秒为间隔单位
print(time)

# 绘图功能
# from pylab import *
# time_series = pd.Series(np.random.randn(1000), index=pd.date_range("20170301", periods=1000))
# time_series = time_series.cumsum()
# time_series.plot()
# show()

# 文件操作（引入xlrd库得到对excel文件的支持）
import xlrd
frame_from_file = pd.read_excel("./data/test.xlsx", "Sheet1")  # 读取文件 DataFrame对象
print(frame_from_file)
