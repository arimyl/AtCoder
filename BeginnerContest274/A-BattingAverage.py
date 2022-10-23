a, b = map(int, input().split())

result = str(b / a)

if len(result) > 5:
    x = result[:5]
    y = result[5:6]

    if int(y) > 4:
        ans = str(float(x) + 0.001)
    else:
        ans = x

else:
    ans = str(float(result)).ljust(5, "0")


print(ans)
