n = int(input())
alist = list(map(int, input().split()))

cnt = 0
for i in set(alist):
    if cnt != i:
        break
    cnt += 1
print(cnt)