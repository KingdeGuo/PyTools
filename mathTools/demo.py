n = int(input())

# 初始化sum和term为0和-2（第一项为-2）
sum = 0
term = 2

# 对于每一个i（1<=i<=n），计算第i项的值，并加到sum中
for i in range(1, n+1):
    sum += term
    term += 3

# 输出结果
print(sum)