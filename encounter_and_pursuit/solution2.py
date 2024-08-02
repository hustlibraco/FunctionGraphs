class Runner:
    def __init__(self, speed, position, direction):
        self.speed = speed
        self.position = position
        self.direction = direction

    def move(self, time):
        self.position += self.speed * self.direction * time

# 初始化 A 和 B
A = Runner(10, 0, 1)
B = Runner(90, 100, -1)

# 记录相遇次数和相遇位置、时间
meet_count = 0
meet_positions = []
meet_times = []

# 模拟运动
time = 0

while meet_count < 3:
    distance = abs(A.position - B.position)  # 计算 A 和 B 之间的距离
    relative_speed = A.speed + B.speed  # 相对速度

    # 处理相遇情况
    if A.direction!= B.direction and distance <= relative_speed:
        meet_time = distance / relative_speed
        time += meet_time
        A.move(meet_time)
        B.move(meet_time)

    # 处理追及情况
    elif A.direction == B.direction and (B.speed > A.speed and (B.position - A.position) <= (B.speed - A.speed) or A.speed > B.speed and (A.position - B.position) <= (A.speed - B.speed)):
        catch_up_distance = min(abs(B.position - A.position), 100 - abs(B.position - A.position))
        catch_up_time = catch_up_distance / abs(B.speed - A.speed)
        time += catch_up_time
        A.move(catch_up_time)
        B.move(catch_up_time)

    # 记录相遇信息
    if distance == 0:  # 更精确的相遇判断，当距离足够近时视为相遇
        meet_count += 1
        meet_positions.append(A.position)
        meet_times.append(time)

    # 处理超出边界的情况
    if A.position >= 100:
        A.position = 100
        A.direction = -1
    elif A.position <= 0:
        A.position = 0
        A.direction = 1

    if B.position >= 100:
        B.position = 100
        B.direction = -1
    elif B.position <= 0:
        B.position = 0
        B.direction = 1

# 输出结果
for i in range(meet_count):
    print(f"第 {i + 1} 次相遇在跑道 {meet_positions[i]} 米处，时间为 {meet_times[i]} 秒")