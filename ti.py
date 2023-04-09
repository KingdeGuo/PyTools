'''

给定一个正整数x，请找出一个尽可能短的仅含正整数的数组 A 使得 A 恰好有x对 i,j满足 Ai> Aj。
如果存在多个这样的数组，请输出宇典序最小的那个。

[输入格式]
输入一行包含一个整数表示，。

[输出格式]
输出两行。第一行包含一个整数”，表示所求出的数组长度。第二行包含n 个整数 A，相邻整数之间使用一个空格分隔，依次表示数组中的每个数。

样例输入
3
样例输出
3
3 2 1
'''

x = int(input())
ans = []
for i in range(x, 0, -1):
    if len(ans) < x:
        ans.append(i)
    else:
        ans[i % x] += i
print(len(ans))
print(' '.join(map(str, ans)))