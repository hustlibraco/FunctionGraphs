# -*- coding: utf-8 -*-

import scipy.optimize as opt

# A的距离公式
def dis_for_A(t):
    t1 = t % 20
    if t1 < 10:
        distance = 10 * t1
    else:
        distance = 200 - 10 * t1
    return distance

# B的距离公式
def dis_for_B(t):
    t1 = (t * 9) % 20
    if t1 < 10:
        distance = 100 - 10 * t1
    else:
        distance = 10 * t1 - 100
    return distance

def intersection(x):
    return dis_for_A(x) - dis_for_B(x)

# 使用scipy.optimize库中的fsolve函数求解交点
result = opt.fsolve(intersection, 0)
print(result)
