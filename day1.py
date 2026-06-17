w, x, h = map(int, input().split())
total = w * x * h

q = int(input())

# 注意顺序：外层是w，中间是x，内层是h（对应坐标i, j, k）
exists = [[[True for _ in range(h)] for _ in range(x)] for _ in range(w)]

for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())

    # 注意：输入坐标从1开始，需要转换为0开始的索引
    # 而且注意变量命名：输入是 x1,y1,z1，但前面已经用了x作为宽度
    # 为了清晰，这里用 i1,j1,k1 表示起始坐标
    i1, j1, k1 = x1 - 1, y1 - 1, z1 - 1
    i2, j2, k2 = x2 - 1, y2 - 1, z2 - 1

    # 遍历切割区域内的所有小方块
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            for k in range(k1, k2 + 1):
                if exists[i][j][k]:  # 如果还存在
                    exists[i][j][k] = False
                    total -= 1

print(total)
