import sys


h, w = map(int, input().split())
lines = sys.stdin.readlines()

ans = [0] * w

for line in lines:
    for i, x in enumerate(line):
        if x == "#":
            ans[i] += 1

ans = map(str, ans)
print(" ".join(ans))
