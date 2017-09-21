#Uses python3

import sys

def to_string(adj):
    result = ''
    data = {k: adj[k] for k in range(len(adj))}
    for k, v in data.items():
        result += 'VERTEX:' + str(k) + ' Edges: ' + str(v)+ '\n'
    print(result)

def bipartite(adj):
    #to_string(adj)
    queue = []
    colored = {k:-1 for k in range(0, len(adj))}

    #make 0 initial node
    colored[0] = 1
    queue.append(0)
    while len(queue):
        v = queue.pop(0)
        for edge in adj[v]:
            if colored[edge] == -1:
                colored[edge] = 1 - colored[v]
                queue.append(edge)
            if colored[edge] == colored[v]:
                return 0

    return 1
#sys.stdin = open('../test/b')

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
    print(bipartite(adj))
