# 题目描述
# 最近有 n 个不爽的事，每句话都有一个正整数刺痛值（心理承受力极差）。爱与愁大神想知道连续 m 个刺痛值的和的最小值是多少，但是由于业务繁忙，爱与愁大神只好请你编个程序告诉他。
#
# 输入格式
# 第一行有两个用空格隔开的整数，分别代表 n 和 m。
#
# 第 2 到第 (n+1) 行，每行一个整数，第 (i+1) 行的整数 a
#   代表第 i 件事的刺痛值 a
#
# 输出格式
# 输出一行一个整数，表示连续 m 个刺痛值的和的最小值是多少。

#暴力
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))

sum_list=[]

for i in range(0,n-m+1):
    sum=0
    for j in range(i,i+m):
        sum+=a[j]
    sum_list.append(sum)

print(min(sum_list))


#滑动窗口
n,m=map(int,input().split())
a=[int(input()) for _ in range(n)]

sum_window=sum(a[:m])
min_window=sum_window

for i in range(m,n):
    sum_window=sum_window-a[i-m]+a[i]
    if sum_window<min_window:
        min_window=sum_window

print(min_window)


# 1.要把多行数据输入到数组中可以用列表表达式
# a=[int(input()) for _ in range(n)]
