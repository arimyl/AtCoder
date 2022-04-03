#encoding : utf-8
import sys

n, l = map(int, input().split())
k = int(input())
alist = list(map(int, sys.stdin.readline().split()))

alist = [0] + alist + [l]
yokan_list = [alist[i] - alist[i-1] for i in range(1, len(alist))]

def yokan_check(check_len):
    """切った羊羹の最小の長さが最大スコアとなるか
    check_len : int

    retrun
    ---------
    boolean

    """
    x = 0
    cnt = 0
    for y in yokan_list:
        x += y
        if x >= check_len:
            x = 0
            cnt += 1
    if cnt >= k + 1:
        return True
    else:
        return False 

def binary_search(ok, ng):
    """二分探索
    parameters
    ----------
    ok : int
    ng : int

    return:
    ----------
    int
    """
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if yokan_check(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search(0, l))