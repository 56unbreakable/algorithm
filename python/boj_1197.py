from queue import PriorityQueue

q = PriorityQueue()

v, e = map(int,input().split())
for _ in range(e):
    a, b, w = map(int,input().split())
    q.put((w,a,b))

parent = [i for i in range(v+1)]

def find(x):
    if x != parent[x]:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

size = 0
weight = 0

while not q.empty():
    node = q.get()

    w, a, b = node

    if find(a) == find(b):
        continue
    else:
        union(a,b)
        size += 1
        weight += w

    if size == v-1:
        break

print(weight)