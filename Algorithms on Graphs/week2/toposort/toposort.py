#Uses python3


import sys
class ADJL():
    def __init__(self, adj):
        self.__data = {k: adj[k] for k in range(len(adj))}
        self.__visited = {k:False for k in range(0, len(adj))}
        self.__postorder = {k:0 for k in range(0, len(adj))}
        self.__post = 0
        self.__order = []

    @property
    def max_post(self):
        idx, val = list(self.postorder.items())[0]
        for k, v in self.postorder.items():
            if v > val:
                idx = k
                val = v
        return idx, val

    @property
    def postorder(self):
        return self.__postorder
    @postorder.setter
    def postorder(self, value):
        self.__postorder = value

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def visited(self):
        return self.__visited
    @visited.setter
    def visited(self, value):
        self.__visited = value

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

    def start_topsort(self):
        for i in range(len(self.data.keys())):
            if not self.visited[i]:
                self.topsort(i)
        return reversed(self.__order)

    def topsort(self, x):
        self.visited[x] = True
        for v in self.get_edges(x):
            if not self.visited[v]:
                self.topsort(v)
        self.__order.append(x)
        #print('END_L', x)





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

    return invest.start_topsort()

#sys.stdin = open('../tests/h')

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

