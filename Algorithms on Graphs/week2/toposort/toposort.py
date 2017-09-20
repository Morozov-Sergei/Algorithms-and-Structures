#Uses python2


import sys
class ADJL():
    def __init__(self, adj):
        self.__data = {k: adj[k] for k in xrange(len(adj))}
        self.__visited = {k:False for k in range(0, len(adj))}
        self.__postorder = {k:0 for k in range(0, len(adj))}
        self.__post = 0

    @property
    def max_post(self):
        idx, val = self.postorder.items()[0]
        for k, v in self.postorder.items():
            if v > val:
                idx = k
                val = v
        return idx, val

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
        for k, v in self.data.items():
            result += 'VERTEX:' + str(k) + ' Edges: ' + str(v)+ ' #POST: ' + str(self.postorder[k]) + '\n'
        return result

    def make_reversed(self):
        newdata = {k:[] for k in xrange(len(self.data.keys()))}
        for i, v in self.data.items():
            for e in v:
                newdata[e].append(i)
        self.data = newdata

    def mark_dfs(self):
        self.postorder = {k:0 for k in self.data.keys()}
        self.visited = {k:False for k in self.data.keys()}
        for v in self.data.keys():
            if not self.visited[v]:
                self.dfs(v)
                self.__post += 1
                self.postorder[v] = self.__post
    def dfs(self, x):
        explored_v = [x]
        self.visited[x] = True
        for v in self.get_edges(x):
            if not self.visited[v]:
                explored_v.extend(self.dfs(v))
        self.__post += 1
        self.postorder[x] = self.__post
        return explored_v

    def post_remove(self, node):
        self.postorder.pop(node)
    def node_remove(self, node):
        ver = self.data[node]
        for k,v in self.data.items():
            if node in v:
                v.remove(node)
                v.extend(ver)
        self.data.pop(node)








def toposort(adj):

    order = []

    invest = ADJL(adj)


    for i in xrange(len(adj)):
        invest.mark_dfs()
        idx, val = invest.max_post
        order.append(idx)
        invest.node_remove(idx)
        invest.post_remove(idx)
    return order

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
    order = toposort(adj)
    for x in order:
        print(x + 1)

