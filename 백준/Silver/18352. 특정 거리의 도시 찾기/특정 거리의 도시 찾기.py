from collections import deque

# 도시갯수, 도로갯수, 최단거리, 출발 도시 번호
n, m, k2, x = map(int,input().split())
graph = [[]for _ in range(n+1)]
depth = [0 for _ in range(n+1)]


for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b) # 단방향 도로

q = deque()
q.append(x)
depth[x] = 0
while q:
    k = q.popleft()
    for i in (graph[k]):
        if depth[i] == 0:
            depth[i] += depth[k] + 1
            q.append(i)

depth[x] = -1

for i in range(len(depth)):
    if depth[i] == k2:
        print(i)
if k2 not in depth:
    print(-1)
