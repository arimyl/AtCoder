# encoding : utf-8
import sys

h , w = map(int , input().split())
square = []
sum_row = [0] * h
sum_column = [0] * w
# print(square)

for i in range(h):
    square.append(list(map(int, sys.stdin.readline().split())))
    sum_row[i] = sum(square[i])

for i in range(w):
    for j in range(h):
        sum_column[i] += square[j][i]

for i in range(h):
    print(' '.join([str(sum_row[i] + sum_column[j] - square[i][j]) for j in range(w)]))

# h , w = map(int , input().split())
# square = [list(map(int, input().split())) for _ in range(h)]
# sum_row = []
# sum_column = []


# for i in range(h):
#     # square.append(list(map(int, sys.stdin.readline().split())))
#     sum_row.append(sum(square[i]))

# for i in range(w):
#     x = 0
#     for j in range(h):
#         x += square[j][i]
#     sum_column.append(x)

# for i in range(h):
#     print(*[sum_row[i] + sum_column[j] - square[i][j] for j in range(w)])
