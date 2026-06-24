# 在一条无限长的路上，有一排无限长的路灯，编号为 1,2,3,4,…。
#
# 每一盏灯只有两种可能的状态，开或者关。如果按一下某一盏灯的开关，那么这盏灯的状态将发生改变。如果原来是开，将变成关。如果原来是关，将变成开。
#
# 在刚开始的时候，所有的灯都是关的。小明每次可以进行如下的操作：
#
# 指定两个数，a,t（a 为实数，t 为正整数）。将编号为 ⌊a⌋,⌊2×a⌋,⌊3×a⌋,…,⌊t×a⌋ 的灯的开关各按一次。其中 ⌊k⌋ 表示实数 k 的整数部分。
#
# 在小明进行了 n 次操作后，小明突然发现，这个时候只有一盏灯是开的，小明很想知道这盏灯的编号，可是这盏灯离小明太远了，小明看不清编号是多少。
#
# 幸好，小明还记得之前的 n 次操作。于是小明找到了你，你能帮他计算出这盏开着的灯的编号吗？

# 原版：
n=int(input())
is_open=[-1]*2000001
for i in range(n):
    data=input().split()
    a=float(data[0])
    t=int(data[1])
    for j in range(1,t+1):
        is_open[int(a*j)]=-is_open[int(a*j)]

print(is_open.index(max(is_open)))

# 改：
n = int(input())
ans = 0
for i in range(n):
    data = input().split()
    a = float(data[0])
    t = int(data[1])
    for j in range(1, t + 1):
        ans ^= int(a * j)

print(ans)


# 1.同一行输入不同数据类型的数就用一个列表先存起来，之后解包
# 2.遇到有一个元素与其他的不同的时候的可以用异或