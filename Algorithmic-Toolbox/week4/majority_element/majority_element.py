# Uses python3
import sys


def get_majority_element_rec(a, left, right):
    if left == right:
        return -1
    if len(a) == 0:
        return -1
    if left + 1 == right:
        return a[left]
    mid = left + (right - left) // 2
    lmajor = get_majority_element(a, left, mid)
    rmajor = get_majority_element(a, mid, right)
    #print (lmajor,rmajor)
    if lmajor == rmajor:
        return lmajor
    elif rmajor == -1:
        lcount = a.count(lmajor)
        if lcount > mid:
            return lmajor
    elif lmajor == -1:
        rcount = a.count(rmajor)
        if rcount > mid:
            return rmajor
    else:
        lcount = a.count(lmajor)
        rcount = a.count(rmajor)
        if lcount > mid:
            return lmajor
        elif rcount > mid:
            return rmajor
    return -1


def get_majority_element(a, left, right):
    majorNum = a[0]
    count = 1
    for item in a:
        if item == majorNum:
            count +=1
        else:
            count -= 1
            if count == 0:
                count = 1
                majorNum = item
    #print (majorNum)
    count = 0
    for item in a:
        if item == majorNum:
            count +=1
    if count > right //2:
        return majorNum
    else:
        return -1
    return majorNum

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = open ("input", "r").read()
    n, *a = list(map(int, input.split()))
    print
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
