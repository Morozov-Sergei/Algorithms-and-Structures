#Uses python2

import sys

class ADJL():
    def __init__(self, adj):
        self.__data = adj
        self.__visited = {k:False for k in range(0, len(adj))}
        self.__postorder = {k:0 for k in range(0, len(adj))}
        self.__post = 0



    @property
    def postorder(self):
        return self.__postorder

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
            result += 'VERTEX:' + str(vertex) + ' Edges: ' + str(kv)+ ' #POST: ' + str(self.postorder[vertex]) + '\n'
            vertex+=1
        return result

    def make_reversed(self):
        newdata = [[] for _ in xrange(len(self.data))]
        for i in xrange(len(self.data)):
            v = self.data[i]
            for e in v:
                newdata[e].append(i)
        self.data = newdata

    def mark_dfs(self):
        self.postorder = {k:0 for k in range(0, len(adj))}
        for v in range(0, len(self.data)):
            if not self.visited[v]:
                self.dfs(v)
                self.__post += 1
                self.postorder[v] = self.__post

    def dfs(self, x):
        self.visited[x] = True
        for v in self.get_edges(x):
            if not self.visited[v]:
                self.dfs(v)
                self.__post += 1
                self.postorder[x] = self.__post

def acyclic(adj):
    al.mark_dfs()
    return 0

sys.stdin = file('../tests/a')
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    al = ADJL(adj)
    al.mark_dfs()
    print(al)
    #print(acyclic(al))

