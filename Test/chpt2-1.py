import json
from collections import defaultdict
from collections import Counter


# 取得序列内元素及其对应出现次数，形成字典
def get_count(sequence):
    counts = defaultdict(int)  # 所有值初始化为0
    for x in sequence:
        counts[x] += 1
    return counts


def top_counts(counter, n):
    value_key_pairs = [(count, tz) for tz, count in counter.items()]
    value_key_pairs.sort(reverse=True)
    return value_key_pairs[:n]


if __name__ == '__main__':
    path = 'F:\Desktop\学习\学习python\python数据分析\pydata-book\datasets\\bitly_usagov\example.txt'
    records = [json.loads(line) for line in open(path)]
    time_zones = [record['tz'] for record in records if 'tz' in record]

    time_zones_counter = get_count(time_zones)
    print(time_zones_counter)

    top_list = top_counts(time_zones_counter, 10)
    print(top_list)

    time_zones_counter_2 = Counter(time_zones)
    print(time_zones_counter_2.most_common(10))
