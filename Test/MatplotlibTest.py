import numpy as np
import matplotlib.pyplot as plt

# # 坐标轴范围
# x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# # 正余弦函数
# c, s = np.cos(x), np.sin(x)
#
# # 创建图形实例
# plt.figure(1)
# # x自变量 c因变量 画出图像
# plt.plot(x, c, color="blue")
# plt.plot(x, s, color="green", label="sin")
# plt.title('cos & sin')  # 标题
#
# # 坐标轴编辑器
# ax = plt.gca()
# # 坐标轴居中设定
# ax.spines["right"].set_color("none")
# ax.spines["top"].set_color("none")
# ax.spines["left"].set_position(("data", 0))
# ax.spines["bottom"].set_position(("data", 0))
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#            [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# # plt.xticks(np.linspace(-np.pi, np.pi, 5, endpoint=True))
# plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
#
# ax.xaxis.set_ticks_position("bottom")
# ax.yaxis.set_ticks_position("left")
#
# # 注释位置
# plt.legend(loc="upper right")
# # 网格线
# plt.grid()
# # 显示范围 x[-1, 1] y[-1, 1]
# # plt.axis([-1, 1, -1, 1])
#
# # 指定区域填充颜色
# plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="green", alpha=0.5)
#
# # 添加注释
# t = 1
# plt.plot([t, t], [0, np.cos(t)], "y")
# plt.annotate("cos(1)", xy=[t, np.cos(1)], xycoords="data", xytext=(+10, +30), textcoords="offset points"
#              , arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
#
# # 图像展示与关闭
# plt.show()
# plt.close()

# 散点图scatter
fig = plt.figure()
fig.add_subplot(3, 3, 1)

# 柱状图bar
fig.add_subplot(332)

# 饼图Pie


# 极坐标polar


# 热图heatmap
from matplotlib import cm

# 3D图
from mpl_toolkits.mplot3d import Axes3D



