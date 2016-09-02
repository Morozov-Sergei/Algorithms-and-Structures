# Uses python3
import sys


def binary_search(array, target):
    lower, upper = 0, len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                return -1
            lower = x
        elif target < val:
            upper = x
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = open("input", "r").read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        pass
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')
    #print (binary_search(a, 12))

#-1 0 1 2 3 4 5 6 7 8 9 -1
