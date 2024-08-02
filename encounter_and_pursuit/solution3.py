def find_meeting_points():
    meetings = []
    time = 0
    position_a = 0
    position_b = 100
    direction_a = 1
    direction_b = -1

    for n in range(1, 4):  # 计算前 3 次相遇
        if n % 2!= 0:  # 奇数次，相向相遇
            m = (n + 1) // 2
            time = m
            position_a = 10 * time
            meetings.append((position_a, time))
        else:  # 偶数次，同向追及
            k = n // 2
            time = 5 * k / 4
            position_a = 10 * time
            meetings.append((position_a, time))

    return meetings

meetings = find_meeting_points()
for i, (position, time) in enumerate(meetings, 1):
    print(f"第 {i} 次相遇在跑道 {position} 米处，时间为 {time} 秒")