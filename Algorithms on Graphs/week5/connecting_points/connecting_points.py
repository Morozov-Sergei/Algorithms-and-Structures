#Uses python3
import sys
import math
import queue

class Item():
    def __init__(self, idx, cost):
        self.idx = idx
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost

def minimum_distance(x, y):
    def get_w(i1, i2):
        return math.sqrt((x[i1] -x[i2])**2 +(y[i1]-y[i2])**2)
    cost = [float('inf')]*len(x)
    parent = [None]*len(x)
    result = 0.
    cost[0] = 0

    que = list(cost)
    tree = []
    # for idx in range(len(x)):
    #     que.put(Item(idx,cost[idx]))

    for u in range(len(x)):
        u = que.index(min(que))
        que[u] = float('inf')
        tree.append(u)
        for v in range(len(x)):
            if v not in tree and cost[v]>get_w(u,v):
                cost[v]=get_w(u,v)
                parent[v]=u
                que[v]=cost[v]
    return sum(cost)

#sys.stdin = open('../tests/b')

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
