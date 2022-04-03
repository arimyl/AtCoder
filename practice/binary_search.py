# encoding : utf-8
import sys

def is_ok(mid):
    """二分探索中の判定
    parameters
    ------
    mid : int

    returns
    ------
    result : bool
    """
    if mid > 0:
        return True
    else:
        return False

def binary_search(ok, ng):
    """二分探索
    paramaters
    ------
    ok : int
    ng : int

    returns
    ------
    ok : int
    """
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
