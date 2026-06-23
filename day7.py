x,y,z=map(int,input().split())
max_sum=x+y+z
cishu=[0]*(max_sum+1)
sum=0
for i in range(1,x+1):
    for j in range(1,y+1):
        for m in range(1,z+1):
            sum=i+j+m
            cishu[sum]+=1
            sum=0

print(cishu.index(max(cishu)))



# 1.变量不要覆盖系统函数名，如把变量命名为max
# 2.列表要初始化才能才能使用用索引
# cishu=[0]*(max_sum+1)
