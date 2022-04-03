a, b , c, d = map(int, input().split())
flag = True

if a > c:
    flag = False
elif a == c: 
    if b > d:
        flag = False

if flag:
    print('Takahashi')
else:
    print('Aoki')
