# 题目描述
# 幻方是一种很神奇的 N×N 矩阵：它由数字 1,2,3,⋯⋯,N×N 构成，且每行、每列及两条对角线上的数字之和都相同。
#
# 当 N 为奇数时，我们可以通过下方法构建一个幻方：
#
# 首先将 1 写在第一行的中间。
#
# 之后，按如下方式从小到大依次填写每个数 K (K=2,3,⋯,N×N) ：
#
# 若 (K−1) 在第一行但不在最后一列，则将 K 填在最后一行， (K−1) 所在列的右一列；
# 若 (K−1) 在最后一列但不在第一行，则将 K 填在第一列， (K−1) 所在行的上一行；
# 若 (K−1) 在第一行最后一列，则将 K 填在 (K−1) 的正下方；
# 若 (K−1) 既不在第一行，也不在最后一列，如果 (K−1) 的右上方还未填数，则将 K 填在 (K−1) 的右上方，否则将 K 填在 (K−1) 的正下方。
# 现给定 N ，请按上述方法构造 N×N 的幻方。
#
# 输入格式
# 一个正整数 N，即幻方的大小。
#
# 输出格式
# 共 N 行，每行 N 个整数，即按上述方法构造出的 N×N 的幻方，相邻两个整数之间用单空格隔开。


def find_col(a, n, huanfang):
    """查找数字a所在的列"""
    for i in range(n):
        for j in range(n):
            if huanfang[i][j] == a:
                return j
    return -1


def find_row(a, n, huanfang):
    """查找数字a所在的行"""
    for i in range(n):
        for j in range(n):
            if huanfang[i][j] == a:
                return i
    return -1


n = int(input())
huanfang = [[0 for _ in range(n)] for _ in range(n)]

# 将1放在第一行中间
huanfang[0][(n - 1) // 2] = 1

# 依次填写2到n*n
for k in range(2, n * n + 1):
    row = find_row(k - 1, n, huanfang)
    col = find_col(k - 1, n, huanfang)

    # 规则1: 在第一行但不在最后一列
    if row == 0 and col != n - 1:
        huanfang[n - 1][col + 1] = k
    # 规则2: 在最后一列但不在第一行
    elif col == n - 1 and row != 0:
        huanfang[row - 1][0] = k
    # 规则3: 在第一行最后一列
    elif row == 0 and col == n - 1:
        huanfang[row + 1][col] = k
    # 规则4: 既不在第一行也不在最后一列
    else:
        # 右上方未填数
        if huanfang[row - 1][col + 1] == 0:
            huanfang[row - 1][col + 1] = k
        # 右上方已填数，填在正下方
        else:
            huanfang[row + 1][col] = k

# 输出幻方
for i in range(n):
    for j in range(n):
        print(huanfang[i][j], end=' ')
    print()


# 1.函数定义的时候二维数组只需要写名字，不需要带着后面的括号
# 2.输出二维列表的格式
# huanfang = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
#
# # ❌ 错误写法
# print(*huanfang)
# # 输出：[8, 1, 6] [3, 5, 7] [4, 9, 2]（带方括号，全在一行）
#
# print(huanfang)
# # 输出：[[8, 1, 6], [3, 5, 7], [4, 9, 2]]（带逗号和括号）
#
# # ✅ 正确写法：逐行打印
# for row in huanfang:
#     print(*row)
# # 输出：
# # 8 1 6
# # 3 5 7
# # 4 9 2
#
# # 或者用 join
# for row in huanfang:
#     print(' '.join(map(str, row)))