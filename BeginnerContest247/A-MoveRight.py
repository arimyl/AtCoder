s = input()

ans = ['0'] * 4

for i in range(3):
    if s[i] == '1':
        ans[i + 1] = '1'

print(''.join(ans))
