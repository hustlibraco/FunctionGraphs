# -*- coding: utf-8 -*-

import math

# 计算两人相遇的时间和位置
def calculate_meet_time_and_position(length, speed_a, speed_b, meet_times):
    meet_times = min(meet_times, 3)  # 最多计算前 3 次相遇
    times = []
    positions = []
    total_distance = 0
    time = 0

    for i in range(meet_times):
        relative_speed = speed_a + speed_b
        meet_time = total_distance / relative_speed
        time += meet_time

        # A 跑过的距离
        distance_a = speed_a * time

        # 计算相遇位置
        meet_position = distance_a % length

        times.append(time)
        positions.append(meet_position)

        # 更新总距离
        if distance_a < length:
            total_distance = length - distance_a
        else:
            total_distance = distance_a - length

    return times, positions

# 跑道长度
length = 100
# A 的速度
speed_a = 10
# B 的速度
speed_b = 90

times, positions = calculate_meet_time_and_position(length, speed_a, speed_b, 3)

for i in range(len(times)):
    print(f"第 {i + 1} 次相遇在跑道的 {positions[i]} 米位置，时间为 {times[i]} 秒")