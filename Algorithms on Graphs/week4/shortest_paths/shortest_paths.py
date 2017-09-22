#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    prev = [None]*len(adj)
    negative_cycle = queue.Queue()

    reachable[s] = 1
    distance[s] = 0
    for ind in range(len(adj)):
        nothingChanged = True
        for u in range(len(adj)):
            for v in adj[u]:
                v_index = adj[u].index(v)
                if distance[u]!= 10**19 and distance[v] > distance[u] + cost[u][v_index]:
                    nothingChanged = False
                    distance[v] = distance[u] + cost[u][v_index]
                    prev[v] = u
                    reachable[v]=1
                    if ind == len(adj) - 1:
                        negative_cycle.put(v)
                        shortest[v]=0
        if nothingChanged:
            break

    #mark reachable
    for ind in range(len(adj)):
        if distance[ind] < 10**19:
            reachable[ind] = 1

    visited = [False] * len(adj)
    while not negative_cycle.empty():
        u=negative_cycle.get()
        visited[u]=True
        shortest[u] = 0
        for v in adj[u]:
            if visited[v] == False:
                negative_cycle.put(v)
                visited[v]=True
                shortest[v]=0

    distance[s] = 0


#sys.stdin = open('../tests/d')


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

