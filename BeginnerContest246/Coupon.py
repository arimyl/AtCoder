import sys

n, k, x = map(int, input().split())
a_list = list(map(int, sys.stdin.readline().split()))

remain = []
result, num = 0, 0
a_list.sort(reverse=True)
if a_list[0] <= x:
    for i in range(k):
        a_list[i] = 0
        if len(a_list) == i+1:
            break
    result = sum(a_list)
else:
    for a in a_list:
        remain.append(a%x)
        result += a
        num += a//x
    result -= min(k, num)*x
    k -= min(k, num)
    remain.sort(reverse=True)
    if k:
        if k < len(remain): 
            result -= sum(remain[:k])
        else:
            result = 0

print(result)