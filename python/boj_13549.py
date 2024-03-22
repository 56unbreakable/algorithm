from collections import deque

n, k = map(int,input().split())

q = deque()

visited = [False for _ in range(100001)]
depth = [0 for _ in range(100001)]

q.append(n)
visited[n] = True

while q:
    if visited[k]:
        break

    curr = q.popleft()

    if 0<= curr*2 <= 100000 and curr*2 not in q and not visited[curr*2]:
        q.append(curr * 2)
        visited[curr * 2] = True
        depth[curr * 2] =  depth[curr]

    if 0<= curr-1 <= 100000 and curr-1 not in q and not visited[curr-1]:
        q.append(curr - 1)
        visited[curr-1] = True
        depth[curr - 1] = depth[curr] + 1

    if 0<= curr+1 <= 100000 and curr+1  not in q and not visited[curr+1]:
        q.append(curr + 1)
        visited[curr+1] = True
        depth[curr + 1] =  depth[curr] + 1


print(depth[k])
