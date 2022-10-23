n = int(input())
a_list = list(map(int, input().split()))

num = 2 * n + 1
ans = [0] * num

for i in range(n):
    parent = a_list[i] - 1
    next = i + 1
    ans[2 * next - 1] = ans[parent] + 1
    ans[2 * next] = ans[parent] + 1

for a in ans:
    print(a)
