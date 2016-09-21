# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    global ans,lines
    rDest, rSource = getParent(destination), getParent(source)
    if rDest == rSource:
        return False
    if rank[rSource] > rank[rDest]:
        lines[rSource] += lines[rDest]
        if lines[rSource] > ans:
            ans = lines[rSource]
        lines[rDest] = 0
        parent[rDest] = rSource
    else:
        lines[rDest] += lines[rSource]
        if lines[rDest] > ans:
            ans = lines[rDest]
        lines[rSource] = 0
        parent[rSource] = rDest
        if rank[rSource] == rank[rDest]:
            rank[rDest] += 1
    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

