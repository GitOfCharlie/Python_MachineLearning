from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import json
from collections import defaultdict


def get_count(sequence):
    counts = defaultdict(int)  # 所有值初始化为0
    for x in sequence:
        counts[x] += 1
    return counts


path = 'F:\Desktop\学习\学习python\python数据分析\pydata-book\datasets\\bitly_usagov\example.txt'
records = [json.loads(line) for line in open(path)]  # records是字典对象集

frame = DataFrame(records)
print(frame['tz'][:10])  # frame['tz']是一个Series对象
tz_counts = frame['tz'].value_counts()  # value_counts()方法获得时区出现次数
print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')  # fillna()函数替换缺失值，设定为Missing
clean_tz[clean_tz == ''] = 'Unknown'  # 未知值（空字符串）通过布尔型数组索引替换
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

# tz_counts[:10].plot(kind='barh', rot=0)

results = Series(x.split(" ")[0] for x in frame['a'].dropna())
print(results[:5])

cframe = frame[frame['a'].notnull()]
operating_system_counts = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
print(operating_system_counts[:5])
# print(type(operating_system_counts))

