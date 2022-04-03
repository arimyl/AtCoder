a, b = map(int, input().split())

ab = (a**2 + b**2)**0.5

x = a / ab
y = b / ab

print(x, y)