#Uses python3

import sys
from heapq import heappush, heappop

class Item():
    def __init__(self, idx, distance):
        self.distance = distance
        self.idx = idx
    def __lt__(self, other):
        return self.distance < other.distance

def to_string(adj):
    result = ''
    data = {k: adj[k] for k in range(len(adj))}
    for k, v in data.items():
        result += 'VERTEX:' + str(k) + ' Edges: ' + str(v)+ '\n'
    print(result)

def distance(adj, cost, s, t):
    distance = [float('inf')]* len(adj)
    prev = [None]* len(adj)
    distance[s] = 0
    #TODO use heapq inited with first Item
    heap = list(distance)
    for _ in range(len(heap)):
        v = heap.index(min(heap))
        heap[v]=float('inf')
        #print('min', v)
        #print(heap)
        idx = 0
        for e in adj[v]:
            if distance[e]>distance[v]+cost[v][idx]:
                #print('v', v, 'e', e, 'idx', idx)
                #print(cost)
                distance[e]=distance[v]+cost[v][idx]
                #print(distance[e])
                prev[e]=v
                heap[e]=distance[e]
                # print('upd', e, distance[e])
                # print('distance', distance)
            idx += 1


    if distance[t] == float('inf'):
        return -1
    return distance[t]

#sys.stdin = open('../tests/b')
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
