import sys

n = int(input())

# lines = sys.stdin.readlines()
s_list = []
for i in range(n):
    s_list.append(list(map(int, list(input().rstrip('\n')))))

num_map = [[0] * 10 for _ in range(10)]

for s in s_list:
    for i, v in enumerate(s):
        num_map[v][i] += 1

val = 10*(n+1)
for n in num_map:
    v = 0
    for i in range(10):
        x = 0
        if n[i] == 0:
            continue
        
        x = (n[i]-1)*10 + i
        v = max(v, x)
    if v:
        val = min(val, v)

print(val)
