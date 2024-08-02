# -*- coding: utf-8 -*-

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist.axislines import AxesZero

CURDIR = Path(__file__).resolve().parent

plt.style.use("seaborn-paper")
fig = plt.figure()
ax = fig.add_subplot(axes_class=AxesZero)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

'''
问题描述：
假设有一个跑道长100米，A在跑道起点，速度为10米/秒；B在跑道终点，速度为90米/秒，在同一时刻A、B两人开始在跑道上匀速来回跑。
请问他们前3次相遇（包含追及的情况）在跑道的什么位置，什么时间点？
'''

x = np.linspace(0, 100, 5000)
plt.xticks(range(0, 101))
plt.yticks([0, 100])
# ax.set_aspect(1)

# A的距离公式
def dis_for_A(t):
    t1 = t % 20
    if t1 < 10:
        distance = 10 * t1
    else:
        distance = 200 - 10 * t1
    # print(t, distance)
    return distance

# B的距离公式
def dis_for_B(t):
    t1 = (t * 9) % 20
    if t1 < 10:
        distance = 100 - 10 * t1
    else:
        distance = 10 * t1 - 100
    # print(t, distance)
    return distance

# f2 = -np.sin(x)
# 函数图像和导数图像
# dis_for_B(10/9)
# dis_for_B(20/9)
# exit(0)

f1 = [dis_for_A(i) for i in x]
f2 = [dis_for_B(i) for i in x]
g1, = ax.plot(x, f1, label="A")
g2, = ax.plot(x, f2, label="B")

# ax.legend(handles=[g1], bbox_to_anchor=(1, 0), loc="upper right")
ax.legend(handles=[g1, g2])
figpath = CURDIR.joinpath("AB_encounter.png")
fig.savefig(figpath, bbox_inches="tight")
plt.show()

