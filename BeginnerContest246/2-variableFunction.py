n = int(input())

def calculate(a, b):
    return (a**2 + b**2)*(a + b)

a = 0
b = 10 ** 6
min_x = 10 ** 18


while a <= b:
    x = calculate(a, b)

    if x >= n:
        min_x = min(min_x, x)
        b -= 1
    else:
        a += 1
print(min_x)
