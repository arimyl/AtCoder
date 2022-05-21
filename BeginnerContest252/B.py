import sys

n, k = tuple(map(int, sys.stdin.readline().split()))

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))


good_foods = []
point = 0
flag = 'No'

for i, v in enumerate(a_list):
    if point > v:
        continue
    elif point < v:
        point = v
        good_foods = [i]
    elif point == v:
        good_foods.append(i)

for v in b_list:
    if v-1 in good_foods:
        flag = 'Yes'
        break

print(flag)
