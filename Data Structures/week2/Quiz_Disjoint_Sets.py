

smallest = [ 0 for _ in range(1,14)]
print(smallest)
print(len(smallest))
def MakeSet(i):
    global smallest
    smallest[i] = i

def Union(x,y):
    global smallest
    if smallest[x] <= smallest [y]:
        smallest[y] = smallest[x]
    else:
        smallest[x] = smallest[y]

def Find(i):
    global smallest
    return smallest[i]
for i in range(1, 12):
    MakeSet(i)
Union(2, 10)
Union(7, 5)
Union(6, 1)
Union(3, 4)
Union(5, 11)
Union(7, 8)
Union(7, 3)
Union(12, 2)
Union(9, 6)
print(Find(6))
print(Find(3))
print(Find(11))
print(Find(9))
