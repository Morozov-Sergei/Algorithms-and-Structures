#Uses python2

import sys

class ADJL():
    def __init__(self, adj):
        self.__data = adj
        self.__visited = {k:False for k in range(0, len(adj))}

    @property
    def data(self):
        return self.__data

    @property
    def visited(self):
        return self.__visited

    def get_edges(self, v):
        return self.data[v]

    def __str__(self):
        result = ''
        vertex = 0
        for kv in self.data:
            result += 'VERTEX:' + str(vertex) + ' Edges: ' + str(kv) +'\n'
            vertex+=1
        return result


def dfs(adj, x):
    adj.visited[x] = True
    for v in adj.get_edges(x):
        if not adj.visited[v]:
            dfs(adj, v)

def number_of_components(adj):
    result = 0
    for v in range(0, len(adj.data)):
        if not adj.visited[v]:
            result += 1
            dfs(adj, v)
    #write your code here
    return result
#sys.stdin = file('../tests/a')

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
    al = ADJL(adj)
    print(number_of_components(al))
