def judge(goal: int, len_list: int) -> bool:
    # 線分計算
    S = set()
    S.add(0)
    for v in len_list:
        T = set()
        for s in S:
            T.add(s + v)
            T.add(s - v)
        S = T

    if goal in S:
        return True
    else:
        return False


n, x, y = map(int, input().split())
a_list = list(map(int, input().split()))

ax = [a_list[i] for i in range(2, n, 2)]
ay = [a_list[i] for i in range(1, n, 2)]

if judge(x - a_list[0], ax) and judge(y, ay):
    print("Yes")
else:
    print("No")
