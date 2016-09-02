# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def optimal_weight(W, wt):
    max_vals = [[0] * (W + 1) for x in range(len(wt))]
    max_vals[0] = [wt[0] if wt[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(wt)):
        for j in range(1, W + 1):
            value = max_vals[i - 1][j]
            if wt[i] <= j:
                val = (max_vals[i - 1][j - wt[i]]) + wt[i]
                if value < val:
                    value = val
                    max_vals[i][j] = value
                else:
                    max_vals[i][j] = value
            else:
                max_vals[i][j] = value
    return max_vals[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = open("input","r").read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
