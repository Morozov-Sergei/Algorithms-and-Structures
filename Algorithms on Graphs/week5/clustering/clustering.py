#Uses python3
import sys
import math

class Item:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.rank = 0

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.weight = w
    def __lt__(self, other):
        return self.weight < other.weight





def Find(i, nodes):
  if (i != nodes[i].idx) :
        nodes[i].idx = Find(nodes[i].idx, nodes)
  return nodes[i].idx

def Union(u, v, nodes):
    r1 = Find(u, nodes)
    r2 = Find(v, nodes)
    if (r1 != r2):
        if (nodes[r1].rank > nodes[r2].rank):
            nodes[r2].idx = r1
        else:
            nodes[r1].idx = r2
            if (nodes[r1].rank == nodes[r2].rank):
                nodes[r2].rank += 1

def MakeSet(i, nodes, x, y):
    nodes.append(Item(x[i], y[i], i))

def clustering(x, y, k):
    def get_w(i1, i2):
        return math.sqrt((x[i1] -x[i2])**2 +(y[i1]-y[i2])**2)

    edges = []
    nodes = []


    for i in range(len(x)):
       MakeSet(i, nodes, x, y)


    for idx1 in range(len(x)):
        for idx2 in range(idx1+1, len(x)):
            edges.append(Edge(idx1, idx2, get_w(idx1, idx2)))

    edges = sorted(edges)
    result = 0

    for edge in edges:
        if Find(edge.u, nodes) != Find(edge.v, nodes):
            result += 1
            Union(edge.u, edge.v, nodes)
        if(result > n - k):
            return edge.weight
    return -1.
#sys.stdin = open('../tests/c')
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
