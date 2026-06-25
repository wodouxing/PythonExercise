# 给出一个不大于 9 的正整数 n，输出 n×n 的蛇形方阵。
#
# 从左上角填上 1 开始，顺时针方向依次填入数字，如同样例所示。注意每个数字有都会占用 3 个字符，前面使用空格补齐。
#
# 输入格式
# 输入一个正整数 n，含义如题所述。
#
# 输出格式
# 输出符合题目要求的蛇形矩阵。

n = int(input())

a = [[0] * n for _ in range(n)]

# 定义四个方向：右、下、左、上
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_direction = 0
# 起始位置
row, col = 0, 0

# 填充数字
for i in range(1, n * n + 1):
    a[row][col] = i

    # 计算下一个位置
    next_row = row + directions[current_direction][0]
    next_col = col + directions[current_direction][1]

    # 判断是否需要改变方向
    # 条件：越界或该位置已经被填充
    if (next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or a[next_row][next_col] != 0):
        # 改变方向（顺时针旋转）
        current_direction = (current_direction + 1) % 4
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]

    row = next_row
    col = next_col

# 输出结果，每个数字占3个字符宽度
for i in range(n):
    for j in range(n):
        print(f"{a[i][j]:3d}", end="")
    print()

# 1.通过定义方向来进行转向，而且方向的定义直接以索引的变化为标准
# 2.当状态在几个里面循环之中可以用加一后取余来操作