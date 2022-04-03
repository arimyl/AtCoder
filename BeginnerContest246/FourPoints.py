x1, y1 = map(int ,input().split())
x2, y2 = map(int ,input().split())
x3, y3 = map(int ,input().split())

x, y = x1, y1
if x == x2:
    x = x3
elif x == x3:
    x = x2

if y == y2:
    y = y3
elif y == y3:
    y = y2

print(x, y)