import sys
n, m = map(int, input().split())
alist = list(map(int, sys.stdin.readline().split()))
blist = list(map(int, sys.stdin.readline().split()))
clist = list(map(int, sys.stdin.readline().split()))
dlist = list(map(int, sys.stdin.readline().split()))

answer = 'Yes'

chocos = [l for l in zip(*[alist, blist, [0] * n])]
boxes = [l for l in zip(*[clist, dlist, [1] * m])]
items = sorted(chocos + boxes, reverse=True)

flag = True
wraps = []
for item in items:
    if flag:
        if item[2]:
            wraps.append(item)
        else:
            wraps_len = len(wraps)
            if wraps_len > 0:
                for i in range(wraps_len):
                    if wraps[i][0] >= item[0] and wraps[i][1] >= item[1]:
                        del wraps[i]
                        break
                    elif i == len(wraps) - 1:
                        flag = False
            else:
                flag = False
    else:
        break
if not flag:
    answer = 'No'
print(answer)
