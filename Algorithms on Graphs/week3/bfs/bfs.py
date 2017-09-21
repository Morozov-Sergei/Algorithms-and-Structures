#Uses python3

import sys
import queue


def to_string(adj):
    result = ''
    data = {k: adj[k] for k in range(len(adj))}
    for k, v in data.items():
        result += 'VERTEX:' + str(k) + ' Edges: ' + str(v)+ '\n'
    print(result)


def distance(adj, s, t):
    queue = []
    distance = {k:-1 for k in range(0, len(adj))}

    #make s initial node
    distance[s] = 0
    queue.append(s)
    while len(queue):
        v = queue.pop(0)
        for edge in adj[v]:
            if distance[edge] == -1:
                distance[edge] = distance[v] + 1
                queue.append(edge)
                if edge == t:
                    return distance[edge]
    return -1

#sys.stdin = open('../test/a')

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
