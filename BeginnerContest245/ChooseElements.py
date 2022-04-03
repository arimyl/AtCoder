import sys
n, k = map(int, input().split())
alist = list(map(int, sys.stdin.readline().split()))
blist = list(map(int, sys.stdin.readline().split()))

# list まとめて値を入れない(参照になる)
dp = [False] * n
ep = [False] * n

dp[0] = ep[0] = True
answer = 'No'
for i in range(n - 1):
    if dp[i]:
        if abs(alist[i] - alist[i + 1]) <= k:
            dp[i + 1] = True
        if abs(alist[i] - blist[i + 1]) <= k:
            ep[i + 1] = True
    if ep[i]:
        if abs(blist[i] - alist[i + 1]) <= k:
            dp[i + 1] = True
        if abs(blist[i] - blist[i + 1]) <= k:
            ep[i + 1] = True

if dp[n-1] == True or ep[n-1] == True:
    answer = 'Yes'

print(answer)