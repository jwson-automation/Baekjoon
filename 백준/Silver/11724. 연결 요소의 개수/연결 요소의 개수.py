import sys
sys.setrecursionlimit(10000)

N, M = map(int,input().split())

graph = [[] for _ in range (N+1)]
visited = [False] * (N+1)

for k in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

answer = 0

for t in range(1, N+1):
    if visited[t] : continue
    answer += 1
    dfs(graph, t, visited)
    

print(answer)