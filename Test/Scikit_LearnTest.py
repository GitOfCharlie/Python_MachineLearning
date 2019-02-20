# 机器学习：计算机程序如何随着经验积累提高自己的性能
# 本质是1个函数
# 不打标记 无监督学习（聚类）：植物分类
# 打标记 监督学习：判断是否是垃圾邮件（提前高速垃圾邮件模型）
# 结果是有限 离散的——分类；连续的——回归

# 监督学习算法：决策树
# 三步骤：数据预处理；数据建模；结果验证
import numpy as np
import pandas as pd

if __name__ == "__main__":
    # 预处理
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    iris = load_iris()
    print(iris)
    # 分离测试集和验证集，验证集占20%， 随机选择
    train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target
                                                                        , test_size=0.2, random_state=1)
    # 建模
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(criterion="entropy")  # 建立决策树，标准定为熵增
    clf.fit(train_data, train_target)
    y_predict = clf.predict(test_data)

    # 验证
    from sklearn import metrics
    print(metrics.accuracy_score(y_true=test_target, y_pred=y_predict))
    print(metrics.confusion_matrix(y_true=test_target, y_pred=y_predict))
    print(test_target)
    print(y_predict)

    # 输出文件
    with open("./data/tree.dot", "w") as fw:
        tree.export_graphviz(clf, out_file=fw)
