import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import *
from sklearn import metrics

path = 'data/iris.csv'
df = pd.read_csv(path, header=0, index_col=False)

# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df['name'].value_counts())

# 文本矢量化
df.loc[df['name'] == 'Iris-virginica', 'id'] = 1
df.loc[df['name'] == 'Iris-setosa', 'id'] = 2
df.loc[df['name'] == 'Iris-versicolor', 'id'] = 3
df['id'] = df['id'].astype(int)
# print(df['id'].value_counts())

xLst = ['x1', 'x2', 'x3', 'x4']
yLst = 'id'
x, y = df[xLst], df[yLst]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
# train是DataFrame类型 test是Series类型
x_test.index.name, y_test.index.name = 'id', 'id'
# print(x_train.tail())

mx = LinearRegression()
mx.fit(x_train, y_train)  # 学习
y_pred = mx.predict(x_test)
y_pred = np.rint(y_pred)  # 四舍五入
# y_predict = np.array(y_pred, dtype=int)


print(metrics.accuracy_score(y_true=y_test, y_pred=y_pred))





